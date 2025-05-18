from locust import HttpUser, task, between

class ReqresUser(HttpUser):
    wait_time = between(1, 3)

    @task
    def get_users(self):
        self.client.get("/api/users?page=2")

    @task
    def create_user(self):
        self.client.post("/api/users", json={
            "name": "Adam",
            "job": "IT student"
        })
