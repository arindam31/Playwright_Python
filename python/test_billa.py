import re
from playwright.sync_api import Page, expect

def test_has_title(page: Page):
    page.goto("https://shop.billa.at//")

    # Expect a title "to contain" a substring.
    expect(page).to_have_title(re.compile("Lebensmittel online bestellen"))

# def test_get_started_link(page: Page):
#     page.goto("https://shop.billa.at//")

#     # Click the get started link.
#     page.get_by_role("link", name="English").click()

#     # Expects page to have a heading with the name of Installation.
#     expect(page.get_by_role("heading", name="Installation")).to_be_visible()

def click_cookie_popup(page):
    page.locator('//*[@id="onetrust-reject-all-handler"]').click()

def test_redirect_when_meine_product_clicked(page: Page):
    page.add_locator_handler(page.get_by_text("Privatsphäre-Einstellungen"), click_cookie_popup)
    page.goto("https://shop.billa.at//")
    page.get_by_role("span", name="Meine Produkte").click()

    page.get_by_role("email").fill("testmail@mail.com")