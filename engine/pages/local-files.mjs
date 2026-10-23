// The game and the HD pack never come from this site. They are read from the
// game repository on GitHub (public: without a key from raw.githubusercontent.com,
// or with the owner's own read-only key through the API), or from folders on this
// machine, and kept in IndexedDB. Only the ScummVM engine is downloaded from the site.
export const GAME_ROOT = '/data/games/samnmax/';
export const MOD_ROOT = '/data/mods/gpt/';

// The game repository and the branches the files come from.
export const REPO = 'Tombonator3000/Sam-Max-HD';
export const SOURCES = [
  {branch: 'spilldata', prefix: 'game/', kind: 'game'},
  {branch: 'hd-mod', prefix: '', kind: 'mod'}
];
const API = 'https://api.github.com/repos/' + REPO + '/';
const RAW = 'https://raw.githubusercontent.com/' + REPO + '/';

export function selectFiles(files, kind) {
  const root = kind === 'game' ? GAME_ROOT : MOD_ROOT;
  const selected = new Map();
  for (const file of files) {
    const parts = (file.webkitRelativePath || file.name).split('/');
    if (file.webkitRelativePath) parts.shift();
    if (parts.some(part => !part || part === '.' || part === '..')) continue;
    let relative = parts.join('/');
    if (kind === 'game') {
      relative = relative.toUpperCase();
      // Sam & Max CD: index, data (with the music), speech, and the optional MT-32 ROMs
      if (!/^(SAMNMAX\.(000|001)|MONSTER\.SOU|MT32_(CONTROL|PCM)\.ROM)$/.test(relative)) continue;
    } else {
      if (!/^(mod\.json|rooms\/room\d+(?:\.(?:png|webp)|_(?:idx|mask)\.png)|objects\/obj\d+_[0-9a-fA-F]{2}(?:(?:_hd)?\.(?:png|webp)|_(?:idx|mask)\.png)|costumes\/costume\d+_\d+(?:(?:_hd)?\.(?:png|webp)|_(?:idx|mask)\.png)|fonts\/[a-z0-9-]+\.(txt|png|webp))$/.test(relative)) continue;
    }
    const path = root + relative;
    if (selected.has(path)) throw new Error('To filer har samme navn: ' + relative);
    selected.set(path, {path, size: file.size, blob: file});
  }
  if (kind === 'game' && (!selected.has(root + 'SAMNMAX.000') || !selected.has(root + 'SAMNMAX.001'))) {
    throw new Error('Velg mappen som inneholder SAMNMAX.000 og SAMNMAX.001.');
  }
  if (kind !== 'game' && (!selected.has(root + 'mod.json') || ![...selected.keys()].some(p => /\/rooms\/room\d+\.(?:png|webp)$/.test(p)))) {
    throw new Error('Velg HD-mappen som inneholder mod.json og rooms.');
  }
  return [...selected.values()];
}

// What the page shows about a chosen folder. Counts the HD images, not the _idx files.
// A figure cel can have both a cut-out image and a soft one (_hd.png); it counts once.
// The same for an object image (the icons with their own soft alpha, objNNN_SS_hd.png).
export function summarize(rows, created = null) {
  const count = re => rows.filter(row => re.test(row.path)).length;
  return {
    files: rows.map(({path, size}) => ({path, size})),
    bytes: rows.reduce((sum, row) => sum + row.size, 0),
    rooms: new Set(rows.map(row => row.path.match(/\/rooms\/(room\d+)\.(?:png|webp)$/)?.[1]).filter(Boolean)).size,
    objects: new Set(rows.map(row => row.path.match(/\/objects\/(obj\d+_[0-9a-fA-F]{2})(_hd)?\.(?:png|webp)$/)?.[1]).filter(Boolean)).size,
    cels: new Set(rows.map(row => row.path.match(/\/costumes\/(costume\d+_\d+)(_hd)?\.(?:png|webp)$/)?.[1]).filter(Boolean)).size,
    created
  };
}

