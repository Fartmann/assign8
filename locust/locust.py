from locust import HttpUser, task, between

class ReqresUser(HttpUser):
    wait_time = between(1, 3)

    @task(2)
    def get_users(self):
        self.client.get("/api/users?page=2")

    @task(1)
    def create_user(self):
        self.client.post("/api/users", json={
            "name": "don",
            "job": "hacker"
        })

    @task(1)
    def login_user(self):
        self.client.post("/api/login", json={
            "email": "eve.holt@reqres.in",
            "password": "cityslicka"
        })
