# Prompter og bilderekkefølge

Første forsøk per ark bruker jobbens beskyttede prompt.txt ordrett. Filene er jobber/fig247_10/prompt.txt og jobber/fig116_02 til 04/prompt.txt. Kopier av de faktiske tekstene følger nedenfor. Eksakt bildemodellnavn vises ikke.

For fig247_10 var bildene referanse.png, hovedark/sam.png, hovedark/max.png og tidligere resultat.png. Den konkrete returinstruksen ble lagt etter originalprompten:

RETUR, targeted edit: Image 1 is the pixel original geometry. Images 2 and 3 are approved Sam and Max identity sheets. Image 4 is the existing HD sheet to edit. Change ONLY head and fedora in frames 3 and 4 of image 4. In frame 3 the fedora stretches upward into a narrow pale blue stalk under the raised helmet, with NO brim, and Sam's face is squashed flat with CLOSED eyes as black horizontal lines. Follow the exact original frame 3 shape. Frame 4 has the brim dragged low over the eyes, eyes are narrow black lines, and a small black OPEN mouth below muzzle. Keep all other parts unchanged, including hands, green helmet bands, cables, tie, suit, feet, frame positions and alpha. Preserve frames 1,2,5,6 exactly. Output 1536x1024 RGBA.

Andre forsøk var avgrenset til originalens og den tidligere HD-leveransens to hoder. Originalutsnitt og HD-utsnitt ligger som 247-hoder-original.png og 247-hoder-hd.png. hovedark/sam.png var siste stilreferanse. Presiseringen krevde smal lyseblå hattestilk uten vanlig krone eller synlig brem, flatpresset ansikt med lukkede øyestreker i venstre rute, lav brem med lukkede øyestreker og liten svart åpen munn i høyre rute.

Tredje forsøk fjernet den resterende venstre bremmen og den ekstra svarte streken over nesen. Venstre hode skulle ha nøyaktig to lukkede øyestreker. Høyre hode skulle bevares.

Fjerde forsøk reparerte komposisjonsskjøter i det plasserte hodeutsnittet. Bare synlige skjøter mellom ansikt, ermer og krage skulle tettes. De legitime transparente åpningene mellom hattestilk og hender skulle beholdes. Referanser var det plasserte hodeutsnittet, originalutsnittet og hovedark/sam.png. Returens hatt og ansiktsuttrykk var låst.

For fig116_02, fig116_03 og fig116_04 var bilde én referanse.png, bilde to hovedark/sam.png. Prompten ble brukt uten tillegg.

Ett ekstra delt bildeforsøk rettet alligatorhodet i fig116_02 og fig116_03. Bilde én var alligator-hode-original.png, bilde to hovedark/sam.png. Prompt:

Faithful smooth HD redraw of this ONE tiny alligator head sprite from Sam & Max Hit the Road, facing LEFT, poking above water. The original pixel image determines every shape and color. It has ONE visible eye only: the single black eye with a small gray-white highlight near the rear/right of the low triangular head. The dark front-left patch is a flat shadow, NOT a second eye. Preserve the long low wedge-like snout pointing left, the two low green angular brow/back humps, dark green rear shading, brighter green lower face and thin dark blue water-edge at the bottom. Do not make a round cute frog or an alligator facing camera. Do not add a second eye, teeth, smile, nostrils, legs, texture or ripples. No items or Sam feet. Strong varied clean cartoon ink outlines, simple original green color areas. Only one isolated head, exact original aspect and silhouette, on genuine transparent alpha, no magenta, no backdrop, no numbers. Image 2 is only the approved Sam & Max style for ink and shading.

## Originalprompt fig247_10

Task: faithful HD remaster of a sheet of animation frames from the 1993 adventure game Sam & Max Hit the Road (LucasArts). This is a production asset. Every frame replaces one original frame in the game, at the same size and position, and the frames are played one after another.

