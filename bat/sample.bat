@echo off
rem *memo_bat.app*
rem sample batch file

set BAT_DIR=%~dp0

cd %BAT_DIR%

echo ARGS : %*
echo ARG0 : %0
echo ARG1 : %1
echo DIR  : %~dp0

set num=0
if %num% equ 0 (
  echo 0
) else (
  echo 1
)

set str=A
if "%str%" == "A" (
  echo 0
) else (
  echo 1
)

if not exist tmp_dir (
  mkdir tmp_dir
)

rem loop for files
for %%f in (*.*) do (
  echo %%f
)

rem loop for dirs
for /d %%d in (tmp_dir) do (
  echo %%d
)

pause

