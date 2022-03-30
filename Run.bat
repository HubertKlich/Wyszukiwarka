@ECHO OFF
echo Odpalanie wyszukiwarki:
:loop
set argument=
echo Jakie slowo chcesz wyszukac?
set /P argument=
if "%argument%" EQU "" goto exit
python3 Wyszukiwarka.py %argument%
if "%argument%" NEQ "" goto loop
:exit
PAUSE