call ".\venv\Scripts\activate" && pyinstaller ^
 --onefile ^
 --distpath "..\..\..\compiled\brightness control" ^
 --icon="icon.ico" ^
 --noconsole ^
 --add-data "icon.ico;." ^
 --paths="venv\Lib\site-packages" ^
 --name="Brightness Controller" ^
 "main.py"

del "Brightness Controller.spec"
