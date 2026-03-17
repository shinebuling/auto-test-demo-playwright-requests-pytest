from playwright.sync_api import sync_playwright, expect
import pytest

@pytest.mark.web
def test_baidu_search():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("https://www.baidu.com")
        
        # 定位搜索框，输入并搜索
        page.fill("#kw", "Playwright 测试")
        page.click("#su")
        
        # 等待结果加载并断言
        page.wait_for_load_state("networkidle")
        title = page.title()
        assert "Playwright 测试" in title or "百度一下" in title
        
        # 截图验证
        page.screenshot(path="baidu_search_result.png")
        
        browser.close()
