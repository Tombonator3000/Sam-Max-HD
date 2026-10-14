@echo off
rem Sam & Max HD, utviklermodus: hopp til et rom eller last et lagret spill, i vindu.
rem Hoppet setter ikke spillet i vanlig tilstand (figurer og skript kan mangle eller henge).
rem Et lagret spill fra en ekte gjennomspilling er riktig tilstand.
setlocal
chcp 65001 >nul
set "HERE=%~dp0"
set "CONF=%APPDATA%\SamMaxHD"
if not exist "%CONF%\saves" mkdir "%CONF%\saves"
if not exist "%CONF%\scummvm.ini" (
	(
		echo [scummvm]
		echo aspect_ratio=true
		echo subtitles=true
		echo gui_return_to_launcher_at_exit=false
		echo confirm_exit=false
		echo.
		echo [samnmax]
		echo description=Sam ^& Max HD
		echo engineid=scumm
		echo gameid=samnmax
		echo subtitles=true
	) > "%CONF%\scummvm.ini"
)
if exist "%HERE%mod\mod.json" set "DIGHD_MOD=%HERE%mod"

echo Sam ^& Max HD, utviklermodus
echo.
echo   1  Hopp til et rom
echo   2  Last et lagret spill
echo   3  Start vanlig, i vindu
echo.
set /p VALG=Velg 1, 2 eller 3: 
set "EKSTRA="
if "%VALG%"=="1" (
	type "%HERE%rom-liste.txt"
	echo.
	set /p ROM=Romnummer: 
	call set "DIGHD_TEST_ROOM=%%ROM%%"
	set "DIGHD_TEST_AT=60"
)
if "%VALG%"=="2" (
	echo Lagrede spill ligger i %CONF%\saves
	dir /b "%CONF%\saves\samnmax.s*" 2>nul
	echo.
	set /p SLOT=Nummer (for eksempel 3 for samnmax.s03): 
	call set "EKSTRA=--save-slot=%%SLOT%%"
)
rem Ctrl+Shift+H viser gult der HD mangler. ScummVM sin konsoll: Ctrl+Alt+D.
"%HERE%scummvm.exe" --config="%CONF%\scummvm.ini" --logfile="%CONF%\scummvm.log" --path="%HERE%game" --savepath="%CONF%\saves" --themepath="%HERE%." --extrapath="%HERE%." --no-fullscreen %EKSTRA% samnmax
if errorlevel 1 (
	echo.
	echo Spillet stoppet med feilkode %errorlevel%. Loggen: %CONF%\scummvm.log
	pause
)
