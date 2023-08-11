from locust import task

from cortisol.cortisollib.users import CortisolHttpUser


class WebsiteUser(CortisolHttpUser):
    @task
    def my_task(self):
        self.client.get("/")
