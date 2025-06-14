import re
import environ
from playwright.sync_api import Page, expect

def click_cookie_popup(page):
    page.locator('[aria-label="Akzeptieren"]').click()

async def handle_cookies_popup(page: Page):
    """Detects and clicks 'Accept Cookies' button if it appears."""
    try:
        # Adjust the selector based on the actual "Accept Cookies" button on the website
        # accept_button = page.locator("text=Akzeptieren")
        # accept_button = page.locator("text=Akzeptieren").click(force=True)
        accept_button = page.locator('[aria-label="Akzeptieren"]')
        
        if accept_button.is_visible():
            await accept_button.click()
            print("Cookies popup accepted.")
        else:
            print("No cookies popup detected.")
    except Exception as e:
        print(f"Error handling cookies popup: {e}")

def test_product_search(page: Page):
    page.goto("https://amazon.de")
    # handle_cookies_popup(page)
    page.add_locator_handler(page.get_by_label("Cookie- und Werbeeinstellungen"), click_cookie_popup)
    # popup_locator = page.locator("text=Hauptinhalt")
    # if popup_locator.is_visible():
    #     popup_locator.click()
    page.get_by_placeholder("Amazon.de durchsuchen").fill("casio watch")
    page.locator('role=button[name="Los"]').click()
    page.wait_for_selector('casio watch')
    page.get_by_role("checkbox", name="Casio").check()