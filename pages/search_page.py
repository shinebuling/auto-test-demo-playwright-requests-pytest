from playwright.sync_api import Page, expect

class PlaywrightHomePage:
    def __init__(self, page: Page):
        self.page = page
        self.search_button = page.locator(".DocSearch-Button")
        self.search_input = page.locator(".DocSearch-Input")
        self.search_dropdown = page.locator(".DocSearch-Dropdown")

    def navigate(self):
        self.page.goto("https://playwright.dev/")
        expect(self.page).to_have_title("Fast and reliable end-to-end testing for modern web apps | Playwright")

    def search(self, keyword: str):
        self.search_button.click()
        self.search_input.fill(keyword)
        # 等待搜索结果的下拉框出现
        self.search_dropdown.wait_for()
