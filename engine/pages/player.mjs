import {LocalLibrary, RemoteSource, ApiError, makeIndexes, privateFetch, blobIds, prefetch} from './local-files.mjs';
import {attachTouch} from './touch.mjs';

// The page goes straight into the game. The game repository is public, so the
// files are read without a key; a read-only key is asked for only when GitHub
// limits requests without one. HD or original graphics: the row HD Graphics in
// the game's own menu (F5), or Ctrl+H.

const baseURL = new URL('./', location.href);
const library = new LocalLibrary(baseURL.pathname);
const networkFetch = window.fetch.bind(window);
const query = new URLSearchParams(location.search);
const $ = id => document.getElementById(id);
const canvas = $('canvas');
const statusElement = $('status');
let started = false;
// Resolved when the engine has drawn its first HD screen
let engineRunning;
const engineStarted = new Promise(resolve => { engineRunning = resolve; });

function status(text = '', error = false) {
  statusElement.textContent = text;
  statusElement.hidden = !text;
  statusElement.classList.toggle('error', error);
}

function showScreen(id) {
  for (const screen of ['key', 'ended']) $(screen).hidden = screen !== id;
}

function showKey(message = '') {
  showScreen('key');
  status();
  $('key-error').textContent = message;
  $('key-error').hidden = !message;
  $('token').focus();
}

function megabytes(bytes) {
  return Math.round(bytes / 1048576);
}

// Big files are fetched once and kept. The game waits for them, so the screen
// says what is coming and how far it has come. The music is inside SAMNMAX.001.
const fileNames = {'MONSTER.SOU': 'talen', 'SAMNMAX.001': 'spillet'};
function progress(name, done, size) {
  if (done >= size) {
    $('loading').hidden = true;
    return;
  }
  const what = fileNames[name] || name;
  $('loading-text').textContent = 'Laster ned ' + what + ': ' + megabytes(done) + ' av ' + megabytes(size) + ' MB';
  $('loading-bar').style.width = (100 * done / size).toFixed(1) + '%';
  $('loading').hidden = false;
}

// WebGL draws the game. Without it, ScummVM's software drawing is used.
function hasWebGL() {
  try {
    const test = document.createElement('canvas');
    return Boolean(test.getContext('webgl2') || test.getContext('webgl'));
  } catch {
    return false;
  }
}

// The whole screen: browsers allow it only after a click or a key, so it comes
// with the first one. In Chrome and Edge Esc then still reaches the game (skip a
// scene); holding Esc leaves full screen. Firefox leaves full screen on Esc, and
// the next click or key brings it back.
function fullscreen() {
  if (!started || document.fullscreenElement || !document.documentElement.requestFullscreen) return;
  document.documentElement.requestFullscreen({navigationUI: 'hide'})
    .then(() => navigator.keyboard?.lock?.(['Escape']))
    .catch(() => {});
}
window.addEventListener('mousedown', fullscreen, true);
window.addEventListener('keydown', fullscreen, true);

// The connection is gone; the game waits and the file is tried again
function waiting(seconds) {
  status('Mistet kontakten med GitHub. Prøver igjen om ' + seconds + ' s …');
}

$('key').addEventListener('submit', async event => {
  event.preventDefault();
  const token = $('token').value.trim();
  if (!token) return;
  $('token').value = '';
  await library.setMeta('token', token);
  // Keeps the game in the browser when space runs low
  if (navigator.storage?.persist) navigator.storage.persist().catch(() => false);
  startRemote(token);
});

$('folders-link').addEventListener('click', () => { $('folders').hidden = false; });
for (const kind of ['game', 'mod']) {
  $(kind + '-files').addEventListener('change', async event => {
    if (!event.target.files.length) return;
    status(kind === 'game' ? 'Lagrer spillfilene i nettleseren …' : 'Lagrer HD-grafikken i nettleseren …');
    try {
      await library.import(event.target.files, kind);
      if (navigator.storage?.persist) await navigator.storage.persist().catch(() => false);
      if (library.metadata.game && library.metadata.mod) {
        // Folders on this machine instead of the repository
        await library.setMeta('token', undefined);
        startLocal();
      } else {
        status('Velg ' + (kind === 'game' ? 'HD-mappen' : 'spillmappen') + ' også.');
      }
    } catch (error) {
      status(error.name === 'QuotaExceededError' ? 'Nettleseren har ikke nok lagringsplass.' : error.message, true);
    } finally {
      event.target.value = '';
    }
  });
}

$('again').addEventListener('click', () => location.reload());

