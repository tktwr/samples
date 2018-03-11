@echo off
rem sample batch file

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
