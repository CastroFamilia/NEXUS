import time
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto('file:///Users/alejandracastro/Desktop/NEXUS/add-search.html')
    
    # Type into search
    page.fill('#locationSearch', 'Rivas')
    time.sleep(1)
    
    # Click + Add Location button manually
    page.click('button:has-text("+ Add Location")')
    
    # See if it adds
    locs = page.query_selector_all('#locationList > div')
    print("Locations added:", len(locs))
    if len(locs) > 0:
        print("Text:", locs[0].inner_text())
        
    # Try autocomplete click
    page.fill('#locationSearch', 'Guada')
    time.sleep(1)
    # The div will have text Guada in it, we click the suggestion
    page.locator('#suggestionsBox > div').first.click()
    time.sleep(1)
    
    locs = page.query_selector_all('#locationList > div')
    print("Locations added after suggestion click:", len(locs))
    if len(locs) > 1:
        print("Text 2:", locs[0].inner_text())
        
browser.close()
