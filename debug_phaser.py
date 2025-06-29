import re
from urllib.parse import urljoin
from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup

BASE_URL = "https://docs.phaser.io/api-documentation/api-documentation"

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    
    print(f"Loading: {BASE_URL}")
    page.goto(BASE_URL)
    page.wait_for_selector("main", timeout=10000)
    html = page.content()
    
    soup = BeautifulSoup(html, "html.parser")
    
    # Find all links
    links = []
    for a_tag in soup.find_all("a", href=True):
        href = a_tag["href"]
        text = a_tag.get_text(strip=True)
        
        # Skip anchors and empty hrefs
        if not href or href.startswith("#"):
            continue
            
        # Convert to absolute URL
        absolute_url = urljoin(BASE_URL, href)
        
        # Check if it's within the API documentation domain
        if "docs.phaser.io" in absolute_url:
            links.append((href, absolute_url, text))
    
    browser.close()
    
    print(f"\nFound {len(links)} links:")
    for i, (href, abs_url, text) in enumerate(links[:20]):  # Show first 20
        print(f"{i+1}. {text[:50]:<50} | {href[:80]}")
    
    print(f"\n... and {len(links) - 20} more links" if len(links) > 20 else "")
    
    # Check for API doc specific links
    api_links = [l for l in links if "/api-documentation/" in l[1]]
    print(f"\nAPI documentation links: {len(api_links)}")