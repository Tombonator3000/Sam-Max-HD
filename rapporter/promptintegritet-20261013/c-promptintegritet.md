# Read-only revisjon av genereringsprompter

Lest 333 JSON-filer. 130 eksplisitte hashreferanser, 64 unike promptfil/forventet-SHA-par. Status: {'OK': 47, 'EOF_AVVIK_BEVIST': 17}.

Inventaret omfatter 306 rapportpromptfiler; 242 mangler en funnet eksplisitt prompt-SHA i de undersøkte manifest-/provenienspostene. Disse er ikke erklært historisk byteverifisert. Generelle sha256-felt som gjelder råbilder/resultater er uttrykkelig utelatt fra promptkontrollen.

Ingen promptfiler, manifest, beskyttede jobbkilder eller Git er endret. Ingen råbilder er lest. Beskyttede jobber/*/prompt.txt er utelatt fra reparasjonsanalysen.

## Beviste avvik

| Fil | Aktuell / opprinnelig lengde | Mekanisk forskjell |
|---|---|---|
| rapporter/bestilling020-20261013/rom086-prompt1.txt | 3164 / 3163 | suffix hex `0a` → ``; EOF_AVVIK_BEVIST |
| rapporter/bestilling020-20261013/obj839_01-prompt1.txt | 3227 / 3226 | suffix hex `0a` → ``; EOF_AVVIK_BEVIST |
| rapporter/bestilling020-20261013/obj839_01-prompt2.txt | 3655 / 3654 | suffix hex `0a` → ``; EOF_AVVIK_BEVIST |
| rapporter/bestilling020-20261013/rom087-prompt1.txt | 3121 / 3120 | suffix hex `0a` → ``; EOF_AVVIK_BEVIST |
| rapporter/bestilling020-20261013/rom088-prompt1.txt | 3196 / 3195 | suffix hex `0a` → ``; EOF_AVVIK_BEVIST |
| rapporter/bestilling021-20261013/obj995_01-prompt1.txt | 3177 / 3176 | suffix hex `0a` → ``; EOF_AVVIK_BEVIST |
| rapporter/bestilling021-20261013/obj995_01-prompt2.txt | 3620 / 3619 | suffix hex `0a` → ``; EOF_AVVIK_BEVIST |
| rapporter/bestilling021-20261013/obj996_01-prompt1.txt | 3069 / 3068 | suffix hex `0a` → ``; EOF_AVVIK_BEVIST |
| rapporter/bestilling021-20261013/obj996_01-prompt2.txt | 3707 / 3706 | suffix hex `0a` → ``; EOF_AVVIK_BEVIST |
| rapporter/bestilling021-20261013/lag002_01-prompt1.txt | 4026 / 4025 | suffix hex `0a` → ``; EOF_AVVIK_BEVIST |
| rapporter/bestilling022-20261013/lag007_02-prompt1.txt | 8100 / 8099 | suffix hex `0a` → ``; EOF_AVVIK_BEVIST |
| rapporter/bestilling022-20261013/lag007_02-prompt-tv.txt | 9453 / 9452 | suffix hex `0a` → ``; EOF_AVVIK_BEVIST |
| rapporter/bestilling022-20261013/lag007_01-prompt1.txt | 8079 / 8078 | suffix hex `0a` → ``; EOF_AVVIK_BEVIST |
| rapporter/bestilling022-20261013/lag007_01-prompt2.txt | 8699 / 8698 | suffix hex `0a` → ``; EOF_AVVIK_BEVIST |
| rapporter/bestilling022-20261013/lag007_01-prompt-tv.txt | 8873 / 8872 | suffix hex `0a` → ``; EOF_AVVIK_BEVIST |
| rapporter/bestilling022-20261013/lag007_01-prompt-tv2.txt | 9233 / 9232 | suffix hex `0a` → ``; EOF_AVVIK_BEVIST |
| rapporter/bestilling022-20261013/lag007_01-prompt-tv3.txt | 9206 / 9205 | suffix hex `0a` → ``; EOF_AVVIK_BEVIST |

Alle 17 avvik som her er bevist kan rekonstrueres ved å fjerne nøyaktig ett avsluttende LF (0a). Ingen endring inne i promptteksten er nødvendig. Dette gjelder fem promptfiler fra bestilling20, fem fra21 og sju fra22. Samme eldre promptreferanser forekommer også i senere gjenbruksmanifest; JSON viser alle referansesteder.

De rekonstruerte bytes matcher nøyaktig den lagrede SHA-256. Dette beviser hvilke filbytes manifestet refererer til, men ikke i seg selv verktøyets eksakte mottatte prompt eller hvem som senere endret filen. Root sin opplysning om EOF-normalisering er konsistent med funnet. Ingen uavklart avvik finnes blant de eksplisitte prompt/hash-parene i denne gjennomgangen.

Root eier eventuell mekanisk reparasjon. Sjekk aktuell filhash mot aktuell_sha256 før endring, fjern bare det påviste avsluttende LF og verifiser mot forventet_sha256. Ikke oppdater historisk forventet SHA for å skjule et avvik. Ingen beskyttet jobbprompt skal røres. Inventarfiler uten historisk prompt-SHA må ikke repareres ved antakelse.

## Konkrete feltkoblinger og rettet foreløpig analyse

Den første interne brede koblingen ga 94 tilsynelatende «uavklarte» par fordi den også brukte et generelt sha256-felt ved siden av prompt-stien. Den koblingen var feil og er fjernet før sluttføring. Ingen av disse 94 er et påvist promptavvik. Eksempler:

- `rapporter/bestilling002-20261013/b-leveranser.json`, `$.leveranser[0].prompt`: peker på `rom003-prompt.txt`, men søskenfeltet `sha256=6a536f0a531d04ee9f00d5b71bd1567d5b4a7464823795fb5c3f0eaf598f2377` gjelder `resultat=jobber/rom003/resultat.png`. Raden inneholder ingen eksplisitt prompt-SHA.
- `rapporter/bestilling011-20261013/c-leveranser.json`, `$.leveranser[0].raw[0].prompt`: peker på `rom047-prompt-1.txt`, men `sha256=71b29b5a3ada863d51c9643400fa154049c82d2aa8b3574db669b56812fc89a3` gjelder råbildefilen i søskenfeltet `fil=rapporter/bestilling011-20261013/rom047-raa-1.png`. Heller ikke denne raden har egen prompt-SHA.

Sikre koblinger i sluttkontrollen er eksplisitt `prompt` sammen med `prompt_sha256`/`sha256_prompt`, eller en selvstendig filpost som selv navngir promptfilen og dens SHA. Generiske leveranse-/råbilde-SHA brukes aldri som prompt-SHA. Beskyttede originaljobbprompter er ikke brukt som hashgrunnlag for utvidede genereringsprompter.

Sluttrapporten er låst for roots mekaniske reparasjon: 64 unike eksplisitte prompt/hash-par, 47 OK og 17 beviste ekstra-LF-avvik, ingen reelle uavklarte par. Ingen ny revisjonskjøring foretas mens root reparerer uten samordning.
