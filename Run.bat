@ECHO OFF
echo Odpalanie wyszukiwarki:
:loop
set argument=
echo.
echo Jakie slowo chcesz wyszukac? (Jezeli chcesz wyjsc kliknij ENTER)
set /P argument=
cls
if "%argument%" EQU "" goto exit
python3 Wyszukiwarka.py %argument%
if "%argument%" NEQ "" goto loop
:exit
PAUSE