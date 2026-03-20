import pytest
import requests

@pytest.fixture(scope="session")
def base_url():
    """统一定义测试用例的基础 URL"""
    return "https://jsonplaceholder.typicode.com"

@pytest.fixture(scope="session")
def api_session():
    """
    提供一个全局的 HTTP 会话。
    使用 requests.Session() 可以在多个请求间复用底层的 TCP 连接，提升测试执行速度。
    也可以统一配置 Token 等鉴权请求头。
    """
    session = requests.Session()
    session.headers.update({"Content-Type": "application/json"})
    yield session
    session.close()
