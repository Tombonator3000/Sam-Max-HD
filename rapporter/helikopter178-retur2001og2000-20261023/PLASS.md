# Diskplass og filstørrelser

Tom spør om ca. 300 GB grafikk 23. oktober 2026. Målt nå: prosjektet viser 350 GiB, hvorav out viser 331 GiB. Selve mods/gpt er 527 MiB, figurjobbene 859 MiB og hele arbeidsbordet 7,3 GiB. Bildeverktøyets generated_images viser 1,7 GiB totalt.

Out inneholder 6 829 701 PNG med samlet logisk størrelse 215,19 GiB, ZIP/AppImage 57,74 GiB, lokale publiseringsrepoer 17,23 GiB og TAR 14,90 GiB. Dette er hovedsakelig gjentatte komplette mod-, pakke- og testutgaver. Btrfs filesystem du oppgir Total 313,45 GiB, Exclusive 208,51 GiB og Set shared 26,44 GiB. Reflink-kopier deler blokker, så du-tallet er ikke et løfte om frigjørbar plass. Disken har 114 GiB ledig.

Tapsfri PNG-test er utført på syv separate kopier. Eksakte RGBA-piksler og alfa er identiske etterpå. To råbilder sparer 17,9 og 21,0 prosent. To ferdige nativefiler sparer 2,2 og 2,9 prosent, et delark 1,4 prosent, et motorbilde 4,1 prosent og Sam-ankeret 1,5 prosent. Dette lille utvalget gir ingen sikker samlet gevinst for alle bilder. Originalene er bevart.

Anbefalt rekkefølge: Kartlegg og rydd ferdigkontrollerte arbeidskopier, gamle lokale pakkenedlastinger, avpakkede pakker, TAR og lokale publiseringsrepoer etter at nødvendige råbilder, faktiske prompter, resultater, notater, testbevis og sjekksummer er sikret på gpt-arbeid og publiserte filer er bekreftet på hd-mod. Behold gjeldende mod og nyeste faktiske Linux-/Windows-pakke. Deretter reduseres arbeidsflytens antall komplette kopier og gamle testbilder. Tapsfri PNG-optimalisering er et tillegg; den største gevinsten ligger i de gjentatte arbeidsutgavene. Publiserte PNG-hash og beskyttede input skal fortsatt bevares.

Bare disklesing og komprimering av egne testkopier er utført. Ingen ryddejobb eller sletting er startet. Ryddevalg må følge filbevis og eierskap, ikke et bredt slett-alt-mønster i out.