async function startRemote(token) {
  showScreen(null);
  status('Henter fillisten fra GitHub …');
  const source = new RemoteSource(library, token, networkFetch, {progress, waiting});
  let rows;
  try {
    rows = await source.list();
  } catch (error) {
    if (error instanceof ApiError && !token) {
      // Without a key GitHub allows 60 requests an hour per address
      showKey('GitHub begrenser henting uten nøkkel akkurat nå. Lim inn en lesenøkkel, eller prøv igjen om en time.');
    } else if (error instanceof ApiError && [401, 403, 404].includes(error.status)) {
      await library.setMeta('token', undefined);
      showKey(error.message);
    } else {
      status(error instanceof TypeError ? 'Fikk ikke kontakt med GitHub. Sjekk nettet og last siden på nytt.' : error.message, true);
    }
    return;
  }
  // The speech (MONSTER.SOU, 183 MB) stays in memory while the game runs. Left
  // out with ?uten-lyd, and on devices that report less than 4 GB memory. The
  // music is inside SAMNMAX.001 and stays. Playing without MONSTER.SOU is not
  // tested in the browser.
  const withoutSound = query.has('uten-lyd') || (navigator.deviceMemory && navigator.deviceMemory < 4);
  await launch(source, withoutSound ? rows.filter(row => !/\/MONSTER\.SOU$/.test(row.path)) : rows);
  // Files an older HD pack had, are removed when the game has started
  setTimeout(() => library.pruneBlobs(blobIds(rows)).catch(() => {}), 30000);
  // The rest of the HD pack comes in the background, so the game does not stop
  // to wait for GitHub the first time it needs a figure or a room (?uten-forhenting: not)
  if (!query.has('uten-forhenting')) {
    engineStarted.then(() => new Promise(resolve => setTimeout(resolve, 5000)))
      .then(() => prefetch(source, rows))
      .then(count => console.log(`HD-pakken er i nettleseren (${count} filer)`))
      .catch(() => {});
  }
}

function startLocal() {
  return launch(library, [...library.metadata.game.files, ...library.metadata.mod.files]);
}

function sendKey(key, code, keyCode) {
  canvas.focus();
  const dispatch = type => canvas.dispatchEvent(new KeyboardEvent(type, {key, code, keyCode, which: keyCode, bubbles: true, cancelable: true}));
  dispatch('keydown');
  // ScummVM reads the key while polling; let it stay down for a moment
  setTimeout(() => dispatch('keyup'), 120);
}

// Touch on phones and tablets (touch.mjs): tap, drag, hold, two and three fingers
const keys = {F5: ['F5', 'F5', 116], Escape: ['Escape', 'Escape', 27]};
attachTouch(canvas, name => sendKey(...keys[name]));

canvas.addEventListener('contextmenu', event => event.preventDefault());
canvas.addEventListener('webglcontextlost', event => {
  event.preventDefault();
  status('Grafikken i nettleseren ble borte. Last siden på nytt.', true);
});