export function makeIndexes(rows, staticRoot = {}) {
  const indexes = new Map([['/data/index.json', {...staticRoot}]]);
  for (const {path, size} of rows) {
    const parts = path.split('/').filter(Boolean);
    if (parts.shift() !== 'data' || parts.some(p => p === '..' || p === '.')) throw new Error('Ugyldig filsti');
    let directory = '/data';
    for (let i = 0; i < parts.length; i++) {
      const key = directory + '/index.json';
      if (!indexes.has(key)) indexes.set(key, {});
      const index = indexes.get(key);
      index[parts[i]] = i === parts.length - 1 ? size : {};
      directory += '/' + parts[i];
    }
  }
  return indexes;
}

// A git tree listing as rows for makeIndexes(), with the same rules as a chosen folder.
// Files over GitHub's 100 MB limit (the speech, MONSTER.SOU) lie in parts
// MONSTER.SOU.001, MONSTER.SOU.002 and so on; they become one row with the parts
// in order. A part number comes after the file's own extension, so SAMNMAX.000
// and SAMNMAX.001 stay two files.
export function treeRows(tree, prefix, kind, branch = '') {
  const files = new Map();
  for (const item of tree) {
    if (item.type !== 'blob' || !item.path.startsWith(prefix)) continue;
    const part = /^(.+\.[A-Za-z0-9]+)\.(\d{3})$/.exec(item.path.slice(prefix.length));
    const relative = part ? part[1] : item.path.slice(prefix.length);
    const file = files.get(relative) || {name: relative.split('/').at(-1), webkitRelativePath: 'repo/' + relative, size: 0, parts: []};
    file.size += item.size;
    file.parts.push({n: part ? Number(part[2]) : 0, sha: item.sha, size: item.size, raw: branch ? branch + '/' + item.path : undefined});
    files.set(relative, file);
  }
  return selectFiles([...files.values()], kind).map(row => {
    const parts = row.blob.parts.sort((a, b) => a.n - b.n);
    const out = {path: row.path, size: row.size, sha: parts.map(p => p.sha).join('+')};
    if (parts.length > 1) out.parts = parts.map(({sha, size, raw}) => (raw ? {sha, size, raw} : {sha, size}));
    else if (parts[0].raw) out.raw = parts[0].raw;
    return out;
  });
}

// All blob ids a listing uses (the parts of split files count one by one)
export function blobIds(rows) {
  return new Set(rows.flatMap(row => row.parts ? row.parts.map(p => p.sha) : [row.sha]));
}

export class ApiError extends Error {
  constructor(status, message) {
    super(message);
    this.status = status;
  }
}

function apiError(status) {
  if (status === 401) return new ApiError(status, 'GitHub godtar ikke nøkkelen. Lag en ny og lim den inn.');
  if (status === 403 || status === 404) return new ApiError(status, 'Nøkkelen har ikke lesetilgang til ' + REPO + '.');
  return new ApiError(status, 'GitHub svarte ' + status + '. Prøv igjen litt senere.');
}

// Reads a response while telling how far it has come; big files show progress.
async function readBody(response, size, progress) {
  if (!response.body || !progress) return response.blob();
  const reader = response.body.getReader();
  const chunks = [];
  let done = 0;
  for (;;) {
    const part = await reader.read();
    if (part.done) break;
    chunks.push(part.value);
    done += part.value.length;
    progress(done, size);
  }
  progress(size, size);
  return new Blob(chunks);
}

const wait = ms => new Promise(resolve => setTimeout(resolve, ms));

// The files from the branches of the game repository, fetched when the engine asks for them
// and kept by git blob id, so a new HD pack only fetches what has changed.
// A lost connection is tried again and again while the game waits: a file the
// engine cannot open stops the game.
//   progress(name, done, size): big files on their way
//   waiting(seconds): the connection is gone, next try in so many seconds
export class RemoteSource {
  constructor(library, token, networkFetch, {progress = null, waiting = null, sleep = wait} = {}) {
    this.library = library;
    this.token = token;
    this.fetch = networkFetch;
    this.progress = progress;
    this.waiting = waiting;
    this.sleep = sleep;
    this.rows = new Map();
  }

