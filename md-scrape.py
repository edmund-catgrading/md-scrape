import os
import re
import json
import subprocess
from urllib.parse import urljoin
from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
from markdownify import markdownify

# ---------------------------------------------------------
# ------------------- Utility Functions --------------------
# ---------------------------------------------------------

def sanitize_filename(name: str) -> str:
    """Remove illegal characters for filenames."""
    return re.sub(r'[\\/*?:"<>|]', '_', name)

def convert_html_to_markdown(html_content: str) -> str:
    """Convert HTML to Markdown (adjust markdownify settings as needed)."""
    return markdownify(html_content, heading_style="ATX")

def rewrite_local_links(soup: BeautifulSoup, current_url: str, url_to_local: dict):
    """
    Rewrite <a> tags to point to local .md files using relative paths.

    - soup: BeautifulSoup object for the page
    - current_url: the URL of the *current* page (string)
    - url_to_local: dict mapping absolute URLs -> local MD file paths
    """
    current_md_path = url_to_local[current_url]  # local .md file for the page

    for a_tag in soup.find_all("a", href=True):
        href = a_tag["href"]
        # Skip anchors, empty, or external
        if not href or href.startswith("#"):
            continue

        absolute = urljoin(current_url, href)
        # Check if it’s in our domain
        if BASE_URL not in absolute:
            continue

        if absolute not in url_to_local:
            # If not yet visited, precompute its local file path
            url_to_local[absolute] = url_to_filename(absolute)

        target_md_path = url_to_local[absolute]

        # Compute a relative path from current .md to the target .md
        relative_path = os.path.relpath(
            target_md_path, 
            start=os.path.dirname(current_md_path)
        )

        a_tag["href"] = relative_path

def url_to_filename(url: str) -> str:
    """
    Convert a doc URL into a local .md file path.

    """
    # Strip the base portion
    rel = url.replace(BASE_URL, "").lstrip("/")
    if not rel:
        rel = "index"
    parts = rel.split("/")
    # Sanitize each part
    parts = [sanitize_filename(p) for p in parts]
    filename = parts[-1] + ".md"
    subdirs = parts[:-1]
    return os.path.join(OUTPUT_DIR, *subdirs, filename)

def save_bfs_state(visited, to_visit, url_to_local):
    """Persist BFS sets/dict to files so we can resume later."""
    visited_path = os.path.join(OUTPUT_DIR, "visited_urls.txt")
    to_visit_path = os.path.join(OUTPUT_DIR, "to_visit_urls.txt")
    mapping_path = os.path.join(OUTPUT_DIR, "url_to_local.json")

    # Ensure output directory exists
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    with open(visited_path, "w", encoding="utf-8") as f:
        for url in visited:
            f.write(url + "\n")

    with open(to_visit_path, "w", encoding="utf-8") as f:
        for url in to_visit:
            f.write(url + "\n")

    with open(mapping_path, "w", encoding="utf-8") as f:
        json.dump(url_to_local, f, indent=2)

def load_bfs_state():
    """Load BFS sets/dict from files. Return (visited, to_visit, url_to_local)."""
    visited_path = os.path.join(OUTPUT_DIR, "visited_urls.txt")
    to_visit_path = os.path.join(OUTPUT_DIR, "to_visit_urls.txt")
    mapping_path = os.path.join(OUTPUT_DIR, "url_to_local.json")

    visited = set()
    to_visit = set()
    url_to_local = {}

    if os.path.exists(visited_path):
        with open(visited_path, "r", encoding="utf-8") as f:
            for line in f:
                visited.add(line.strip())

    if os.path.exists(to_visit_path):
        with open(to_visit_path, "r", encoding="utf-8") as f:
            for line in f:
                to_visit.add(line.strip())

    if os.path.exists(mapping_path):
        with open(mapping_path, "r", encoding="utf-8") as f:
            url_to_local = json.load(f)

    return visited, to_visit, url_to_local

def run_utility_script():
    """Ask user if they'd like to run a utility script from `utils` folder."""
    choice = input("\nWould you like to process the files with a utility script (y/n)? ").strip().lower()
    if choice != "y":
        return

    # List all python scripts in `utils` folder
    utils_dir = "utils"
    if not os.path.isdir(utils_dir):
        print(f"No '{utils_dir}' folder found. Skipping utility scripts.")
        return

    scripts = [
        f for f in os.listdir(utils_dir)
        if f.endswith(".py") and os.path.isfile(os.path.join(utils_dir, f))
    ]
    if not scripts:
        print(f"No .py files found in {utils_dir}.")
        return

    print("\nAvailable utility scripts:")
    for i, script_name in enumerate(scripts, start=1):
        print(f"  {i}. {script_name}")

    # Prompt user for a script selection
    while True:
        selection = input("\nEnter the number of the script you want to run (or 'q' to quit): ").strip()
        if selection.lower() == 'q':
            print("Skipping utility scripts.")
            return
        if selection.isdigit():
            idx = int(selection)
            if 1 <= idx <= len(scripts):
                chosen_script = scripts[idx - 1]
                script_path = os.path.join(utils_dir, chosen_script)

                print(f"\nRunning script: {chosen_script}\n")
                try:
                    # Run the script in a subprocess
                    subprocess.run(["python", script_path], check=True)
                except subprocess.CalledProcessError as e:
                    print(f"Error running '{chosen_script}': {e}")
                return
        print("Invalid selection. Try again or press 'q' to quit.")

