import re
import environ
from playwright.sync_api import Page, expect

def test_has_title(page: Page):
    page.goto("http://localhost:3000/login")

    # Expect a title "to contain" a substring.
    expect(page).to_have_title(re.compile("User Login"))

def test_login(page: Page):
    env = environ.Env()
    username = env("EMAIL")
    password = env("USER_PWD")
    page.goto("http://localhost:3000/login")
    page.get_by_label("Username").fill(username)
    page.get_by_label("Password").fill(password)
    page.get_by_role("button", name=re.compile("Login", re.IGNORECASE)).click()

    #This waits for the page to load
    page.wait_for_url("http://localhost:3000")
    page.wait_for_selector("text=Today's date is:")

    assert "HomePage" in page.title()
    