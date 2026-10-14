@echo off
rem Sam & Max HD: starter spillet rett, med HD-grafikk, musikk og tale.
rem Innstillinger og lagrede spill: %APPDATA%\SamMaxHD
setlocal
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
start "" "%HERE%scummvm.exe" --config="%CONF%\scummvm.ini" --path="%HERE%game" --savepath="%CONF%\saves" --themepath="%HERE%." --extrapath="%HERE%." %* samnmax
