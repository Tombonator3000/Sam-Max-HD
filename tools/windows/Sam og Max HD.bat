@echo off
rem Sam & Max HD: starter spillet rett, med HD-grafikk, musikk og tale.
rem Innstillinger og lagrede spill: %APPDATA%\SamMaxHD
setlocal
chcp 65001 >nul
set "HERE=%~dp0"
set "CONF=%APPDATA%\SamMaxHD"
if not exist "%CONF%\saves" mkdir "%CONF%\saves"
if not exist "%CONF%\scummvm.ini" (
	(
		echo [scummvm]
		echo fullscreen=true
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
rem Vinduet blir stående mens spillet går. Stopper spillet med en feil, står meldingen og
rem loggen her (%CONF%\scummvm.log).
"%HERE%scummvm.exe" --config="%CONF%\scummvm.ini" --logfile="%CONF%\scummvm.log" --path="%HERE%game" --savepath="%CONF%\saves" --themepath="%HERE%." --extrapath="%HERE%." %* samnmax
if errorlevel 1 (
	echo.
	echo Spillet stoppet med feilkode %errorlevel%. Loggen: %CONF%\scummvm.log
	echo Prøv "Sam og Max HD.bat --gfx-mode=surfacesdl" hvis det står noe om grafikk eller OpenGL.
	pause
)
