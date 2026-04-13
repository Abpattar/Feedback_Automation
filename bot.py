from playwright.sync_api import sync_playwright
import time
import random

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=200)
    page = browser.new_page()

    # Open login page
    page.goto("https://presidencyuniversity.linways.com")

    page.wait_for_load_state("networkidle")

    # =========================
    # LOGIN PART
    # =========================

    # Select "Student" (adjust if needed)
    page.click("text=Student")

    # Enter ID
    page.fill("input[type='text']", "YOUR_ID")

    # Enter Password
    page.fill("input[type='password']", "YOUR_PASSWORD")

    # Click Login button
    page.click("button:has-text('Sign In')")

    # Wait for login to complete
    page.wait_for_load_state("networkidle")

    print("✅ Logged in")

    # =========================
    # GO TO EVALUATION PAGE
    # =========================
    page.goto("https://presidencyuniversity.linways.com/ams/student/faculty-evaluation/view-faculty-list?evaluationId=jrMmhEu2jYts5ndYo")

    page.wait_for_load_state("networkidle")

    # =========================
    # FILL ALL DROPDOWNS
    # =========================
    dropdowns = page.locator("select")

    total = dropdowns.count()
    print(f"Found {total} dropdowns")

    options = ["Strongly Agree", "Agree", "Neutral", "Disagree", "Strongly Disagree"]

    for i in range(total):
        try:
            dropdown = dropdowns.nth(i)
            dropdown.select_option(label=random.choice(options))
            time.sleep(0.3)
        except:
            print(f"Skipped {i}")

    print("✅ Form filled")

    # =========================
    # OPTIONAL: SUBMIT BUTTON
    # =========================
    try:
        page.click("button:has-text('Submit')")
        print("🚀 Submitted")
    except:
        print("⚠️ Submit button not found")

    time.sleep(10)
    browser.close()