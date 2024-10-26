cd "D:\code\Python\pyinstaller_demo\>"

set PACKAGE_NAME=py_installer_test

RD /S /Q "build"
RD /S /Q "dist"
del %PACKAGE_NAME%.spec

call "venv\Scripts\activate" && pyinstaller ^
--name %PACKAGE_NAME% ^
--noconsole ^
--add-data "tool\my_module\src\test.txt;tool\my_module\src\." ^
"tool\__main__.py"

.\dist\py_installer_test\py_installer_test.exe
