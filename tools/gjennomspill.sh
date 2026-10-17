#!/usr/bin/env bash
# Gjennomspillingsagenten: Claude spiller Sam & Max HD uten skjerm i økter, lagrer i hvert område
# og skriver feil i work/gjennomspill/FUNN.md. Instruksen agenten følger: docs/GJENNOMSPILLING.md.
#
#   tools/gjennomspill.sh                   til klokka 08:00
#   tools/gjennomspill.sh --timer 2         i to timer
#   tools/gjennomspill.sh --til 23:00 --okt 30
#   tools/gjennomspill.sh --uten-push       funnene blir bare liggende lokalt
#
# Stopp: touch work/gjennomspill/STOPP (etter økten som går), eller Ctrl+C.
# Etter hver økt legges FUNN.md, FREMDRIFT.md, utsnittene og de lagrede spillene i grenen
# gjennomspilling og pushes. De er fra spillet og skal ikke inn i main.
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"
export PATH="$HOME/.local/bin:$HOME/.local/share/node/bin:$HOME/.npm-global/bin:$PATH"

TIL=08:00 TIMER="" OKT=45 PUSH=1
while [ $# -gt 0 ]; do
	case "$1" in
	--til) TIL="$2"; shift 2 ;;
	--timer) TIMER="$2"; shift 2 ;;
	--okt) OKT="$2"; shift 2 ;;
	--uten-push) PUSH=0; shift ;;
	-h|--help) sed -n '2,13p' "$0"; exit 0 ;;
	*) echo "Ukjent valg: $1"; exit 1 ;;
	esac
done

M="$ROOT/work/gjennomspill"
mkdir -p "$M/lagret" "$M/bilder" "$M/funnbilder" "$M/okter"
rm -f "$M/STOPP"
logg() { echo "- $(date '+%H:%M') $*" | tee -a "$M/LOGG.md"; }

if [ -n "$TIMER" ]; then
	FRIST=$(( $(date +%s) + ${TIMER%.*} * 3600 ))
else
	FRIST=$(date -d "$TIL" +%s)
	[ "$FRIST" -gt "$(date +%s)" ] || FRIST=$(date -d "tomorrow $TIL" +%s)
fi

command -v claude >/dev/null || { echo "Fant ikke claude. Kjør prosjektbibliotekets samarbeid/installer.sh først."; exit 1; }
[ -f game/SAMNMAX.001 ] || tools/hent_spilldata.sh
[ -x engine/scummvm/scummvm ] || engine/build.sh
if ! grep -q DIGHD_STYRING engine/scummvm/scummvm; then
	echo "Motoren mangler styringen (DIGHD_STYRING). Bygger på nytt med patchen ..."
	engine/build.sh
fi
[ -f mods/gpt/mod.json ] || tools/mod_gren.sh hent

# Kopier av modden og motoren: natteskiftet kan bygge ny modd (rm -rf mods/gpt) mens agenten spiller
rm -rf "$M/mod"
cp -al mods/gpt "$M/mod" 2>/dev/null || cp -r mods/gpt "$M/mod"
cp engine/scummvm/scummvm "$M/scummvm"
export STYR_MOTOR="$M/scummvm" STYR_MOD="$M/mod" STYR_MAPPE="$M"

[ -f "$M/FUNN.md" ] || printf '# Funn fra gjennomspillingen\n\nSe docs/GJENNOMSPILLING.md for formatet. Nyeste nederst.\n' > "$M/FUNN.md"
[ -f "$M/FREMDRIFT.md" ] || printf '# Fremdrift\n\nIkke startet. Begynn med tools/styr.py start.\n' > "$M/FREMDRIFT.md"

