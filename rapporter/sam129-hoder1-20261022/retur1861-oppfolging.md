# Avgrenset oppfølging av 1861

22. oktober 2026. Bevarte 3597-feil, 3589/3596-kontroller og patchens blend- og dumpFrame-steder er lest igjen. dumpFrame sammenligner faktisk deloppdatert skjerm med hel compose. Tegneren multipliserer premultiplisert RGB med c.gain, mens alfadekningen beholdes i blandingen. Dette er kodebeskrivelse, ikke en bekreftet rotårsak til denne returen. Feilpunktene opptrer også der 1861s egen alfa er null; en ren endring i den malte kanten ville derfor ikke bevise riktig overgangshåndtering.

Ingen avgrenset og bekreftet motorretting er klar. 1861 holdes fortsatt utenfor native. Tegning, alfa, 3597-diagnosen og alle gamle resultater er bevart. Ingen kodeendring eller ny motorgodkjenning. Videre retting må isolere overgangens faktiske dirty-områder og komposisjon, og gå via testet PR. Uavhengige 129-hoder produseres videre med uendrede mottaksporter.
