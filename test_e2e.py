from playwright.sync_api import sync_playwright

def test_home_page():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto('http://127.0.0.1:5000')
        assert page.title() == 'Smart Home Control'
        browser.close()