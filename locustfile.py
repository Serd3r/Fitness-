from locust import HttpUser, task, between
import random

class FitnessUser(HttpUser):
    wait_time = between(1, 3)
    member_id = None
    
    def on_start(self):
        # Create a user on start
        response = self.client.post("/members/", json={
            "name": f"User_{random.randint(1, 10000)}",
            "email": f"user{random.randint(1, 10000)}@example.com",
            "membership_type": "standard"
        })
        if response.status_code == 201:
            self.member_id = response.json()["id"]

    @task(2)
    def view_classes(self):
        self.client.get("/classes/")

    @task(1)
    def book_class(self):
        if self.member_id:
            # First get classes to pick one
            classes_resp = self.client.get("/classes/")
            if classes_resp.status_code == 200 and len(classes_resp.json()) > 0:
                c_id = classes_resp.json()[0]["id"]
                self.client.post("/reservations/", json={
                    "member_id": self.member_id,
                    "class_id": c_id
                })
