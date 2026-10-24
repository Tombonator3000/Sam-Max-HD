# Plassbruk og kompakte spillerpakker

Spillerpakken inneholder motoren, nødvendige biblioteker, spilldata og den aktive HD-modden. Arbeidsområdet inneholder i tillegg råbilder, feilforsøk, originaluttrekk, motoropptak, byggekopier og Git-historikk. Arbeidsområdets størrelse skal aldri presenteres som spillerens nedlasting eller installasjon.

## Oppløsning og lagringsformat

HD-grafikken beholder 4 ganger originalens oppløsning. Publiserte fargebilder bruker tapsfri WebP med ekte alfa. `_idx.png` og `_mask.png` beholder originale indekser og maskebits. Ingen oppløsning eller kvalitet reduseres av størrelseskontrollen. Originale jobbgrunnlag, råbilder, godkjente stilankere og `resultat.png` beholdes for produksjon i `gpt-arbeid`. De tas ikke med i spillerpakken. Se [WebP](WEBP.md).

## Grenser i pakkebyggingen

Begge pakkeskriptene kjører `tools/kontroller_pakkestorrelse.py` før de lykkes. Pakkebyggingen stopper over 1000 MB nedlasting eller 2000 MB utpakket innhold. Dette er tak som skal hindre utilsiktet vekst, ikke et løfte om sluttstørrelsen på den uferdige HD-utgaven. MB betyr 1 000 000 byte.

Kontrollen stopper også hvis arbeidsmapper som `.git`, `out`, `work`, `jobber` eller `rapporter` lekker inn. ZIP kontrolleres uten utpakking, med både komprimert og utpakket størrelse. AppImage måles sammen med pakkemappen den bygges fra. Rapporten skrives til `storrelse.json` i byggemappen. Grensene er uavhengige av bildeformat og endrer aldri grafikken automatisk.

Eksempel for en nedlastet Windows-pakke:

```sh
python3 tools/kontroller_pakkestorrelse.py SamMaxHD-Windows.zip --rapport storrelse.json
```

Ved utgaven 24. oktober 2026 er Linux-nedlastingen 392 411 640 byte og Windows-nedlastingen 544 532 414 byte. Windows-innholdet utpakket er 659 179 020 byte. Aktiv mod er 368 606 455 byte med 3733 native figurruter. Disse tallene gjelder denne utgaven; resten av HD-produksjonen og kontrollen gjenstår.

## Arbeidsområdet skal ikke vokse for hver bunke

- Bruk én nødvendig komplett modkandidat per aktiv bunke, bygget fra gjeldende publisert mod. Historiske dedupliserte out-mapper er ikke komplette modder.
- Gjenbruk hovedrepoets Git-objektlager. Publiseringsarbeid kan bruke en separat Git-worktree eller indeks. Ikke lag en ny full Git-klon i `out/` for hver publisering.
- Ha én spilldatakilde i `game/`. Testkjøringer peker på den fremfor å kopiere talen.
- Behold én nødvendig kopi av hver gjeldende nedlastingspakke. Kontroller nye nedlastinger som strømmer når selve arkivet ikke skal beholdes.
- Fjern verifiserte arbeidskopier etter bunken. Behold råbilder, unike kilder, godkjente stilankere og relevante kontrollbevis i `gpt-arbeid`.
- Før sletting skal en journal oppgi SHA-festet beholdt kilde eller historisk Git-objekt. Kontroller bytes før sletting. Verken tre eksisterende stasher, aktive worktrees eller upublisert arbeid skal fjernes.

Gamle publiseringskloner kan ha Git-objekter som ikke lenger er nåbare fra en aktiv gren. Sikre disse og refs før klonen ryddes. En delt objektbase skal bevare historikken, ikke bare den siste arbeidsfilen. Gamle motorbilder kan fjernes som duplikater bare når en beholdt identisk kilde er kontrollert og journalført.

Rapporter både logisk prosjektstørrelse og observert ledig diskplass. Btrfs kan dele extents mellom kopier, så summerte filstørrelser er ikke et bevis på like stor fysisk plassgevinst. Ingen generell Git-pruning eller sletting av historikk inngår i oppryddingen.
