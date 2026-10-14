import test from 'node:test';
import assert from 'node:assert/strict';
import {selectFiles, makeIndexes, privateFetch, summarize, treeRows, blobIds, RemoteSource, ApiError, REPO, GAME_ROOT, MOD_ROOT, prefetch} from '../local-files.mjs';

const file = (name, content = 'sample') => ({name: name.split('/').at(-1), webkitRelativePath: name, size: content.length});

test('imports game files from a directory without importing unrelated files', () => {
  const rows = selectFiles([file('game/samnmax.000'), file('game/samnmax.001'), file('game/monster.sou'), file('game/token.txt'), file('game/SHA256SUMS')], 'game');
  assert.deepEqual(rows.map(row => row.path), [GAME_ROOT + 'SAMNMAX.000', GAME_ROOT + 'SAMNMAX.001', GAME_ROOT + 'MONSTER.SOU']);
  assert.throws(() => selectFiles([file('game/SAMNMAX.000')], 'game'), /SAMNMAX.001/);
  assert.throws(() => selectFiles([file('game/SAMNMAX.001'), file('game/MONSTER.SOU')], 'game'), /SAMNMAX.000/);
});

test('the MT-32 ROMs are optional game files; other files in the game folder are left out', () => {
  const rows = selectFiles([
    file('game/SAMNMAX.000'), file('game/SAMNMAX.001'),
    file('game/MT32_CONTROL.ROM'), file('game/mt32_pcm.rom'),
    file('game/SAMNMAX.002'), file('game/OTHER.ROM'), file('game/sub/MONSTER.SOU')], 'game');
  assert.deepEqual(rows.map(row => row.path),
    [GAME_ROOT + 'SAMNMAX.000', GAME_ROOT + 'SAMNMAX.001', GAME_ROOT + 'MT32_CONTROL.ROM', GAME_ROOT + 'MT32_PCM.ROM']);
});

test('HD references, prompts and film frames are excluded; an incomplete mod is rejected', () => {
  // Sam & Max has no SMUSH films, so san/ (film frames in The Dig) is not part of the mod
  const rows = selectFiles([file('gpt/mod.json'), file('gpt/rooms/room022.png'), file('gpt/rooms/room022_idx.png'), file('gpt/prompt.txt'), file('gpt/referanse.png'), file('gpt/san/INTRO/00001.png')], 'mod');
  assert.equal(rows.length, 3);
  assert.throws(() => selectFiles([file('gpt/mod.json')], 'mod'), /HD-mappen/);
  assert.throws(() => selectFiles([file('gpt/mod.json'), file('gpt/rooms/room022.png'), file('gpt/rooms/room022.png')], 'mod'), /samme navn/);
});

test('HD objects and figure cels are imported and counted without their _idx files', () => {
  const rows = selectFiles([
    file('gpt/mod.json'), file('gpt/rooms/room022.png'), file('gpt/rooms/room022_idx.png'),
    file('gpt/objects/obj097_0a.png'), file('gpt/objects/obj097_0a_idx.png'),
    file('gpt/costumes/costume014_003.png'), file('gpt/costumes/costume014_003_idx.png'),
    file('gpt/costumes/costume014_016.png'), file('gpt/costumes/costume014_016_idx.png'),
    file('gpt/costumes/costume014_016_hd.png'),
    file('gpt/fonts/map.txt'), file('gpt/fonts/exo2.png'), file('gpt/fonts/exo2.txt'), file('gpt/fonts/OFL.txt'),
    file('gpt/SHA256SUMS'), file('gpt/README.md')], 'mod');
  assert.equal(rows.length, 13);
  assert.ok(rows.some(row => row.path === MOD_ROOT + 'fonts/map.txt'));
  assert.ok(rows.some(row => row.path === MOD_ROOT + 'fonts/exo2.png'));
  assert.ok(rows.some(row => row.path === MOD_ROOT + 'costumes/costume014_016_hd.png'));
  assert.ok(rows.some(row => row.path === MOD_ROOT + 'costumes/costume014_016_idx.png'));
  const sum = summarize(rows, '2026-10-09 09:49');
  assert.deepEqual([sum.rooms, sum.objects, sum.cels, sum.created], [1, 1, 2, '2026-10-09 09:49']);
  assert.equal(sum.bytes, 13 * 'sample'.length);
});