async function launch(source, rows) {
  if (started) return;
  started = true;
  showScreen(null);
  status('Laster spillmotoren …');
  try {
    const response = await networkFetch(new URL('data/index.json', baseURL));
    if (!response.ok) throw new Error('Fant ikke spillmotorens data. Last siden på nytt.');
    const indexes = makeIndexes(rows, await response.json());
    // A file the game could not get is shown, not swallowed
    const reader = {read: path => source.read(path).then(blob => {
      if (/^Mistet kontakten/.test(statusElement.textContent)) status();
      return blob;
    }, error => { status(error.message, true); throw error; })};
    window.fetch = privateFetch(reader, indexes, baseURL, networkFetch);

    // The DIGHD_ variables keep their names from The Dig.
    const env = {DIGHD_MOD: '/data/mods/gpt', HOME: '/home/sam-max-hd' + baseURL.pathname.replace(/[^a-zA-Z0-9_-]/g, '_')};
    if (query.has('rom')) {
      // The index of Sam & Max has 95 room slots (memory.md); not every number is a room
      const room = Number(query.get('rom'));
      if (!Number.isInteger(room) || room < 1 || room > 94) throw new Error('Romnummeret må være mellom 1 og 94.');
      Object.assign(env, {DIGHD_TEST_ROOM: String(room), DIGHD_TEST_AT: '240', DIGHD_SKIP_VIDEO: '1'});
    }
    if (query.has('klassisk')) env.DIGHD_CLASSIC = '1';
    if (query.has('gult')) env.DIGHD_SHOW_MISSING = '1';
    // The engine's test hooks work here too (docs/HD-MOTOR.md)
    for (const [key, value] of query) if (/^DIGHD_(TEST_[A-Z0-9_]+|SKIP_VIDEO|TEXT|VERIFY|BENCH)$/.test(key)) env[key] = value;
    const args = ['--path=/data/games/samnmax', '--savepath=' + env.HOME, '--aspect-ratio', '--subtitles'];
    if (query.has('programvare') || !hasWebGL()) args.push('--gfx-mode=surfacesdl');
    // The music: Roland MT-32 emulation with the ROMs from spilldata (or the chosen game folder)
    // ?adlib: AdLib instead, which costs far less in the browser (to compare if the game stutters)
    if (query.has('adlib')) args.push('--music-driver=adlib');
    else if (rows.some(row => /\/MT32_CONTROL\.ROM$/.test(row.path)) && rows.some(row => /\/MT32_PCM\.ROM$/.test(row.path))) args.push('--music-driver=mt32');
    args.push('samnmax');
    history.replaceState(null, '', location.pathname + location.search + '#' + args.join(' '));

    canvas.focus();
    // F5 is the game's menu, not reload; Ctrl+H is HD or classic (with the HD patch), not history
    window.addEventListener('keydown', event => {
      if (/^F([1-9]|10)$/.test(event.key) || event.key === 'Tab' || event.key === 'Backspace' ||
          ((event.ctrlKey || event.altKey) && !event.metaKey && event.key.length === 1)) event.preventDefault();
    }, true);
    // ScummVM asks for Web MIDI when it loads (dists/emscripten/custom_shell-pre.js),
    // and the browser then asks the player for permission. This blocks that question.
    // Sam & Max plays its music as MIDI (iMUSE), here through the MT-32 emulation
    // in the engine (--music-driver=mt32), so Web MIDI is not needed.
    Object.defineProperty(navigator, 'requestMIDIAccess', {configurable: true, value: () => new Promise(() => {})});
    window.Module = {
      canvas,
      locateFile: path => new URL(path, baseURL).href,
      preRun: [() => {
        for (const [key, value] of Object.entries(env)) ENV[key] = value;
        FS.mkdirTree(env.HOME);
      }],
      onRuntimeInitialized: () => status('Starter Sam & Max …'),
      onAbort: text => status('Spillmotoren stoppet: ' + text, true),
      onExit: () => { status(); showScreen('ended'); },
      print: text => {
        console.log(text);
        if (/Could not load any graphics mode/.test(text)) {
          status('Nettleseren fikk ikke tegnet spillet. Slå på maskinvareakselerasjon i nettleseren, eller legg ?programvare bak adressen.', true);
        }
        // The canvas gets its right size after a resize event. The line comes from
        // the HD patch, which does not run for Sam & Max yet: until it does, the
        // status line stays and the picture may be skewed until the window is
        // resized (Known Issues in dists/emscripten/README.md in ScummVM).
        if (/^DigHD: screen /.test(text)) {
          engineRunning();
          setTimeout(() => {
            window.dispatchEvent(new Event('resize'));
            if (!statusElement.classList.contains('error')) status();
          }, 300);
        }
      },
      printErr: text => console.error(text),
      setStatus: text => { if (text) console.log(text); }
    };
    // An engine that stops must not leave the page looking like it is still starting
    window.addEventListener('error', event => status('Spillmotoren stoppet: ' + (event.message || 'ukjent feil'), true));
    window.addEventListener('unhandledrejection', event => {
      if (!statusElement.classList.contains('error')) status('Spillmotoren stoppet: ' + (event.reason?.message || event.reason || 'ukjent feil'), true);
    });
    const script = document.createElement('script');
    script.src = new URL('scummvm.js', baseURL).href;
    script.onerror = () => status('Spillmotoren kunne ikke lastes. Last siden på nytt.', true);
    document.body.appendChild(script);
  } catch (error) {
    started = false;
    window.fetch = networkFetch;
    status(error.message, true);
  }
}

try {
  if (!globalThis.WebAssembly) throw new Error('Denne nettleseren støtter ikke spillmotoren. Bruk en oppdatert Chrome, Edge eller Firefox.');
  await library.open();
  // ?ny-nokkel asks for a new key
  const token = query.has('ny-nokkel') ? null : await library.getMeta('token');
  if (token) await startRemote(token);
  else if (query.has('ny-nokkel')) showKey();
  else if (library.metadata.game && library.metadata.mod) await startLocal();
  else await startRemote(null);
} catch (error) {
  status('Kunne ikke starte: ' + error.message, true);
}
