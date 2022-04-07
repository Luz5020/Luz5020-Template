from playwright.sync_api import Playwright, sync_playwright


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    # Open new page
    page = context.new_page()

    # Go to https://docs.google.com/forms/d/e/1FAIpQLSfmC3rMpA8sM3Xd1DBc_J8JaMilTrR4EQjvb05EhHBFj9h3Vg/viewform?usp
    # =send_form
    page.goto("https://docs.google.com/forms/d/e/1FAIpQLSfmC3rMpA8sM3Xd1DBc_J8JaMilTrR4EQjvb05EhHBFj9h3Vg/viewform"
              "?usp=send_form")

    # Go to https://docs.google.com/forms/d/e/1FAIpQLSfmC3rMpA8sM3Xd1DBc_J8JaMilTrR4EQjvb05EhHBFj9h3Vg/viewform
    page.goto("https://docs.google.com/forms/d/e/1FAIpQLSfmC3rMpA8sM3Xd1DBc_J8JaMilTrR4EQjvb05EhHBFj9h3Vg/viewform")

    # Click [aria-label="Right"]
    page.locator("[aria-label=\"Right\"]").click()

    # Click [aria-label="Right 01"]
    page.locator("[aria-label=\"Right 01\"]").click()

    # Click [aria-label="Right 02"]
    page.locator("[aria-label=\"Right 02\"]").click()

    # Click [aria-label="Right 03"]
    page.locator("[aria-label=\"Right 03\"]").click()

    # Click input[type="text"]
    page.locator("input[type=\"text\"]").click()

    # Fill input[type="text"]
    page.locator("input[type=\"text\"]").fill("This is correct")

    # Click div[role="button"]:has-text("Senden") with page.expect_navigation(
    # url="https://docs.google.com/forms/d/e/1FAIpQLSfmC3rMpA8sM3Xd1DBc_J8JaMilTrR4EQjvb05EhHBFj9h3Vg/formResponse"):
    with page.expect_navigation():
        page.locator("div[role=\"button\"]:has-text(\"Senden\")").click()
    # expect(page).to_have_url("https://docs.google.com/forms/d/e/1FAIpQLSfmC3rMpA8sM3Xd1DBc_J8JaMilTrR4EQjvb05EhHBFj9h3Vg/formResponse")

    # ---------------------
    context.close()
    browser.close()


i = 1
while i < 10:
    with sync_playwright() as playwright:
        run(playwright)
    i += 1
