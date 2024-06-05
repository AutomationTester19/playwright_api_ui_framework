from playwright.sync_api import Page, expect


def test_validate_Page_Title(page: Page):
    page.goto("https://admin-demo.nopcommerce.com/login")
    title = page.title()
    expect(page).to_have_title(title)


def test_validate_userName_IsDisplayed(page: Page):
    page.goto("https://admin-demo.nopcommerce.com/login")
    title = page.title()
    expect(page).to_have_title(title)
    username_loc = page.locator("xpath=//input[@id='Email']")
    expect(username_loc).to_be_visible()
    password_loc = page.locator("xpath=//input[@id='Password']")
    expect(password_loc).to_be_visible()