test('ScummVM directory indexes combine local game/HD files with built-in themes', () => {
  const indexes = makeIndexes([{path: GAME_ROOT + 'MONSTER.SOU', size: 45}, {path: MOD_ROOT + 'rooms/room022.png', size: 23}], {'scummmodern.zip': 99});
  assert.deepEqual(indexes.get('/data/index.json'), {'scummmodern.zip': 99, games: {}, mods: {}});
  assert.deepEqual(indexes.get('/data/games/index.json'), {samnmax: {}});
  assert.deepEqual(indexes.get('/data/games/samnmax/index.json'), {'MONSTER.SOU': 45});
  assert.deepEqual(indexes.get('/data/mods/gpt/rooms/index.json'), {'room022.png': 23});
});

test('private data and missing private files never reach the network; themes use the Pages prefix', async () => {
  const requests = [];
  const base = new URL('https://example.github.io/Sam-Max-HD-Web/');
  const fetch = privateFetch({read: async path => path.endsWith('SAMNMAX.000') ? new Blob(['local']) : undefined}, makeIndexes([{path: GAME_ROOT + 'SAMNMAX.000', size: 5}]), base, async url => {
    requests.push(String(url)); return new Response('network');
  });
  assert.equal(await (await fetch(GAME_ROOT + 'SAMNMAX.000')).text(), 'local');
  assert.equal((await fetch(GAME_ROOT + 'MONSTER.SOU')).status, 404);
  assert.equal((await fetch(MOD_ROOT + 'missing.png')).status, 404);
  assert.deepEqual(requests, []);
  assert.equal(await (await fetch('/data/scummmodern.zip')).text(), 'network');
  assert.deepEqual(requests, ['https://example.github.io/Sam-Max-HD-Web/data/scummmodern.zip']);
});

const tree = [
  {path: 'README.md', type: 'blob', sha: 'r', size: 10},
  {path: 'game', type: 'tree', sha: 't'},
  {path: 'game/SAMNMAX.000', type: 'blob', sha: 'a0', size: 7},
  {path: 'game/SAMNMAX.001', type: 'blob', sha: 'a1', size: 7},
  {path: 'game/MT32_CONTROL.ROM', type: 'blob', sha: 'r1', size: 7},
  {path: 'game/SHA256SUMS', type: 'blob', sha: 'x', size: 3}
];
const modTree = [
  {path: 'mod.json', type: 'blob', sha: 'm', size: 6},
  {path: 'rooms/room022.png', type: 'blob', sha: 'r22', size: 8},
  {path: 'costumes/costume014_003.png', type: 'blob', sha: 'c3', size: 7},
  {path: 'SHA256SUMS', type: 'blob', sha: 'y', size: 3}
];

test('git tree listings become the same paths as chosen folders, with blob ids', () => {
  assert.deepEqual(treeRows(tree, 'game/', 'game'), [
    {path: GAME_ROOT + 'SAMNMAX.000', size: 7, sha: 'a0'},
    {path: GAME_ROOT + 'SAMNMAX.001', size: 7, sha: 'a1'},
    {path: GAME_ROOT + 'MT32_CONTROL.ROM', size: 7, sha: 'r1'}]);
  assert.deepEqual(treeRows(modTree, '', 'mod').map(row => row.path),
    [MOD_ROOT + 'mod.json', MOD_ROOT + 'rooms/room022.png', MOD_ROOT + 'costumes/costume014_003.png']);
});

function memoryLibrary() {
  const blobs = new Map(), meta = new Map();
  return {
    blobs,
    getBlob: async sha => blobs.get(sha),
    putBlob: async (sha, blob) => { blobs.set(sha, blob); },
    getMeta: async key => meta.get(key),
    setMeta: async (key, value) => { meta.set(key, value); }
  };
}

