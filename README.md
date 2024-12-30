# API Downloader

This project allows you to **scrape** and **download** API documentation (or other websites) for offline use, converting pages into organized Markdown files, and optionally **cleaning** those Markdown files with a utility script.

## Table of Contents

1. [Features](#features)  
2. [Directory Structure](#directory-structure)  
3. [Requirements](#requirements)  
4. [Installation](#installation)  
   - [Windows Installation](#windows-installation)  
   - [Linux Installation](#linux-installation)  
5. [Usage](#usage)  
   - [Running the Scraper](#running-the-scraper)  
   - [Running the Utility Scripts](#running-the-utility-scripts)  
6. [How It Works](#how-it-works)  
7. [License](#license)  

---

## Features

- **Offline Documentation Download**: Scrape a React/JavaScript-powered documentation site using [Playwright](https://playwright.dev/python/).  
- **Markdown Output**: Each visited page is converted to `.md` and all links are rewritten as local, relative Markdown links.  
- **Resume Downloads**: If the download process is interrupted, it can be resumed without re-downloading everything.  
- **Cleanup Utility**: Optionally remove any content above the first Markdown heading in your `.md` files.

---

## Directory Structure

```bash
API_DOWNLOADER/
├── .venv/                      # Python virtual environment (created after install)
├── utils/
│   └── clean-before-heading.py # Utility script that removes text above first heading
├── install-linux-deps.sh       # Bash script to install dependencies (Linux/macOS)
├── Install-windows-deps.bat    # Batch file to install dependencies (Windows)
├── md-scrape.py                # Main Python scraper/downloader script
└── requirements.txt            # Python dependencies (if you prefer pip install -r)
```

### File Descriptions

- **`.venv/`**  
  A folder automatically created by the install scripts to hold your local Python virtual environment.  

- **`utils/clean-before-heading.py`**  
  A utility script that removes all text above the first `#` heading in each Markdown file (except `index.md`). It can optionally process a single file or an entire directory.

- **`install-linux-deps.sh`**  
  A Bash script for Linux/macOS that:  
  1. Creates a `.venv/` directory.  
  2. Installs/updates pip.  
  3. Installs Python dependencies (including Playwright).  
  4. Installs Playwright’s browsers (Chromium, Firefox, WebKit).

- **`Install-windows-deps.bat`**  
  A Windows batch file that:  
  1. Creates a `.venv/` directory.  
  2. Installs/updates pip.  
  3. Installs Python dependencies (including Playwright).  
  4. Installs Playwright’s browsers (Chromium, Firefox, WebKit).  

- **`md-scrape.py`**  
  The **main script** that asks for a URL to scrape, prompts for an output directory, and saves BFS state so that you can **resume** if needed. As it visits each page, it:
  1. Downloads the fully-rendered HTML (via Playwright).  
  2. Converts HTML to Markdown (via `markdownify`).  
  3. Rewrites links to reference local `.md` files.  
  4. Outputs `.md` files into subdirectories.

- **`requirements.txt`**  
  A simple text file listing the Python package dependencies. You can install them via:
  ```bash
  pip install -r requirements.txt
  ```
  (Not strictly required if you’re using the provided install scripts.)

---

## Requirements

- **Python 3.7+** installed (confirm by running `python --version` or `python3 --version`).  
- **Git** (optional, but useful for cloning the repo).  
- A **network connection** for initially scraping the site.  
- Supported OS:
  - Windows 10/11 or Server  
  - Linux distributions (Ubuntu, Debian, Fedora, etc.)  
  - macOS  
- **Playwright** (installed automatically by the scripts) requires additional system dependencies for headless browsers. See [Playwright docs](https://playwright.dev/python/docs/installation#system-dependencies) if you run into issues.

---

## Installation

Choose **either** Windows or Linux/macOS instructions below. Both scripts do the following:

1. Create a local Python virtual environment in `.venv`.  
2. Activate that environment (updating PATH for the current shell).  
3. Upgrade `pip` and install the required Python packages.  
4. Install the Playwright browsers so they can run headless.

### Windows Installation

1. **Double-click** `Install-windows-deps.bat` (or run it in CMD/PowerShell).
2. Wait for the script to complete—this may take a few minutes as it downloads and installs browsers.
3. Once done, you should see a `.venv` folder in your project directory.

### Linux/macOS Installation

1. **Make the script executable**:  
   ```bash
   chmod +x install-linux-deps.sh
   ```
2. **Run it**:  
   ```bash
   ./install-linux-deps.sh
   ```
3. Wait for the script to complete; a `.venv` folder will appear in your project directory.

---

## Usage

### Running the Scraper

1. **Activate the virtual environment** (manually, if you’re in a new shell session):

   - **Windows**:
     ```bat
     call .venv\Scripts\activate
     ```
   - **Linux/macOS**:
     ```bash
     source .venv/bin/activate
     ```

2. **Run the main scraper**:
   ```bash
   python md-scrape.py
   ```
3. **Provide inputs** when prompted:
   - **Base URL** to scrape (e.g. `https://base.url.com/doc`).  
   - **Output directory** (e.g. `my_docs`).  
   - **Resume** if existing BFS state is found.  
4. As it runs, the scraper will:
   - **Render** each page with Playwright.  
   - **Convert** the HTML to Markdown.  
   - **Rewrite** internal links.  
   - Save `.md` files to your chosen output directory.  
   - **Periodically** save BFS state to `visited_urls.txt`, `to_visit_urls.txt`, and `url_to_local.json`.

### Running the Utility Scripts

- After the scraper finishes, you can optionally **run a utility script**:
  - **clean-before-heading.py** (in the `utils` folder)  
  This script removes all text above the first `#` heading in a Markdown file (excluding `index.md`).

1. Still in the **activated** environment, run:
   ```bash
   python utils/clean-before-heading.py
   ```
2. **Provide** either a single `.md` filename or a directory path when prompted.  
   - The script will modify all markdown files in the folder (recursive), or just one file.

---

## How It Works

1. **BFS Scraping**:  
   - `md-scrape.py` maintains two sets: `visited` (URLs already processed) and `to_visit` (URLs discovered but not yet processed).  
   - For each URL, Playwright loads the page, waits for the main content to appear, and captures the final rendered HTML.  
   - Markdown conversion is done via [markdownify](https://github.com/matthewwithanm/python-markdownify).  

2. **Link Rewriting**:  
   - All internal links (anchors) pointing to the same base domain are converted to **relative** local `.md` links.  

3. **Resume on Interrupt**:  
   - If you exit or lose connection, the script saves BFS state files to disk. On the next run, you can choose to **resume**.  

4. **Cleaning Script**:  
   - `clean-before-heading.py` scans each file, removing lines above the first `# `. This is optional post-processing to tidy up your docs.


**Happy scraping and offline documentation building!**