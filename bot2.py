from playwright.sync_api import sync_playwright
import time
import random

USERNAME = "YOUR_ID"
PASSWORD = "YOUR_PASSWORD"

OPTIONS = ["Strongly Agree", "Agree", "Neutral", "Disagree", "Strongly Disagree"]


def safe_click(locator):
    try:
        locator.first.click(timeout=3000)
        return True
    except:
        return False


def handle_popup(page):
    try:
        page.wait_for_selector("text=Perform Mandatory Evaluation", timeout=4000)
        page.locator("button:has-text('OK')").first.click()
        print("✅ Popup handled")
        time.sleep(1)
    except:
        print("ℹ️ No popup")


def login(page):
    page.goto("https://presidencyuniversity.linways.com", timeout=60000)
    page.wait_for_load_state("domcontentloaded")

    # Click Student tab if present
    safe_click(page.locator("text=Student"))

    # Wait for login fields
    page.wait_for_selector("input[type='password']", timeout=10000)

    # Fill credentials
    page.locator("input[type='text']").first.fill(USERNAME)
    password_field = page.locator("input[type='password']").first
    password_field.fill(PASSWORD)

    # Try login click → fallback → Enter
    if not safe_click(page.locator("button:has-text('Login')")):
        if not safe_click(page.locator("input[type='submit']")):
            password_field.press("Enter")

    print("👉 Login triggered")
    time.sleep(5)
    print("Current URL:", page.url)


def open_dashboard(page):
    page.goto("https://presidencyuniversity.linways.com/ams/student/faculty-evaluation")
    page.wait_for_load_state("networkidle")
    handle_popup(page)


def fill_evaluation(page):
    page.wait_for_load_state("networkidle")

    dropdowns = page.locator("select")
    total = dropdowns.count()
    print(f"🧠 Found {total} dropdowns")

    for i in range(total):
        try:
            dropdown = dropdowns.nth(i)
            dropdown.select_option(label=random.choice(OPTIONS))
            time.sleep(random.uniform(0.1, 0.4))
        except:
            print(f"⚠️ Skipped {i}")

    print("✅ Filled evaluation")

    try:
        page.locator("button:has-text('Submit')").first.click()
        print("🚀 Submitted")
        time.sleep(3)
    except:
        print("⚠️ Submit not found")


with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=150)
    context = browser.new_context()
    page = context.new_page()

    # LOGIN
    login(page)

    # DASHBOARD
    open_dashboard(page)

    # LOOP THROUGH EVALUATIONS
    while True:
        cards = page.locator("div:has-text('Attend Evaluation')")

        if cards.count() == 0:
            print("🎉 No evaluations found")
            break

        found = False

        for i in range(cards.count()):
            card = cards.nth(i)

            # Skip completed ones
            if card.locator("text=Fully Evaluated").count():
                continue

            print(f"👉 Opening evaluation {i+1}")

            try:
                # Handle new tab
                with context.expect_page(timeout=10000) as new_page_info:
                    card.locator("text=Attend Evaluation").click()

                new_page = new_page_info.value
                new_page.wait_for_load_state()

                print("✅ Switched to new tab")

                # Fill evaluation
                fill_evaluation(new_page)

                # Close tab
                new_page.close()
                page.bring_to_front()

                # Reload dashboard
                open_dashboard(page)

                found = True
                break

            except Exception as e:
                print(f"❌ Error opening evaluation: {e}")

        if not found:
            print("🎉 All evaluations completed!")
            break

    time.sleep(5)
    browser.close()