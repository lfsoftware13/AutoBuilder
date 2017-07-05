@echo off
set vcvarsall_path="E:\Program Files (x86)\Visual Studio\VC\vcvarsall.bat"
set file_path=%1
set h_path=%2
set file_output=%3

if not exist %file_output% md %file_output%
if not exist %file_path% goto missingpath

set exe_output="%file_output:"=%\Main.exe"
set result_output="%file_output:"=%\result.txt"
set obj_path="%file_output:"=%\Debug\\"

if not exist %obj_path% md %obj_path%

::echo source file path: %file_path%    product path: %result_output%

call %vcvarsall_path%

if exist %result_output% DEL %result_output%

setlocal EnableDelayedExpansion

set count=0
for /f %%i in ('dir "%file_path:"=%\*.cpp" /b') do (
    ::echo %%i
    set /a count=!count!+1
    set file_list=!file_list! "%file_path:"=%\%%i"
)
if %count%==0 goto:missingfile

cl %file_list% /Fe%exe_output% /nologo /EHsc /I%h_path% /Fo"%file_output:"=%\Debug\\"> %result_output% 2>&1

rd /s /q %obj_path%
goto:eof

:missingpath
echo Source path error: %file_path%
goto:eof

:missingfile
echo CPP file not exist: %file_path%
goto:eof