function github(requests, status = 200) {
  return async (url, options) => {
    requests.push({url: String(url), auth: options?.headers?.Authorization, accept: options?.headers?.Accept});
    if (status !== 200) return new Response('{}', {status});
    const u = new URL(url);
    if (u.pathname.endsWith('/git/trees/spilldata')) return Response.json({tree, truncated: false});
    if (u.pathname.endsWith('/git/trees/hd-mod')) return Response.json({tree: modTree, truncated: false});
    if (u.pathname.includes('/git/blobs/')) return new Response('blob ' + u.pathname.split('/').at(-1));
    if (u.hostname === 'raw.githubusercontent.com') {
      // /<owner>/<repo>/<branch>/<path>: the same content as the blob in the tree
      const [, , , branch, ...rest] = decodeURIComponent(u.pathname).split('/');
      const item = (branch === 'hd-mod' ? modTree : tree).find(i => i.path === rest.join('/'));
      return item ? new Response('blob ' + item.sha) : new Response('', {status: 404});
    }
    return new Response('', {status: 404});
  };
}

test('files come from the private branches with the key, once per blob id', async () => {
  const requests = [];
  const library = memoryLibrary();
  const source = new RemoteSource(library, 'KEY', github(requests));
  const rows = await source.list();
  assert.equal(rows.length, 6);
  assert.ok(requests.every(r => r.url.startsWith('https://api.github.com/repos/' + REPO + '/') && r.auth === 'Bearer KEY'));
  assert.equal(await (await source.read(GAME_ROOT + 'SAMNMAX.001')).text(), 'blob a1');
  assert.equal(await (await source.read(GAME_ROOT + 'SAMNMAX.001')).text(), 'blob a1');
  assert.equal(requests.filter(r => r.url.includes('/git/blobs/a1')).length, 1);
  assert.equal(requests.find(r => r.url.includes('/git/blobs/')).accept, 'application/vnd.github.raw+json');
  assert.equal(await source.read(GAME_ROOT + 'MONSTER.SOU'), undefined);
  assert.equal(requests.length, 3);

  // Offline: the last list is used, and kept files still work
  const offline = new RemoteSource(library, 'KEY', async () => { throw new TypeError('Failed to fetch'); });
  assert.equal((await offline.list()).length, 6);
  assert.equal(await (await offline.read(GAME_ROOT + 'SAMNMAX.001')).text(), 'blob a1');
});

test('without a key the public repository is read: lists from the API, files from raw.githubusercontent.com', async () => {
  const requests = [];
  const source = new RemoteSource(memoryLibrary(), null, github(requests));
  const rows = await source.list();
  assert.equal(rows.length, 6);
  assert.ok(requests.every(r => r.auth === undefined));
  assert.equal(await (await source.read(GAME_ROOT + 'SAMNMAX.001')).text(), 'blob a1');
  assert.ok(requests.some(r => r.url === 'https://raw.githubusercontent.com/' + REPO + '/spilldata/game/SAMNMAX.001'));
  assert.ok(!requests.some(r => r.url.includes('/git/blobs/')));
});

test('a key GitHub does not accept gives an error the page can show', async () => {
  for (const status of [401, 404]) {
    const source = new RemoteSource(memoryLibrary(), 'BAD', github([], status));
    await assert.rejects(source.list(), error => error instanceof ApiError && error.status === status);
  }
});

test('with the private branches, game paths never go to the site', async () => {
  const requests = [];
  const source = new RemoteSource(memoryLibrary(), 'KEY', github(requests));
  const rows = await source.list();
  const base = new URL('https://example.github.io/Sam-Max-HD-Web/');
  const site = [];
  const fetch = privateFetch(source, makeIndexes(rows), base, async url => { site.push(String(url)); return new Response('x'); });
  assert.equal(await (await fetch(GAME_ROOT + 'SAMNMAX.000')).text(), 'blob a0');
  assert.equal((await fetch(GAME_ROOT + 'MONSTER.SOU')).status, 404);
  assert.equal((await fetch(MOD_ROOT + 'rooms/room023.png')).status, 404);
  assert.deepEqual(site, []);
});

