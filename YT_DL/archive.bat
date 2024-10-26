echo on
for /f "tokens=3,2,4 delims=/- " %%x in ("%date%") do set d=%%y%%x%%z
set data=%d%
Echo zipping...
"C:\Program Files\7-Zip\7z.exe" a -tzip "D:\code\Python\YT_DL\dist\YouTube Downloader.zip" "D:\code\Python\YT_DL\dist\YouTube Downloader\"
echo Done!