  // Without a key the repository is read as a public one: the file lists from the
  // API (two requests), the files themselves from raw.githubusercontent.com.
  api(path, accept, cache = 'default') {
    const headers = {Accept: accept};
    if (this.token) headers.Authorization = 'Bearer ' + this.token;
    return this.fetch(API + path, {headers, cache});
  }

  // Runs attempt() until it works. Network errors, 5xx, 429 and rate limits are
  // tried again (at most `tries` times), a key GitHub rejects is not.
  async retry(attempt, tries = Infinity) {
    for (let n = 1; ; n++) {
      let delay = Math.min(1000 * 2 ** (n - 1), 15000);
      try {
        return await attempt();
      } catch (error) {
        const limited = error instanceof ApiError && (error.status === 429 || error.status >= 500 || error.rateLimited);
        if (!(error instanceof TypeError || limited) || n >= tries) throw error;
        if (error.retryAfter) delay = Math.min(error.retryAfter * 1000, 60000);
      }
      this.waiting?.(Math.round(delay / 1000));
      await this.sleep(delay);
    }
  }

  async get(path, accept, cache) {
    const response = await this.api(path, accept, cache);
    if (response.ok) return response;
    const error = apiError(response.status);
    error.rateLimited = response.status === 403 && (response.headers.get('x-ratelimit-remaining') === '0' || response.headers.has('retry-after'));
    error.retryAfter = Number(response.headers.get('retry-after')) || 0;
    throw error;
  }

  async getRaw(raw) {
    const response = await this.fetch(RAW + raw.split('/').map(encodeURIComponent).join('/'));
    if (response.ok) return response;
    const error = apiError(response.status);
    error.retryAfter = Number(response.headers.get('retry-after')) || 0;
    throw error;
  }

  // The file lists of both branches. Offline, the last list is used.
  async list() {
    let rows = [];
    try {
      for (const source of SOURCES) {
        const data = await this.retry(async () =>
          (await this.get('git/trees/' + source.branch + '?recursive=1', 'application/vnd.github+json', 'no-store')).json(), 3);
        if (data.truncated) throw new Error('Fillisten fra GitHub ble avkortet.');
        rows.push(...treeRows(data.tree, source.prefix, source.kind, source.branch));
      }
      await this.library.setMeta('listing', rows);
    } catch (error) {
      const saved = error instanceof TypeError ? await this.library.getMeta('listing') : null;
      if (!saved) throw error;
      rows = saved;
    }
    this.rows = new Map(rows.map(row => [row.path, row]));
    return rows;
  }

  // quiet: no progress line (the background fetch, see prefetch())
  async read(path, {quiet = false} = {}) {
    const row = this.rows.get(path);
    if (!row) return undefined;
    const name = path.split('/').at(-1);
    const parts = row.parts || [{sha: row.sha, size: row.size, raw: row.raw}];
    const blobs = [];
    let before = 0;
    for (const part of parts) {
      blobs.push(await this.blob(part, name, before, row.size, quiet));
      before += part.size;
    }
    return blobs.length === 1 ? blobs[0] : new Blob(blobs);
  }

  // One git blob, from the browser if it is there, else from GitHub. A blob that
  // is on its way (the game and the background fetch want the same) is fetched once.
  // A background read (quiet) tries once and gives up on a limit from GitHub, so it
  // never holds up the game; the game then fetches the blob itself.
  blob(part, name, before, total, quiet = false) {
    this.pending ??= new Map();
    let promise = this.pending.get(part.sha);
    if (!promise) {
      promise = this.fetchBlob(part, name, before, total, quiet).finally(() => this.pending.delete(part.sha));
      promise.background = quiet;
      this.pending.set(part.sha, promise);
    }
    if (!quiet && promise.background) return promise.catch(() => this.blob(part, name, before, total, false));
    return promise;
  }

