#!/usr/bin/env bash

echo "Creating virtual environment..."
python3 -m venv .venv

echo "Activating virtual environment..."
source .venv/bin/activate

echo "Upgrading pip and installing Python dependencies..."
python -m pip install --upgrade pip
python -m pip install playwright beautifulsoup4 markdownify

echo "Installing Playwright browsers..."
python -m playwright install

echo "Installation complete!"