publiser() {
	[ "$PUSH" = 1 ] || return 0
	local T="$M/gren"
	if [ ! -e "$T/.git" ]; then
		git worktree prune
		if git fetch -q origin "+refs/heads/gjennomspilling:refs/remotes/origin/gjennomspilling" 2>/dev/null; then
			git worktree add -q -B gjennomspilling "$T" origin/gjennomspilling
		else
			git worktree add -q --orphan -b gjennomspilling "$T"
		fi
	fi
	mkdir -p "$T/funnbilder" "$T/lagret"
	cp "$M/FUNN.md" "$M/FREMDRIFT.md" "$T/"
	[ -f "$M/LOGG.md" ] && cp "$M/LOGG.md" "$T/"
	shopt -s nullglob
	local f
	for f in "$M"/funnbilder/*.png; do cp -u "$f" "$T/funnbilder/"; done
	for f in "$M"/lagret/samnmax.s[0-9]*; do cp -u "$f" "$T/lagret/"; done
	shopt -u nullglob
	printf '# Gjennomspilling\n\nFunn fra gjennomspillingsagenten (tools/gjennomspill.sh i main, instruksen i docs/GJENNOMSPILLING.md).\nFUNN.md har feilene, funnbilder/ bevisene (HD, original, gult), lagret/ de lagrede spillene (tools/romtest.sh --lagret).\nSpillet og grafikken tilhører Disney/Lucasfilm.\n' > "$T/README.md"
	git -C "$T" add -A
	if git -C "$T" -c user.name="${GIT_AUTHOR_NAME:-KI-samarbeid}" commit -q -m "Gjennomspilling $(date '+%Y-%m-%d %H:%M')"; then
		if git -C "$T" push -q -u origin gjennomspilling; then
			logg "Funnene er pushet til grenen gjennomspilling."
		else
			logg "Push av gjennomspilling feilet; funnene ligger i $M."
		fi
	fi
}

logg "Starter gjennomspillingen. Stopper $(date -d "@$FRIST" '+%Y-%m-%d %H:%M'). Økter på $OKT minutter."
n=0 tomme=0
while :; do
	na=$(date +%s)
	[ -f "$M/STOPP" ] && { logg "Stoppet etter beskjed."; break; }
	[ $(( FRIST - na )) -gt 600 ] || { logg "Tiden er ute."; break; }
	n=$((n + 1))
	slutt=$(( na + OKT * 60 ))
	[ "$slutt" -le "$FRIST" ] || slutt=$FRIST
	mkdir -p "$M/okter" "$M/lagret" "$M/bilder" "$M/funnbilder"
	ut="$M/okter/$(date '+%Y%m%d_%H%M').txt"
	logg "Økt $n til $(date -d "@$slutt" '+%H:%M')."
	minutter=$(( (slutt - na) / 60 ))
	prompt="Du er gjennomspillingsagenten for Sam & Max HD i $ROOT. Les docs/GJENNOMSPILLING.md og følg den. Les så work/gjennomspill/FREMDRIFT.md og slutten av work/gjennomspill/FUNN.md, og fortsett der forrige økt slapp (er det første økt, start spillet fra begynnelsen). Denne økten varer i $minutter minutter, til $(date -d "@$slutt" '+%H:%M') etter maskinens klokke (kommandoen date). Bruk hele tiden; gi ikke opp før den er ute. Da lagrer du, oppdaterer FREMDRIFT.md, kjører tools/styr.py stopp og skriver SEGMENT FERDIG som siste linje, eller SPILLET FERDIG hvis hele spillet er spilt."
	set +e
	timeout $(( (slutt - na) + 900 )) claude -p --permission-mode auto --output-format text <<<"$prompt" >"$ut" 2>&1
	kode=$?
	set -e
	tools/styr.py stopp >/dev/null 2>&1 || true
	siste=$(grep -v '^[[:space:]]*$' "$ut" | tail -1 || true)
	logg "Økt $n slutt (kode $kode): ${siste:0:160}"
	publiser || true
	case "$siste" in
	*"SPILLET FERDIG"*) logg "Agenten har spilt hele spillet."; break ;;
	esac
	if [ "$kode" -ne 0 ] && [ ! -s "$ut" ]; then
		tomme=$((tomme + 1))
		[ "$tomme" -lt 3 ] || { logg "Tre økter uten svar fra Claude på rad. Stopper."; break; }
		logg "Ingen svar fra Claude (bruksgrense?). Venter 15 minutter."
		sleep 900
	else
		tomme=0
	fi
done
publiser || true
logg "Ferdig. Funn: $M/FUNN.md"
