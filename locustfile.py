from locust import HttpUser, between, task

class DjangoAppUser(HttpUser):
    # Time between tasks (in seconds)
    wait_time = between(1, 3)

    # This method will be executed by Locust to simulate visiting the homepage
    @task
    def index(self):
        self.client.get("/")  # Replace with your actual Django homepage URL

    # This method simulates logging in
    @task(2)  # This task is weighted more (i.e., it will be executed more frequently)
    def login(self):
        self.client.post("/login/", {
            "username": "testuser",
            "password": "password123"
        })

    # Simulate other tasks, like browsing to specific pages, submitting forms, etc.
    @task
    def view_product(self):
        self.client.get("/product/1/")  # Replace with your actual product URL
