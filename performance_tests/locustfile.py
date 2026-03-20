from locust import HttpUser, task, between

class JsonPlaceholderUser(HttpUser):
    # 模拟用户在每个请求之间的思考/等待时间 (1到3秒)
    wait_time = between(1, 3)
    
    # 压测目标主机地址
    host = "https://jsonplaceholder.typicode.com"

    @task(2) # 权重 2 (模拟这个接口请求的频率更高)
    def test_get_post(self):
        with self.client.get("/posts/1", name="Query Single Post", catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            else:
                response.failure(f"Expected 200, got {response.status_code}")

    @task(1) # 权重 1
    def test_create_post(self):
        payload = {
            "title": "foo",
            "body": "bar",
            "userId": 1
        }
        with self.client.post("/posts", json=payload, name="Create New Post", catch_response=True) as response:
            if response.status_code == 201:
                response.success()
            else:
                response.failure("Failed to create post")