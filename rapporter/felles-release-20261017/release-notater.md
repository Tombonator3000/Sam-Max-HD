Sam & Max HD for Linux og Windows, 17. oktober 2026. Begge pakkene har samme motor og hele den publiserte HD-modden med 1290 native figurruter, 195 flere enn fellespakken fra 16. oktober. Den nye inventory-knappen, flere Sam-animasjoner, Gator Golf, Sam opp ned og den rettede munndelen er med.

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

Grafikken er under arbeid: modden har 76 rom, 959 objektbilder og 1290 native figurruter. 118 av 1758 figurark har resultat; 1640 mangler, i tillegg til returer og stilgodkjenning. Originalbasert visning brukes der nytegning mangler. Bakgrunnsrester og enkelte animasjonsforløp gjenstår. Rute costume204_286 er kontrollert som PNG, men ikke observert i motorprøvene. De siste arkene har Codex-kontroll, men har ikke fått separat Claude-kontroll eller Toms nye stilgodkjenning.

Begge nedlastinger er sjekksumkontrollert. Alle 19 531 moddfiler i hver pakke er byteidentiske med publisert hd-mod og hverandre. Repoets README.md utelates av begge eksisterende pakkeskripter; ingen grafikkfil er utelatt.

Linux består oppstartstest og Debian 12-test. Den nedlastede pakken er kjørt med inventar, akvarium, cafeteriarør og Sam opp ned med blinking og tale: fem prøver, 99 skjermbufferkontroller uten avvik. Bilder fra disse prøvene er visuelt kontrollert. Dette er avgrensede prøver med dummy lyd/skjerm og kopierte lagringer, ikke full gjennomspilling. Z-kantmålingene er ikke null, og prøvene erklærer ikke alle grafikkfeil løst. Windows består automatisert oppstart med HD og MT-32; interaktiv Windows-spilling er ikke kontrollert her.

Byggegrunnlag:

- Kode: `6c181decb140bc73c641b726e9fe0a10b86ddcb3`, med den tidligere flettede PR32-motorrettingen.
- HD-mod: `5212c395ce621dc2d72424affda4e6e19d77a151`.
- Linux-bygg: [39020147979](https://github.com/Tombonator3000/Sam-Max-HD/actions/runs/39020147979).
- Windows-bygg: [39020149118](https://github.com/Tombonator3000/Sam-Max-HD/actions/runs/39020149118).

SHA-256:

```text
2c1b370347b6d81b084e824b9d3d9b0166265ee54df7b376fd1ec2d0429fe463  SamMaxHD-x86_64.AppImage
11edfff532a488ddcf0175871dbd4a7004acfe6260d3da9d4fbc8280acc8341c  SamMaxHD-Windows.zip
```

Sam & Max Hit the Road og grafikken tilhører Disney/Lucasfilm. Motoren er ScummVM (GPL); lisensfiler følger pakkene.