test('the speech in parts becomes one file, read in order; SAMNMAX.000 and .001 stay two files', async () => {
  const parts = [
    {path: 'game/SAMNMAX.000', type: 'blob', sha: 'a0', size: 5},
    {path: 'game/SAMNMAX.001', type: 'blob', sha: 'a1', size: 7},
    {path: 'game/MONSTER.SOU.002', type: 'blob', sha: 'm2', size: 3},
    {path: 'game/MONSTER.SOU.001', type: 'blob', sha: 'm1', size: 4}
  ];
  const rows = treeRows(parts, 'game/', 'game');
  assert.deepEqual(rows.map(row => row.path), [GAME_ROOT + 'SAMNMAX.000', GAME_ROOT + 'SAMNMAX.001', GAME_ROOT + 'MONSTER.SOU']);
  assert.deepEqual(rows.slice(0, 2), [
    {path: GAME_ROOT + 'SAMNMAX.000', size: 5, sha: 'a0'},
    {path: GAME_ROOT + 'SAMNMAX.001', size: 7, sha: 'a1'}]);
  const speech = rows.find(row => row.path === GAME_ROOT + 'MONSTER.SOU');
  assert.equal(speech.size, 7);
  assert.deepEqual(speech.parts, [{sha: 'm1', size: 4}, {sha: 'm2', size: 3}]);
  assert.deepEqual([...blobIds(rows)].sort(), ['a0', 'a1', 'm1', 'm2']);

  const library = memoryLibrary();
  const source = new RemoteSource(library, 'KEY', async url => {
    const sha = new URL(url).pathname.split('/').at(-1);
    return new Response({m1: 'ABCD', m2: 'EFG'}[sha]);
  });
  source.rows = new Map(rows.map(row => [row.path, row]));
  assert.equal(await (await source.read(GAME_ROOT + 'MONSTER.SOU')).text(), 'ABCDEFG');
  assert.deepEqual([...library.blobs.keys()].sort(), ['m1', 'm2']);
});

test('a lost connection is tried again until the file comes', async () => {
  let calls = 0;
  const waits = [];
  const source = new RemoteSource(memoryLibrary(), 'KEY', async () => {
    calls++;
    if (calls === 1) throw new TypeError('Failed to fetch');
    if (calls === 2) return new Response('x', {status: 502});
    if (calls === 3) return new Response('kort');  // body cut off
    return new Response('hele filen');
  }, {waiting: s => waits.push(s), sleep: async () => {}});
  source.rows = new Map([[GAME_ROOT + 'MT32_PCM.ROM', {path: GAME_ROOT + 'MT32_PCM.ROM', size: 10, sha: 'p1'}]]);
  assert.equal(await (await source.read(GAME_ROOT + 'MT32_PCM.ROM')).text(), 'hele filen');
  assert.equal(calls, 4);
  assert.deepEqual(waits, [1, 2, 4]);

  // A key GitHub rejects is not tried again
  let rejected = 0;
  const bad = new RemoteSource(memoryLibrary(), 'BAD', async () => { rejected++; return new Response('', {status: 401}); }, {sleep: async () => {}});
  bad.rows = source.rows;
  await assert.rejects(bad.read(GAME_ROOT + 'MT32_PCM.ROM'), error => error.status === 401);
  assert.equal(rejected, 1);
});

test('the HD pack is fetched in the background, figure cels first, each blob once', async () => {
  const requests = [];
  const library = memoryLibrary();
  const source = new RemoteSource(library, null, github(requests));
  const rows = await source.list();
  const listed = requests.length;
  // The game asks for a file while the background fetch has it on its way
  const mod = rows.filter(r => r.path.startsWith(MOD_ROOT));
  const [count] = await Promise.all([prefetch(source, rows), source.read(mod[0].path)]);
  assert.equal(count, mod.length);
  const fetched = requests.slice(listed).map(r => decodeURIComponent(new URL(r.url).pathname));
  // Only the HD pack, each file once, and the game files are left to the game
  assert.equal(fetched.length, mod.length);
  assert.equal(new Set(fetched).size, fetched.length);
  assert.ok(fetched.every(p => p.includes('/hd-mod/')));
  const kinds = fetched.map(p => /\/costumes\//.test(p) ? 0 : /\/objects\//.test(p) ? 1 : /\/rooms\//.test(p) ? 2 : 3);
  assert.deepEqual(kinds, [...kinds].sort((a, b) => a - b));
  // A second time everything is in the browser
  assert.equal(await prefetch(source, rows), mod.length);
  assert.equal(requests.length, listed + mod.length);
});
