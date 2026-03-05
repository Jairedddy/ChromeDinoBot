from playwright.sync_api import sync_playwright
import config

def launch_browser():
    playwright = sync_playwright().start()
    
    browser = playwright.chromium.launch(
        headless=False,
        args=["--disable-blink-features=AutomationControlled"]
    )
    
    page = browser.new_page()

    page.goto(config.GAME_URL)
    
    return browser, page