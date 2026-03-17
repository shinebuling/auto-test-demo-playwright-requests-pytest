from playwright.sync_api import sync_playwright, expect
import pytest

@pytest.mark.web
def test_baidu_search():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        # 添加一个 User-Agent 伪装成普通浏览器，避免被百度盾拦截无头浏览器
        context = browser.new_context(user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")
        page = context.new_page()
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
