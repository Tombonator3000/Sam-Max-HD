# Bestilling 9 gruppe B kilde-QA

Tre jobber levert fra to fullscene-genereringer, ett forsøk per rom. Innebygd imagegen, eksakt bildemodell ikke eksponert. Godkjent kontorpilot brukt bare som stilanker. Alle fire originale delreferanser sett før generering; originalprompter ordrett med kildeføring bevart.

Rom037: umulig trapp, deformert klokke uten normale tall, avklipt 8-ball, flygel, små dører, ståspeil og dets store grønne skygge er bevart. Lilla felt på gulvet og mørk gardinåpning er tomme. Ingen personer eller retting av tyngderetninger. Fine klokkeformer og vegg-/plankepensling er tolket, ikke dokumentert identiske med enkeltpiksler.

Rom038: tre røde magneter med grålilla ender og kildeegne beslag/spaker. Høyre del inkludert fra start. Den lille blå spaken ved rød midtblokk ble særskilt sammenlignet i rom038-detalj-original.png og rom038-detalj-hd.png; den finnes i originalen. Ingen N/S, gnister eller feltlinjer. Hvit lysåpning og svarte hulrom beholdt. Detaljert overflateskyggelegging er HD-tolkning.

Begge fullmastere er 1920×800, avledet med global normalisering fra råbildenes fullcanvas, deretter klipp. Deloffset 0/384 og overlapp 1152×800 er byte-identisk. Ingen lokal warp eller originalpikselmaskering. Rom038 del2 ligger bare som fremtidig kontrollbilde i rapportmappen og skal leveres i bestilling10 fra samme master. Manifestet låser masterSHA og fremtidig delSHA.

Uendret check_picture fra sjekk_leveranse.py kjørt med respektive originaljobbmetadata: rom037 del1 OK0.06/0.42/0.96, del2 OK0.06/0.61/0.95; rom038 del1 OK0.08/0.84/0.97 og fremtidig del2 OK0.07/0.37/0.97. Alle 16 beskyttede kilder for disse fire delene er kontrollert uendret mot ordinær og ekstra kildehashliste. Råforsøk, prompter, fullkilder og oppskrift bevart.

Runtime, integrasjon, palettsyklus og animert samspill er ikke testet. Ny individuell brukergodkjenning=false. Teknisk OK gjør ikke disse nye bildene til godkjente stilankere.
