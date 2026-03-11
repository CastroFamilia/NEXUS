import time
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto('file:///Users/alejandracastro/Desktop/NEXUS/add-search.html')
    
    # Type into search
    page.fill('#locationSearch', 'Rivas')
    time.sleep(1)
    
    # Try autocomplete click
    page.locator('#suggestionsBox > div').first.click(force=True)
    time.sleep(1)
    
    locs = page.query_selector_all('#locationList > div')
    print("Locations added after suggestion click:", len(locs))
    
    page.fill('#locationSearch', 'San Jose')
    page.click('button:has-text("+ Add Location")')
    time.sleep(1)
    locs = page.query_selector_all('#locationList > div')
    print("Locations added after button click:", len(locs))

    page.screenshot(path='test-out.png')
    browser.close()
