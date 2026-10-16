Sam & Max HD for Linux og Windows, 16. oktober 2026. Begge pakkene bruker samme motor og HD-grafikk, inkludert den flettede motorrettingen fra PR32 og nattens leveranser.

| Maskin | Last ned | Start |
| --- | --- | --- |
| Linux x86_64 | SamMaxHD-x86_64.AppImage | Gjør filen kjørbar og start den |
| Windows x86_64 | SamMaxHD-Windows.zip | Pakk ut hele mappen og start «Sam og Max HD.bat» |

Linux:

```sh
chmod +x SamMaxHD-x86_64.AppImage
./SamMaxHD-x86_64.AppImage
```

Hvis maskinen mangler FUSE: `./SamMaxHD-x86_64.AppImage --appimage-extract-and-run`.

Spill, tale, MT-32-musikk og HD-grafikk er med. Ctrl+H bytter HD/original, F5 åpner spillmenyen og Alt+Enter bytter vindu/fullskjerm. Lagrede spill og innstillinger beholdes i brukerens mappe.

Grafikken er fortsatt under arbeid: modden har 76 rom, 959 objektbilder og 1095 native figurruter. Det som mangler nytegning, bruker originalbasert visning. Bakgrunnsrester og enkelte animasjonsforløp gjenstår.

Begge pakkene er sjekksumkontrollert etter nedlasting. Linux består oppstartstest og Debian 12-test, og inventar, akvarium og cafeteriarør er kjørt i den nedlastede pakken. Windows består automatisert oppstart med HD og MT-32; interaktiv Windows-spilling er ikke kontrollert her.

Byggegrunnlag:

- Kode: `9b5a9197bac68c9559af00b0580adb7022f5d196`.
- HD-mod: `a6c286bdc37b67f11559fb76d038e23da3624158`.
- Linux-bygg: [38886201631](https://github.com/Tombonator3000/Sam-Max-HD/actions/runs/38886201631).
- Windows-bygg: [38866752358](https://github.com/Tombonator3000/Sam-Max-HD/actions/runs/38866752358).

SHA-256:

```text
aac361d35fdd801b31f966c4e4c9abdb51d28c8f439f6527c43bd27d08bf1f18  SamMaxHD-x86_64.AppImage
ed34bc93a22bb3d2b4a1c43941122496c93e1f65ff4f798bebd9d8ff2a5e5425  SamMaxHD-Windows.zip
```

Sam & Max Hit the Road og grafikken tilhører Disney/Lucasfilm. Motoren er ScummVM (GPL); lisensfiler følger pakkene.
