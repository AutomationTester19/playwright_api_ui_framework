from playwright.sync_api import Page, expect


def test_validate_Page_Title(page: Page):
    page.goto("https://admin-demo.nopcommerce.com/login")
    title = page.title()
    expect(page).to_have_title(title)