# ---------------------------------------------------------
# ---------------------- Main Logic ------------------------
# ---------------------------------------------------------

def main():
    global BASE_URL, OUTPUT_DIR

    # Prompt for base URL and output directory
    BASE_URL = input("Enter the base URL to scrape: ").strip()
    if not BASE_URL:
        print("Base URL cannot be empty. Exiting.")
        return

    OUTPUT_DIR = input("Enter the output directory (e.g. dir_name): ").strip()
    if not OUTPUT_DIR:
        print("Output directory cannot be empty. Exiting.")
        return

    # Check if BFS state exists, ask user to resume
    visited, to_visit, url_to_local = set(), set(), {}
    visited_exists = os.path.exists(os.path.join(OUTPUT_DIR, "visited_urls.txt"))
    to_visit_exists = os.path.exists(os.path.join(OUTPUT_DIR, "to_visit_urls.txt"))
    mapping_exists = os.path.exists(os.path.join(OUTPUT_DIR, "url_to_local.json"))

    if visited_exists and to_visit_exists and mapping_exists:
        choice = input("Found existing BFS state. Resume from previous run (y/n)? ").strip().lower()
        if choice == "y":
            visited, to_visit, url_to_local = load_bfs_state()
            print(f"Resuming: {len(visited)} visited, {len(to_visit)} to_visit.")
        else:
            print("Starting fresh. Existing BFS state will be overwritten.")
    else:
        print("No existing BFS state found. Starting fresh.")

    # If starting fresh, initialize BFS
    if not visited and not to_visit:
        to_visit = {BASE_URL}
        url_to_local = {BASE_URL: url_to_filename(BASE_URL)}

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        try:
            # BFS loop
            while to_visit:
                url = to_visit.pop()
                if url in visited:
                    continue

                visited.add(url)
                print(f"Scraping: {url}")

                # Make sure the URL has a mapping
                if url not in url_to_local:
                    url_to_local[url] = url_to_filename(url)

                # Attempt to load the page
                try:
                    page.goto(url)
                    page.wait_for_selector("main", timeout=10000)  # Wait for main content
                    html = page.content()
                except Exception as e:
                    print(f"Error loading {url}: {e}")
                    # Save BFS state and continue
                    save_bfs_state(visited, to_visit, url_to_local)
                    continue

                soup = BeautifulSoup(html, "html.parser")

                # Extract new links
                for a_tag in soup.find_all("a", href=True):
                    href = a_tag["href"]
                    if not href or href.startswith("#"):
                        continue
                    absolute = urljoin(url, href)
                    # If in doc domain
                    if BASE_URL in absolute:
                        if absolute not in visited:
                            to_visit.add(absolute)
                        if absolute not in url_to_local:
                            url_to_local[absolute] = url_to_filename(absolute)

                # Rewrite links in this soup
                rewrite_local_links(soup, url, url_to_local)
                # Convert to MD
                md = convert_html_to_markdown(str(soup))

                # Save MD
                md_file_path = url_to_local[url]
                os.makedirs(os.path.dirname(md_file_path), exist_ok=True)
                with open(md_file_path, "w", encoding="utf-8") as f:
                    f.write(md)

                # Save BFS state periodically so we can resume even if interrupted
                save_bfs_state(visited, to_visit, url_to_local)

        except KeyboardInterrupt:
            # If user hits CTRL+C, we still save BFS state so we can resume later
            print("\nInterrupted by user. Saving BFS state...")
            save_bfs_state(visited, to_visit, url_to_local)

        except Exception as e:
            # Catch any other errors, save BFS state
            print(f"An unexpected error occurred: {e}")
            save_bfs_state(visited, to_visit, url_to_local)

        finally:
            browser.close()

    # Done. Show summary
    print("\nScraping complete.")
    print(f"Visited URLs: {len(visited)}")
    print(f"Remaining in queue: {len(to_visit)}")
    print(f"Output directory: {OUTPUT_DIR}")

    # Ask user to run a utility script
    run_utility_script()

if __name__ == "__main__":
    main()
