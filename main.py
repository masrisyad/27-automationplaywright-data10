from playwright.sync_api import sync_playwright

def run():
    mock_data = [{"name": "Budi", "email": "budi@mail.com"}, {"name": "Siti", "email": "siti@mail.com"}]
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://demoqa.com/text-box")
        for data in mock_data:
            page.fill("#userName", data["name"])
            page.fill("#userEmail", data["email"])
            page.click("#submit")
            print(f"Data {data['name']} terinput.")
        browser.close()

if __name__ == "__main__": run()