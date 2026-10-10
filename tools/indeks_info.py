#!/usr/bin/env python3
"""Leser indeksfilen SAMNMAX.000 fra Sam & Max Hit the Road (SCUMM v6) og skriver ut det viktigste.

Bruk:
    python3 tools/indeks_info.py game/SAMNMAX.000            # oversikt
    python3 tools/indeks_info.py game/SAMNMAX.000 --json     # alt som JSON
    python3 tools/indeks_info.py game/SAMNMAX.000 --rooms    # bare romlisten (CSV; Sam & Max har ingen romnavn)

Skriptet leser filen og endrer ingenting. Det trenger bare standardbiblioteket.
Det leser også DIG.LA0 fra The Dig (v7, ukryptert), som det ble skrevet for.

Format (bekreftet mot ScummVM engines/scumm/resource.cpp ved c9091321):
  Sam & Max: hele filen er kryptert med XOR 0x69 (GF_USE_KEY). Den dekrypteres først.
  Blokker: 4 byte tagg + 4 byte storrelse (big endian, inkludert hodet).
  RNAM:    oppforinger med 1 byte romnummer + 9 byte navn XOR 0xFF, avsluttet med 0 (tom i Sam & Max).
  MAXS:    v6: 15 x uint16 LE (blokkstorrelse 38). v7: 50 byte motorversjon, 50 byte dataversjon, deretter 15 x uint16 LE.
  D*:      kataloger med uint16 LE antall forst, sa romnummer (1 byte) og offset (4 byte) per plass.
"""
import argparse
import hashlib
import json
import struct
import sys

KNOWN = {b"RNAM", b"MAXS", b"DROO", b"DSCR", b"DSOU", b"DCOS", b"DCHR", b"DOBJ", b"AARY", b"ANAM"}
MAXS_FIELDS = [
    "variables", "bit_variables", "unknown", "global_objects", "local_objects",
    "new_names", "verbs", "fl_objects", "inventory", "arrays", "rooms",
    "scripts", "sounds", "charsets", "costumes",
]
MAXS_FIELDS_V6 = [
    "variables", "unknown", "bit_variables", "local_objects", "arrays",
    "unknown2", "verbs", "fl_objects", "inventory", "rooms",
    "scripts", "sounds", "charsets", "costumes", "global_objects",
]
XOR_V6 = 0x69
# Kjente MD5-summer fra ScummVM sin scumm-md5.h (samnmax CD, 9080 byte; dig, 16304 byte)
KNOWN_MD5 = {
    "d917f311a448e3cc7239c31bddb00dd2": "Sam & Max, engelsk CD-utgave",
    "0fb73eddfcf584c02ba097984df131ba": "Sam & Max, tysk CD-utgave",
    "7edd665bbede7ea8b7233f8e650be6f8": "Sam & Max, fransk CD-utgave",
    "0f6f2e716ba896a44e5059bba1de7ca9": "Sam & Max, italiensk CD-utgave",
    "4ba7fb331296c283e73d8f5b2096e551": "Sam & Max, spansk CD-utgave",
    "d8323015ecb8b10bf53474f6e6b0ae33": "The Dig, standardoppforingen i ScummVM",
}


def walk_blocks(data):
    """Gar gjennom blokkene. Hvis en tagg er ukjent, leter den etter neste kjente tagg."""
    pos, blocks = 0, []
    while pos + 8 <= len(data):
        tag = data[pos:pos + 4]
        if tag not in KNOWN:
            nxt = min((i for i in (data.find(t, pos + 1) for t in KNOWN) if i > 0), default=-1)
            if nxt < 0:
                break
            blocks.append(("RESYNC", pos, nxt - pos))
            pos = nxt
            continue
        size = struct.unpack(">I", data[pos + 4:pos + 8])[0]
        if size < 8 or pos + size > len(data):
            # Skadet blokkhode: en størrelse under 8 ville gitt evig løkke, og en for stor
            # ville lest forbi slutten av filen. Lagre resten som ukjent og stopp.
            blocks.append(("SKADET", pos, len(data) - pos))
            break
        blocks.append((tag.decode(), pos, size))
        pos += size
    return blocks


