echo "Hello World"
goto namelong
:wait
echo %filenamelong64% | base64 -d
rm flnm64.txt
::timeout 1
goto namelong
:name
set filetime=%time%
echo %filetime%
::if %filetime%==%time% (goto photo) else (goto fail)
goto photo
:namelong
echo %username%%time% | base64> flnm64.txt
type flnm64.txt
set /p filenamelong64=<flnm64.txt
echo %filenamelong64%
goto photo
:name64
echo %time% | base64> b64.txt
type b64.txt
set /p filetime64=<b64.txt
goto photo
:photo
wget.exe http://127.0.0.1:8080/photoaf.jpg
mv photoaf.jpg %filenamelong64%.jpg
goto uploadphoto
:uploadphoto
gdrive-windows-x64.exe upload -p xxxxxxxxxxx "%filenamelong64%.jpg"
goto wait
:fail
echo fail
pause
exit
:delall
echo "Delete All Photos"
pause
rm -rf "*.jpg"
pause