  async fetchBlob({sha, size, raw}, name, before, total, quiet) {
    const cached = await this.library.getBlob(sha);
    if (cached) return cached;
    const progress = !quiet && this.progress && ((done) => this.progress(name, before + done, total));
    const blob = await this.retry(async () => {
      const response = !this.token && raw ? await this.getRaw(raw) : await this.get('git/blobs/' + sha, 'application/vnd.github.raw+json');
      const body = await readBody(response, size, progress && total >= 4 * 1048576 ? progress : null);
      // A connection that breaks off can give a short body without an error
      if (body.size !== size) throw new TypeError('Filen kom ikke helt fram.');
      return body;
    }, quiet ? 1 : Infinity);
    await this.library.putBlob(sha, blob);
    return blob;
  }
}

// Fetches the HD pack into the browser in the background while the game runs,
// so the game does not wait for GitHub the first time it needs a figure cel, an
// object or a room (it stopped for a moment each time, most in the middle of
// animations). Figure cels first, then objects, rooms and the rest. Files that
// are in the browser already cost one lookup. Returns the number of files read.
export async function prefetch(source, rows, {workers = 2, stop = () => false, pause = 60000, sleep = ms => new Promise(r => setTimeout(r, ms))} = {}) {
  // The index images of cels without an HD image (the engine smooths them) are
  // many and small: last, the game fetches them itself when it needs them.
  const paths = new Set(rows.map(row => row.path));
  const indexOnly = path => /\/costumes\/.*_idx\.png$/.test(path) &&
    !['_hd.png', '_hd.webp', '.png', '.webp'].some(suffix => paths.has(path.replace(/_idx\.png$/, suffix)));
  const rank = path => indexOnly(path) ? 4 : /\/costumes\//.test(path) ? 0 : /\/objects\//.test(path) ? 1 : /\/rooms\//.test(path) ? 2 : 3;
  const queue = rows.filter(row => row.path.startsWith(MOD_ROOT))
    .sort((a, b) => rank(a.path) - rank(b.path) || (a.path < b.path ? -1 : a.path > b.path ? 1 : 0));
  let next = 0, read = 0, pausedUntil = 0;
  const work = async () => {
    while (next < queue.length && !stop()) {
      // GitHub limits the number of requests: on a limit the background fetch
      // waits a minute, so the files the game needs come first
      if (Date.now() < pausedUntil) {
        await sleep(pausedUntil - Date.now());
        continue;
      }
      const row = queue[next++];
      try {
        if (await source.read(row.path, {quiet: true})) read++;
      } catch (error) {
        if (error instanceof ApiError && (error.status === 429 || error.status === 403 || error.rateLimited)) {
          pausedUntil = Date.now() + pause;
          row.tries = (row.tries || 0) + 1;
          if (row.tries < 3) queue.push(row);  // tried again at the end
        }
        // Otherwise the game asks for the file again when it needs it
      }
    }
  };
  await Promise.all(Array.from({length: workers}, work));
  return read;
}

function requestResult(request) {
  return new Promise((resolve, reject) => {
    request.onsuccess = () => resolve(request.result);
    request.onerror = () => reject(request.error);
  });
}

export class LocalLibrary {
  constructor(basePath) {
    // GitHub Pages projects share an origin; keep this game's cache separate.
    this.name = 'sam-max-hd-files:' + basePath;
    this.db = null;
    this.metadata = {};
  }

  async open() {
    const request = indexedDB.open(this.name, 2);
    request.onupgradeneeded = () => {
      const db = request.result;
      // files: chosen folders; blobs: files from GitHub by blob id
      if (!db.objectStoreNames.contains('files')) db.createObjectStore('files', {keyPath: 'path'});
      if (!db.objectStoreNames.contains('metadata')) db.createObjectStore('metadata');
      if (!db.objectStoreNames.contains('blobs')) db.createObjectStore('blobs');
    };
    this.db = await requestResult(request);
    this.db.onversionchange = () => this.db.close();
    const store = this.db.transaction('metadata').objectStore('metadata');
    const [game, mod] = await Promise.all(['game', 'mod'].map(key => requestResult(store.get(key))));
    this.metadata = {game, mod};
    return this.metadata;
  }

