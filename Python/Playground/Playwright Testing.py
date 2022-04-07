from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.webkit.launch(headless=False, slow_mo=50)
    page = browser.new_page()
    page.goto("http://whatsmyuseragent.org/")
    page.screenshot(path="example.png")
    browser.close()
