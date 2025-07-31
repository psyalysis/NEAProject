@echo off
setlocal

:: ======== CONFIGURATION ==========
:: Change this to your project folder
set PROJECT_PATH=C:\Users\DREAD\Desktop\NEAProject\Gyroskate

:: Change to your GitHub repo URL (HTTPS or SSH)
set REPO_URL=https://github.com/psyalysis/NEAProject

:: ======== SCRIPT LOGIC ===========
echo.
echo Navigating to project folder...
cd /d "%PROJECT_PATH%"

echo.
echo Initializing git...
git init

echo.
echo Adding files...
git add .

echo.
echo Creating initial commit...
git commit -m "Initial commit"

echo.
echo Adding remote origin...
git remote add origin %REPO_URL%

echo.
echo Setting main branch...
git branch -M main

echo.
echo Pushing to GitHub...
git push -u origin main

echo.
echo Upload complete!
pause