  async import(files, kind) {
    const rows = selectFiles(files, kind);
    let mod;
    if (kind === 'mod') {
      mod = JSON.parse(await rows.find(row => row.path === MOD_ROOT + 'mod.json').blob.text());
      if (mod.format !== 1 || mod.scale !== 4) throw new Error('HD-pakken må være i DigHD-format 1 med skala 4.');
    }
    const prefix = kind === 'game' ? GAME_ROOT : MOD_ROOT;
    const metadata = summarize(rows, mod?.created || null);
    await new Promise((resolve, reject) => {
      const tx = this.db.transaction(['files', 'metadata'], 'readwrite');
      tx.oncomplete = resolve;
      tx.onerror = () => reject(tx.error);
      tx.onabort = () => reject(tx.error || new Error('Lagringen ble avbrutt.'));
      const store = tx.objectStore('files');
      // Replacement is atomic: a storage error preserves the previous usable set.
      store.delete(IDBKeyRange.bound(prefix, prefix + '\uffff'));
      for (const row of rows) store.put({path: row.path, blob: row.blob});
      tx.objectStore('metadata').put(metadata, kind);
    });
    this.metadata[kind] = metadata;
    return metadata;
  }

  async read(path) {
    const row = await requestResult(this.db.transaction('files').objectStore('files').get(path));
    return row?.blob;
  }

  getMeta(key) {
    return requestResult(this.db.transaction('metadata').objectStore('metadata').get(key));
  }

  setMeta(key, value) {
    const store = this.db.transaction('metadata', 'readwrite').objectStore('metadata');
    return requestResult(value === undefined ? store.delete(key) : store.put(value, key));
  }

  getBlob(sha) {
    return requestResult(this.db.transaction('blobs').objectStore('blobs').get(sha));
  }

  putBlob(sha, blob) {
    return requestResult(this.db.transaction('blobs', 'readwrite').objectStore('blobs').put(blob, sha));
  }

  // Removes files an older HD pack had, but the current one does not
  async pruneBlobs(keep) {
    const store = this.db.transaction('blobs', 'readwrite').objectStore('blobs');
    const keys = await requestResult(store.getAllKeys());
    await Promise.all(keys.filter(key => !keep.has(key)).map(key => requestResult(store.delete(key))));
  }

  async clear() {
    await new Promise((resolve, reject) => {
      const tx = this.db.transaction(['files', 'metadata', 'blobs'], 'readwrite');
      tx.oncomplete = resolve;
      tx.onerror = () => reject(tx.error);
      tx.onabort = () => reject(tx.error || new Error('Slettingen ble avbrutt.'));
      tx.objectStore('files').clear();
      tx.objectStore('metadata').clear();
      tx.objectStore('blobs').clear();
    });
    this.metadata = {};
  }
}

// source: LocalLibrary (chosen folders) or RemoteSource (the branches of the game repository)
export function privateFetch(source, indexes, baseURL, networkFetch) {
  return async (input, options) => {
    const url = new URL(typeof input === 'string' || input instanceof URL ? input : input.url, baseURL);
    if (url.origin !== baseURL.origin || !url.pathname.startsWith('/data/')) return networkFetch(input, options);
    const path = decodeURIComponent(url.pathname);
    const headers = {'Cache-Control': 'no-store'};
    if (indexes.has(path)) {
      headers['Content-Type'] = 'application/json';
      return new Response(JSON.stringify(indexes.get(path)), {headers});
    }
    if (path.startsWith(GAME_ROOT) || path.startsWith('/data/mods/')) {
      const blob = await source.read(path);
      // Never send a game/HD filename to GitHub or another server, even if missing.
      return new Response(blob || null, {status: blob ? 200 : 404, headers});
    }
    // Built-in ScummVM themes/translations use /data, but Pages has a project prefix.
    return networkFetch(new URL('data/' + path.slice('/data/'.length), baseURL), options);
  };
}
