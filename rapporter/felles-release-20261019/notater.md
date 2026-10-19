Begge pakkene har 1546 native HD-figurruter, med de 160 nye rutene som er laget siden fellespakken fra 18. oktober. Sam i strikk, Max på kjøkkenet og de nye VR-rutene er med. Grafikken er fortsatt under arbeid; resten vises som originalen eller glattes av motoren.

- [Linux: SamMaxHD-x86_64.AppImage](https://github.com/Tombonator3000/Sam-Max-HD/releases/download/sam-max-hd-2026-10-19/SamMaxHD-x86_64.AppImage)
- [Windows: SamMaxHD-Windows.zip](https://github.com/Tombonator3000/Sam-Max-HD/releases/download/sam-max-hd-2026-10-19/SamMaxHD-Windows.zip)

Linux: gjør AppImage-filen kjørbar og start den. Mangler FUSE, bruk `./SamMaxHD-x86_64.AppImage --appimage-extract-and-run`. Windows: pakk ut hele ZIP-filen og start «Sam og Max HD.bat». Spillet, talen, musikken og HD-modden følger med. F5 åpner menyen, Ctrl+H bytter mellom HD og originalgrafikk, Alt+Enter bytter vindu/fullskjerm.

Begge pakker er bygget fra main 73b63a9b2b7af18fc045ac2431db7b7b1f2f8339 og hd-mod d31c30f269ed7b0b8746b5b1dfb5c50551cc900d. Ingen motor-/pipeline-/verktøyendring siden forrige fellespakke. Alle 19 787 runtime moddfiler er byteidentiske i begge nedlastingene og med publisert modd; bare README.md utelates av pakkeskriptene.

Linux-bygg 39286953973 består oppstart og Debian 12. Windows-bygg 39286957890 består automatisert oppstart med HD og MT-32. Begge er grønne. Den nedlastede Linux-pakken har i tillegg bestått elleve lokale motorprøver: inventar, akvarium, cafeteriarør og alle 160 nye figurruter observert tegnet. 417 skjermbufferkontroller fra figurstart uten avvik, ni hele prøvebilder sett. Seks kjente frame 36-avvik før testfiguren er dokumentert. Prøvene bruker pakkens uendrede motor, spill og modd, med isolerte innstillinger og kopierte saves.

Dette er ikke full naturlig gjennomspilling, interaktiv Windows-test eller en ny nettleserprøve. Tidligere bakgrunns-/kantrester og stilreturer står fortsatt åpne. Fire VR-ark mangler etter et bildeverktøyavslag og er ikke telt som ferdige. [Rapport og kontrollbilder](https://github.com/Tombonator3000/Sam-Max-HD/blob/gpt-arbeid/rapporter/felles-release-20261019/RAPPORT.md).

SHA-256:

```text
f2ff67f6b016dd7f34aef3cb2c9ac9cfe612effb6d57ddb9e3f7762dfc8792ea  SamMaxHD-x86_64.AppImage
f89b04065969c2c723368eb643c46ce9d97c689cd12aea3a23a5538fde51b685  SamMaxHD-Windows.zip
```

Spillet og grafikken tilhører Disney/Lucasfilm.
