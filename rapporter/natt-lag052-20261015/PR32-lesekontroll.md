# Lesekontroll av PR 32

Dato: 15. oktober 2026. Kontrollert lokal Git-referanse origin/codex/hd-masker-inventory på 930ad41d, med motorretting aeef1572. Ingen henting, bygging, endring eller fletting utført. CI-status er oppgitt av Tom, ikke hentet på nytt her.

Jeg leste patchforskjellen mot lokal origin/main og Claudes docs/KONTROLL-PR32.md i prosjektets hovedarbeidstre.

## Konkret funn

Claudes bufferfunn bekreftes ved kodelesing. noteObject og blastSlot bruker samme nøkkel i _objectImages. blastSlot laster _hd.png med pad=true. loadImage beregner softEdge bare når pad=false. Ved et senere noteObject-kall med samme objekt og tilstand hoppes innlastingen over, og dermed også den uttrykkelige softEdge=true-tilordningen. drawSoftObjectEdges tar bare med bilder med softEdge. Dersom samme ressurs først går gjennom blast og deretter gjennom romobjektbanen i samme rom, kan alfakanten derfor bli behandlet feil. Jeg har ikke påvist at denne kallrekkefølgen oppstår i spillet. Dette er et eksisterende konkret kodefunn, ingen ny motorretting er laget.

Kilde: engine/patches/0001-dighd-hd-grafikk.patch i referansen ovenfor, patchlinjer 1235, 1321, 1436 og 1682. Tallene gjelder akkurat denne revisjonen.

## Det som ser riktig ut ved lesing

beginClassicCel nullstiller _recordSlot før den velger presis eller eldre bane. Både noteObject og blastSlot begrenser _drawn til 255 elementer. Det nye active-feltet på 256 elementer overskrides dermed ikke av disse innsettingsveiene. objectGain bruker _palVersion som bufferstempel og regner ut faktorene ved første bruk.

## Oppfølging

Claude bør avklare eller rette den delte buffertilstanden før fletting. Inventaret i rom 93 og bilens nedtoning i rom 9 er fortsatt oppførte spilltester. Ingen skjerm- eller lydtesting er gjort her. PR 32 er ikke duplisert eller flettet.
