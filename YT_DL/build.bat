RD /S /Q "D:\code\Python\YT_DL\build"
RD /S /Q "D:\code\Python\YT_DL\dist"
call "D:\code\Python\YT_DL\venv\Scripts\activate.bat" && pyinstaller --name "YouTube Downloader" --noconsole --icon=".\resources\icon.ico" main.py && xcopy "D:\code\Python\YT_DL\resources\" "D:\code\Python\YT_DL\dist\YouTube Downloader\resources\" /E && mkdir "D:\code\Python\YT_DL\dist\YouTube Downloader\history\"
"D:\code\Python\YT_DL\archive.bat"
