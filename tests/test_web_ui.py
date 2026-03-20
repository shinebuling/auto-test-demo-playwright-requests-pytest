import allure
from pages.search_page import PlaywrightHomePage
import pytest

@allure.feature("Web UI 测试")
@allure.story("Playwright 官网主页")
@allure.title("验证首页搜索功能是否正常呈现下拉结果")
@pytest.mark.web
def test_example_search(page):
    # 使用 POM (Page Object Model) 模式，实例化页面类
    home_page = PlaywrightHomePage(page)
    
    # 导航并验证标题
    home_page.navigate()
    
    # 执行搜索
    home_page.search("Python")
    
    # 截图验证
    page.screenshot(path="playwright_search_result.png")
