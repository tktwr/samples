@echo off

echo #include ^<string^>

echo namespace A {

for /f %%i in ('git rev-parse --abbrev-ref HEAD') do set GIT_BRANCH=%%i
echo const std::string GIT_BRANCH = "%GIT_BRANCH%";

for /f %%i in ('git rev-parse --short HEAD') do set GIT_COMMIT=%%i
echo const std::string GIT_COMMIT = "%GIT_COMMIT%";

echo }

