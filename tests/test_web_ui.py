from playwright.sync_api import sync_playwright, expect
import pytest

@pytest.mark.web
def test_example_search():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        # 换成无需应对反爬虫的官方测试页面
        page.goto("https://playwright.dev/")
        
        # 验证页面标题
        expect(page).to_have_title("Fast and reliable end-to-end testing for modern web apps | Playwright")
        
        # 点击搜索框
        page.click(".DocSearch-Button")
        
        # 输入并搜索
        page.fill(".DocSearch-Input", "Python")
        
        # 验证搜索结果出现
        page.wait_for_selector(".DocSearch-Dropdown")
        
        # 截图验证
        page.screenshot(path="playwright_search_result.png")
        
        browser.close()
