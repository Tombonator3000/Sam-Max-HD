Sam & Max HD for Linux og Windows, 18. oktober 2026. Begge pakkene har samme motor og publiserte grafikkpakke med 1386 native figurruter. Det er 96 flere enn fellespakken fra 17. oktober: Sam i strikkhoppsele og sekvensen der han løfter Max og hopper.

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

Spill, tale, MT-32-musikk og HD-grafikk er med. Ctrl+H bytter HD/original, F5 åpner spillmenyen og Alt+Enter bytter vindu/fullskjerm. Lagrede spill og innstillinger ligger i brukerens mappe.

Grafikken er under arbeid. 128 av 1758 figurark har resultat; 1630 mangler, i tillegg til returer og stilgodkjenning. Nytegning mangler fortsatt for mange figurer, og kjente bakgrunnsrester og enkelte animasjonsforløp gjenstår. Costume204_286 er kontrollert som PNG, men ikke observert i motorprøvene. De 96 siste rutene har egenkontroll og teknisk mottak, men har ikke separat Claude-kontroll eller Toms nye stilgodkjenning.

Grafikkprøvene viser alle 96 nye ruter og 340 skjermbufferkontroller fra figurstart uten avvik. Kunstig rom61-hopp har et kjent avvik på 160 piksler ved frame 36 før testfiguren settes inn; samme avvik finnes med forrige publiserte grafikkpakke. Denne grafikkrunden retter ikke dette. Tvunget avspilling, ikke full naturlig gjennomspilling. Z-kantmålingene er ikke null.

Byggegrunnlag:

- Kode: `ed7a1face8286a3737c8b63d6876572d7b3c5ebd`. Ingen ny motorkode siden forrige fellespakke; senere endringer gjelder dokumentasjon.
- HD-mod: `f7a3f275d62de5327d5a0d08153dfbc17ffdb9c9`.
- Linux-bygg: [39124246281](https://github.com/Tombonator3000/Sam-Max-HD/actions/runs/39124246281).
- Windows-bygg: [39124248206](https://github.com/Tombonator3000/Sam-Max-HD/actions/runs/39124248206).
- Grafikk, prompter og kontroller: [strikkhopp-20261018](https://github.com/Tombonator3000/Sam-Max-HD/tree/gpt-arbeid/rapporter/strikkhopp-20261018).

Spillet og grafikken tilhører Disney/Lucasfilm.

Begge nedlastinger er sjekksumkontrollert. Alle 19 627 runtime moddfiler i hver pakke er byteidentiske med publisert hd-mod og hverandre. Bare repoets README.md utelates av de eksisterende pakkeskriptene; alle grafikkfilene er med.

Linux har bestått oppstart og Debian 12. Den nedlastede, uendrede produksjonsmotoren er også kjørt lokalt i ni avgrensede prøver: inventar, akvarium, cafeteriarør, Sam opp ned med blinking/tale, Sam i sele med ståing/tale og to strikkhoppprøver. Alle 44 ruter for Sam som løfter Max og hopper er observert i denne nedlastingen. Første automatiske syklus nådde bare forberedelsen; hele hoppanimasjonen er derfor prøvd særskilt.

404 skjermbufferkontroller i pakkeprøvene. De fire rom61-prøvene har det kjente avviket 160 ved frame 36 før figurstart; 350 kontroller fra figurstart er uten avvik. Alle øvrige kontrollmålinger er null. Åtte utvalgte prøvebilder er visuelt kontrollert. Kopierte saves og isolerte HOME-/XDG-mapper, dummy lyd/skjerm og null musikk, ikke full naturlig gjennomspilling. Windows består automatisert oppstart med HD og MT-32; interaktiv Windows-spilling er ikke kontrollert her.

Sjekksummer:

- SamMaxHD-x86_64.AppImage: `8eee97117a0d94e65ec9171b7a58eefa9775af74d78e23f0536775747adb0b51`.
- SamMaxHD-Windows.zip: `926d779d523a9df367f0b864f3b6ffa422cabbaadfc1b78cca3a949dece311d8`.
