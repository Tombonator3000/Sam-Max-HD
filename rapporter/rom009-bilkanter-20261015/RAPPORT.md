# HD-kantfeil på bilen i rom 9

Tom meldte 15. oktober 2026 trappete kanter rundt ting i rommet og sendte [skjermbildet](toms-skjermbilde.png). Det viser bilen utenfor kontoret, objekt 89 tilstand 01. Trappetrinn er tydelige langs tak, frontrute, støtfanger og bilens underside.

## Bekreftet i grafikkfilene

Den native HD-tegningen i `jobber/obj089_01/resultat.png` har glatte konturer. Den publiserte `hd-mod`-filen `objects/obj089_01.png` er 928 x 352 og har bare alfaverdiene 0 og 255. Hele alfakanalen er byteidentisk med originalens 232 x 88 maske skalert 4x med nearest. Kontrollgrunnlag og SHA-256 står i [diagnose.json](diagnose.json).

[Takutsnitt](tak-kontroll.png) viser native tegning ved siden av publisert bil med hard maske over HD-rommet. [Hele sammenligningen](sammenligning.png) viser samme forskjell. Dette er en diagnostisk sammenstilling av eksisterende filer, ikke et forslag til ny tegning eller en ferdig rettelse.

## Bekreftet i gjeldende kode

Undersøkt main `6269b68e6542eb9f4423d5db87feac0aaed8809f` og hd-mod `e3b7a785d679658e9b68dcc23509807d7b3024ec`.

- `pipeline/smhd/gpt.py::_with_alpha` erstatter HD-bildets alfa med originalmasken.
- `pipeline/smhd/upscale.py::upscale_alpha` bruker nearest. Det gir harde blokker på 4 x 4 HD-piksler for hver originalpiksel.
- I `engine/patches/0001-dighd-hd-grafikk.patch` laster `DigHD::noteObject` vanlige romobjekter fra `objNNN_SS.png`. Kildevalget skjer per originalpiksel med originalens synlighet og indeksverdi.
- `DigHD::compose` kopierer bilens HD-farge for valgte originalpikselblokker og setter full alfa. Myk alfa i PNG-en alene endrer derfor ikke romobjektets ytre kildegrense.
- Den myke `_hd.png`-støtten for pekere, blast-objekter og kostymeruter løser ikke automatisk dette for vanlige romobjekter.

Dette er konkret støtte for en feil i behandlingen av romobjektets kant. Vi har ikke kjørt brukerens nettleserbygg eller en ny motoravspilling i denne kontrollen. Skjermbildets eksakte kjørende motorversjon er ikke oppgitt. Lokale fil- og kodefunn må derfor skilles fra en runtimeverifisert rettelse.

## Rettelse som må gjennomføres i import og motor

Bevar eller etabler en korrekt myk HD-kontur for hele romobjektet, og gi romobjekter kompositering som kan bruke denne kanten over riktig underlag. Originalens tilstand, klikkflate og tegnerekkefølge skal fortsatt styre spillet. Ren alfaeksport er utilstrekkelig så lenge motorens kildegrense fortsatt er den harde originalmasken.

Bilens native levering er et malt utsnitt med gaten rundt, ikke allerede en frittstående bil med myk alfa. Den komplette rektangulære leveransen kan derfor ikke bare omdøpes til `_hd.png` og behandles som en ferdig utskåret bil. Kant/underlag må håndteres eksplisitt ved mottak og kompositering. Bevar eksisterende bilmotiv, dimensjoner og plassering.

Kontroller etter rettingen: tak, frontrute og støtfanger ved skjermstørrelsen i Toms bilde; Sam og Max foran/bak bilen; bilen når den skjules eller bytter tilstand; rulling av gaten; skygger og nedtoning; HD/klassisk-bryter. Ingen gammel kant eller veibakgrunn fra objektutsnittet skal bli stående. Kjør motorens eksisterende nearest- og tilstandstester for å kontrollere at spillgeometrien ikke er endret.

## Status

Diagnose bekreftet med filanalyse og visuell sammenligning. Ingen grafikkfiler, spilldata, pipeline eller motorkode endret. Motorrettelse og spilltest gjenstår. Rå skjermbilde, sammenligninger, sjekksummer og [diagnoseskript](diagnose.py.txt) ligger i grafikkgrenen for videre feilretting. Skriptets input kommer fra de oppgitte hd-mod-filene og den native jobben.
