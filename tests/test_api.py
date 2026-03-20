import pytest
import allure

@allure.feature("API 接口测试")
@allure.story("Posts 模块")
@allure.title("批量测试获取文章详情接口 (Data-Driven)")
@pytest.mark.api
@pytest.mark.parametrize("post_id, expected_user_id, expected_status", [
    (1, 1, 200),
    (2, 1, 200),
    (11, 2, 200),
    (999, None, 404)  # 异常流测试：ID不存在
])
def test_get_post(api_session, base_url, post_id, expected_user_id, expected_status):
    """
    通过参数化测试数据驱动，验证多组获取文章的场景
    """
    response = api_session.get(f"{base_url}/posts/{post_id}")
    assert response.status_code == expected_status, f"Expected {expected_status}, got {response.status_code}"
    
    if expected_status == 200:
        data = response.json()
        assert "title" in data
        assert data["userId"] == expected_user_id
        assert data["id"] == post_id
        assert isinstance(data["id"], int)

@allure.feature("API 接口测试")
@allure.story("Posts 模块")
@allure.title("批量测试创建文章接口 (Data-Driven)")
@pytest.mark.api
@pytest.mark.parametrize("payload, expected_status", [
    ({"title": "hello", "body": "world", "userId": 1}, 201),
    ({"title": "only_title", "userId": 2}, 201),  # 部分字段
    ({}, 201)  # 空 Payload 数据创建
])
def test_create_post(api_session, base_url, payload, expected_status):
    """
    通过参数化测试不同 Payload 组合下的文章创建接口
    """
    response = api_session.post(f"{base_url}/posts", json=payload)
    assert response.status_code == expected_status
    
    data = response.json()
    if payload:
        for key in payload.keys():
            assert data[key] == payload[key]
    assert "id" in data  # 新创建的post有id
