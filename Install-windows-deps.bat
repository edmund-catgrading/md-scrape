@echo off

:: Create a virtual environment (named ".venv")
echo Creating virtual environment...
python -m venv .venv

:: Activate the virtual environment
echo Activating virtual environment...
call .\.venv\Scripts\activate

:: Upgrade pip, install dependencies
echo Installing Python dependencies...
pip install --upgrade pip
pip install playwright beautifulsoup4 markdownify

:: Install the Playwright browsers (Chromium, Firefox, WebKit)
echo Installing Playwright browsers...
python -m playwright install

echo Installation complete!
pause