def decrypt(raw):
    """Gir (data, nøkkel). Sam & Max er kryptert med XOR 0x69; The Dig er ukryptert."""
    if raw[:4] in KNOWN:
        return raw, 0
    table = bytes(i ^ XOR_V6 for i in range(256))
    if raw[:4].translate(table) in KNOWN:
        return raw.translate(table), XOR_V6
    return raw, 0


def parse(raw):
    data, key = decrypt(raw)
    out = {"size": len(raw), "md5": hashlib.md5(raw).hexdigest(), "xor": key, "blocks": [], "directories": {}}
    out["md5_match"] = KNOWN_MD5.get(out["md5"], "ukjent (eller filen er endret)")
    for tag, pos, size in walk_blocks(data):
        out["blocks"].append({"tag": tag, "offset": pos, "size": size})
        body = data[pos + 8:pos + size]
        if tag == "RNAM":
            rooms, p = [], 0
            while p < len(body) and body[p] != 0:
                name = bytes(b ^ 0xFF for b in body[p + 1:p + 10]).split(b"\x00")[0].decode("latin1")
                rooms.append({"room": body[p], "name": name})
                p += 10
            out["rooms"] = sorted(rooms, key=lambda r: r["room"])
        elif tag == "MAXS" and size == 38:
            out["scumm"] = 6
            out["maxs"] = dict(zip(MAXS_FIELDS_V6, struct.unpack("<15H", body[:30])))
        elif tag == "MAXS":
            out["scumm"] = 7
            out["engine_version"] = body[:50].split(b"\x00")[0].decode("latin1")
            out["data_version"] = " ".join(body[50:100].replace(b"\x00", b" ").decode("latin1").split())
            out["maxs"] = dict(zip(MAXS_FIELDS, struct.unpack("<15H", body[100:130])))
        elif tag in ("DROO", "DSCR", "DSOU", "DCOS", "DCHR"):
            n = struct.unpack("<H", body[:2])[0]
            rooms = body[2:2 + n]
            offs = struct.unpack(f"<{n}I", body[2 + n:2 + 5 * n]) if len(body) >= 2 + 5 * n else ()
            used = sum(1 for r, o in zip(rooms, offs) if r or o)
            out["directories"][tag] = {"plasser": n, "i_bruk": used}
        elif tag in ("DOBJ", "ANAM"):
            out["directories"][tag] = {"plasser": struct.unpack("<H", body[:2])[0]}
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("indeks", help="SAMNMAX.000 (eller DIG.LA0)")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--rooms", action="store_true")
    args = ap.parse_args()
    with open(args.indeks, "rb") as f:
        info = parse(f.read())
    if args.json:
        json.dump(info, sys.stdout, indent=1, ensure_ascii=False)
        print()
        return
    if args.rooms:
        print("rom,navn")
        for r in info.get("rooms", []):
            print(f"{r['room']},{r['name']}")
        return
    print(f"Fil: {args.indeks}  ({info['size']} byte)")
    print(f"MD5: {info['md5']}  -> {info['md5_match']}")
    print(f"SCUMM:        v{info.get('scumm', '?')}" + (f", XOR 0x{info['xor']:02X}" if info["xor"] else ""))
    if "engine_version" in info:
        print(f"Motorversjon: {info['engine_version']}")
        print(f"Dataversjon:  {info.get('data_version', '?')}")
    for k, v in info.get("maxs", {}).items():
        print(f"  {k:15} {v}")
    print("Kataloger:", ", ".join(f"{k}={v['plasser']}" + (f" ({v['i_bruk']} i bruk)" if "i_bruk" in v else "")
                                  for k, v in info["directories"].items()))
    resync = [b for b in info["blocks"] if b["tag"] in ("RESYNC", "SKADET")]
    if resync:
        print(f"Advarsel: {len(resync)} ukjente omrader i filen. Filen kan vaere skadet.")
    print(f"Navngitte rom: {len(info.get('rooms', []))}")


if __name__ == "__main__":
    main()
