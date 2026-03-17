import requests
import pytest

BASE_URL = "https://jsonplaceholder.typicode.com"

@pytest.mark.api
def test_get_post():
    response = requests.get(f"{BASE_URL}/posts/1")
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    
    data = response.json()
    assert "title" in data
    assert data["userId"] == 1
    assert isinstance(data["id"], int)

@pytest.mark.api
def test_create_post():
    payload = {
        "title": "foo",
        "body": "bar",
        "userId": 1
    }
    response = requests.post(f"{BASE_URL}/posts", json=payload)
    assert response.status_code == 201
    
    data = response.json()
    assert data["title"] == "foo"
    assert "id" in data  # 新创建的post有id
