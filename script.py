from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)  # headless so it runs in cloud
        page = browser.new_page()
        page.goto("https://bricksense.streamlit.app")
        page.wait_for_timeout(5000)  # wait 5 seconds
        browser.close()

if __name__ == "__main__":
    run()