Input: the attached image is the original low-resolution sheet enlarged exactly 4x with hard pixel edges. The frames stand apart on a plain flat magenta background (#FF00FF). Around the sheet is a plain gray (#808080) border. The background and the border are only padding.

What the sheet shows: Sam and Max together: Sam, the dog detective (a big brown dog in a light blue-gray suit, white shirt, striped dark blue tie and a blue-gray fedora) and Max, the white rabbit-like creature (long ears, wide toothy grin, no clothes). The description is only a help; the input image decides. On this sheet, row by row from left to right: animation 8, facing right (6 frames). The game mirrors the frames facing right when the character faces left, so there are no frames facing left; do not add any.

Size rule (most important): draw every frame at exactly the size it has in the input, with the same height, the same width and the same proportions of head, body, arms, legs and props. One input pixel is 4 output pixels for every frame on this sheet and on every other sheet of this character, so the character never grows, shrinks or changes shape between frames. On this sheet the frames are from 464 to 464 pixels tall and from 176 to 192 pixels wide in the input (the box around each frame's visible pixels); jobb.json lists every frame's box under ruter (synlig, in original pixels: multiply by 4).

Do:
- Trace every frame at 4x in high resolution, so it looks like the characters of Day of the Tentacle Remastered next to their originals: keep the pose, silhouette and proportions, and turn every cluster of pixels into the shape it shows (glasses, a tie, a shoe). Clean dark anti-aliased outlines with a little variation in weight, flat colors with one shade and a few highlights, the same color for every area as in the input. No dithering, no texture, no gradients, no pixel steps.
- Keep the original design: the same character, the same colors, light direction, shadows and contrast as in the input.
- Make all frames look identical apart from the pose: the same face, eyes, hat, clothes, colors and light in every frame. Any difference between frames flickers in the game.
- Keep the pose and silhouette of every frame, and keep each frame in its place on the sheet, in the same rows and the same order.
- Glowing effects (light, lightning, sparks, fire) are painted as soft glow that fades into transparency.

Do not:
- Do not add, remove, merge, split or redesign frames.
- Do not add anything that is not in the input: no new props, accessories, patterns, logos, text, shadows, floor, numbers, labels, frames or grid lines.
- Do not change colors, clothes or proportions, and do not make heads, hands or eyes bigger than in the input.
- Some frames show only part of the character (a body without a head, a head alone, an arm), because the game draws the parts separately. Paint them as they are and do not complete them.
- Do not let frames touch or overlap each other.
- No photorealism, no modern 3D look, no film grain, no vignette, no watermark, no signature.

Output: one PNG image, exactly 1536 x 1024 pixels, with a fully transparent background (real alpha: no background color and no gray border) and every frame in the same place as in the input. Before delivering, run python3 verktoy/sjekk_leveranse.py jobber/fig247_10/resultat.png and redo the frames it reports as too big, too small, moved or missing. List the delivery with its sha256 in the fremdrift.json of your report and add a rutekart (the box around each frame's drawing, alpha above 128).

If a second image is attached, it is the approved master sheet (hovedark) of this character, or an already approved HD sheet of the same character, or an approved HD picture from the same game. Paint the character exactly as in that image: the same face, hair, clothes, colors and level of detail. Take every pose, size and position from the first image. If a third image is attached, it is the master sheet of the second character on the sheet.


## Originalprompt fig116_02

Task: faithful HD remaster of a sheet of animation frames from the 1993 adventure game Sam & Max Hit the Road (LucasArts). This is a production asset. Every frame replaces one original frame in the game, at the same size and position, and the frames are played one after another.

Input: the attached image is the original low-resolution sheet enlarged exactly 4x with hard pixel edges. The frames stand apart on a plain flat magenta background (#FF00FF). Around the sheet is a plain gray (#808080) border. The background and the border are only padding.

What the sheet shows: Sam, the dog detective (a big brown dog in a light blue-gray suit, white shirt, striped dark blue tie and a blue-gray fedora). The description is only a help; the input image decides. On this sheet, row by row from left to right: start pose, facing right (1 frame). The game mirrors the frames facing right when the character faces left, so there are no frames facing left; do not add any.

Size rule (most important): draw every frame at exactly the size it has in the input, with the same height, the same width and the same proportions of head, body, arms, legs and props. One input pixel is 4 output pixels for every frame on this sheet and on every other sheet of this character, so the character never grows, shrinks or changes shape between frames. The frame on this sheet is 440 x 240 pixels in the input (the box around its visible pixels).

Do:
- Trace every frame at 4x in high resolution, so it looks like the characters of Day of the Tentacle Remastered next to their originals: keep the pose, silhouette and proportions, and turn every cluster of pixels into the shape it shows (glasses, a tie, a shoe). Clean dark anti-aliased outlines with a little variation in weight, flat colors with one shade and a few highlights, the same color for every area as in the input. No dithering, no texture, no gradients, no pixel steps.
- Keep the original design: the same character, the same colors, light direction, shadows and contrast as in the input.
- Make all frames look identical apart from the pose: the same face, eyes, hat, clothes, colors and light in every frame. Any difference between frames flickers in the game.
- Keep the pose and silhouette of every frame, and keep each frame in its place on the sheet, in the same rows and the same order.
- Glowing effects (light, lightning, sparks, fire) are painted as soft glow that fades into transparency.

Do not:
- Do not add, remove, merge, split or redesign frames.
- Do not add anything that is not in the input: no new props, accessories, patterns, logos, text, shadows, floor, numbers, labels, frames or grid lines.
- Do not change colors, clothes or proportions, and do not make heads, hands or eyes bigger than in the input.
- Some frames show only part of the character (a body without a head, a head alone, an arm), because the game draws the parts separately. Paint them as they are and do not complete them.
- Do not let frames touch or overlap each other.
- No photorealism, no modern 3D look, no film grain, no vignette, no watermark, no signature.

Output: one PNG image, exactly 1536 x 1024 pixels, with a fully transparent background (real alpha: no background color and no gray border) and every frame in the same place as in the input. Before delivering, run python3 verktoy/sjekk_leveranse.py jobber/fig116_02/resultat.png and redo the frames it reports as too big, too small, moved or missing. List the delivery with its sha256 in the fremdrift.json of your report and add a rutekart (the box around each frame's drawing, alpha above 128).

If a second image is attached, it is the approved master sheet (hovedark) of this character, or an already approved HD sheet of the same character, or an approved HD picture from the same game. Paint the character exactly as in that image: the same face, hair, clothes, colors and level of detail. Take every pose, size and position from the first image. If a third image is attached, it is the master sheet of the second character on the sheet.


## Originalprompt fig116_03

Task: faithful HD remaster of a sheet of animation frames from the 1993 adventure game Sam & Max Hit the Road (LucasArts). This is a production asset. Every frame replaces one original frame in the game, at the same size and position, and the frames are played one after another.

Input: the attached image is the original low-resolution sheet enlarged exactly 4x with hard pixel edges. The frames stand apart on a plain flat magenta background (#FF00FF). Around the sheet is a plain gray (#808080) border. The background and the border are only padding.

What the sheet shows: Sam, the dog detective (a big brown dog in a light blue-gray suit, white shirt, striped dark blue tie and a blue-gray fedora). The description is only a help; the input image decides. On this sheet, row by row from left to right: animation 7, facing right (9 frames). The game mirrors the frames facing right when the character faces left, so there are no frames facing left; do not add any.

Size rule (most important): draw every frame at exactly the size it has in the input, with the same height, the same width and the same proportions of head, body, arms, legs and props. One input pixel is 4 output pixels for every frame on this sheet and on every other sheet of this character, so the character never grows, shrinks or changes shape between frames. On this sheet the frames are from 228 to 260 pixels tall and from 268 to 440 pixels wide in the input (the box around each frame's visible pixels); jobb.json lists every frame's box under ruter (synlig, in original pixels: multiply by 4).

Do:
- Trace every frame at 4x in high resolution, so it looks like the characters of Day of the Tentacle Remastered next to their originals: keep the pose, silhouette and proportions, and turn every cluster of pixels into the shape it shows (glasses, a tie, a shoe). Clean dark anti-aliased outlines with a little variation in weight, flat colors with one shade and a few highlights, the same color for every area as in the input. No dithering, no texture, no gradients, no pixel steps.
- Keep the original design: the same character, the same colors, light direction, shadows and contrast as in the input.
- Make all frames look identical apart from the pose: the same face, eyes, hat, clothes, colors and light in every frame. Any difference between frames flickers in the game.
- Keep the pose and silhouette of every frame, and keep each frame in its place on the sheet, in the same rows and the same order.
- Glowing effects (light, lightning, sparks, fire) are painted as soft glow that fades into transparency.

Do not:
- Do not add, remove, merge, split or redesign frames.
- Do not add anything that is not in the input: no new props, accessories, patterns, logos, text, shadows, floor, numbers, labels, frames or grid lines.
- Do not change colors, clothes or proportions, and do not make heads, hands or eyes bigger than in the input.
- Some frames show only part of the character (a body without a head, a head alone, an arm), because the game draws the parts separately. Paint them as they are and do not complete them.
- Do not let frames touch or overlap each other.
- No photorealism, no modern 3D look, no film grain, no vignette, no watermark, no signature.

Output: one PNG image, exactly 1536 x 1024 pixels, with a fully transparent background (real alpha: no background color and no gray border) and every frame in the same place as in the input. Before delivering, run python3 verktoy/sjekk_leveranse.py jobber/fig116_03/resultat.png and redo the frames it reports as too big, too small, moved or missing. List the delivery with its sha256 in the fremdrift.json of your report and add a rutekart (the box around each frame's drawing, alpha above 128).

If a second image is attached, it is the approved master sheet (hovedark) of this character, or an already approved HD sheet of the same character, or an approved HD picture from the same game. Paint the character exactly as in that image: the same face, hair, clothes, colors and level of detail. Take every pose, size and position from the first image. If a third image is attached, it is the master sheet of the second character on the sheet.


## Originalprompt fig116_04

Task: faithful HD remaster of a sheet of animation frames from the 1993 adventure game Sam & Max Hit the Road (LucasArts). This is a production asset. Every frame replaces one original frame in the game, at the same size and position, and the frames are played one after another.

Input: the attached image is the original low-resolution sheet enlarged exactly 4x with hard pixel edges. The frames stand apart on a plain flat magenta background (#FF00FF). Around the sheet is a plain gray (#808080) border. The background and the border are only padding.

What the sheet shows: Sam, the dog detective (a big brown dog in a light blue-gray suit, white shirt, striped dark blue tie and a blue-gray fedora). The description is only a help; the input image decides. On this sheet, row by row from left to right: animation 8, facing right (8 frames). The game mirrors the frames facing right when the character faces left, so there are no frames facing left; do not add any.

Size rule (most important): draw every frame at exactly the size it has in the input, with the same height, the same width and the same proportions of head, body, arms, legs and props. One input pixel is 4 output pixels for every frame on this sheet and on every other sheet of this character, so the character never grows, shrinks or changes shape between frames. On this sheet the frames are from 236 to 328 pixels tall and from 284 to 324 pixels wide in the input (the box around each frame's visible pixels); jobb.json lists every frame's box under ruter (synlig, in original pixels: multiply by 4).

Do:
- Trace every frame at 4x in high resolution, so it looks like the characters of Day of the Tentacle Remastered next to their originals: keep the pose, silhouette and proportions, and turn every cluster of pixels into the shape it shows (glasses, a tie, a shoe). Clean dark anti-aliased outlines with a little variation in weight, flat colors with one shade and a few highlights, the same color for every area as in the input. No dithering, no texture, no gradients, no pixel steps.
- Keep the original design: the same character, the same colors, light direction, shadows and contrast as in the input.
- Make all frames look identical apart from the pose: the same face, eyes, hat, clothes, colors and light in every frame. Any difference between frames flickers in the game.
- Keep the pose and silhouette of every frame, and keep each frame in its place on the sheet, in the same rows and the same order.
- Glowing effects (light, lightning, sparks, fire) are painted as soft glow that fades into transparency.

Do not:
- Do not add, remove, merge, split or redesign frames.
- Do not add anything that is not in the input: no new props, accessories, patterns, logos, text, shadows, floor, numbers, labels, frames or grid lines.
- Do not change colors, clothes or proportions, and do not make heads, hands or eyes bigger than in the input.
- Some frames show only part of the character (a body without a head, a head alone, an arm), because the game draws the parts separately. Paint them as they are and do not complete them.
- Do not let frames touch or overlap each other.
- No photorealism, no modern 3D look, no film grain, no vignette, no watermark, no signature.

Output: one PNG image, exactly 1536 x 1024 pixels, with a fully transparent background (real alpha: no background color and no gray border) and every frame in the same place as in the input. Before delivering, run python3 verktoy/sjekk_leveranse.py jobber/fig116_04/resultat.png and redo the frames it reports as too big, too small, moved or missing. List the delivery with its sha256 in the fremdrift.json of your report and add a rutekart (the box around each frame's drawing, alpha above 128).

If a second image is attached, it is the approved master sheet (hovedark) of this character, or an already approved HD sheet of the same character, or an approved HD picture from the same game. Paint the character exactly as in that image: the same face, hair, clothes, colors and level of detail. Take every pose, size and position from the first image. If a third image is attached, it is the master sheet of the second character on the sheet.
