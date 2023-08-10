from time import time
from locust import HttpUser, between, task

from cortisol.cortisollib.readers import log_file_size_reader, count_log_entries


class WebsiteUser(HttpUser):
    wait_time = between(2, 5)
    start_time = ""
    initial_log_volume = 0
    initial_log_entries = 0

    @task
    def my_task(self):
        self.client.get(
            "/",
            context={
                "log_file": self.environment.parsed_options.log_file,
                "container_id": self.environment.parsed_options.container_id,
                "start_time": self.start_time,
                "initial_log_volume": self.initial_log_volume,
                "initial_log_entries": self.initial_log_entries,
            },
        )

    def on_start(self):
        self.start_time = time()
        self.initial_log_volume = log_file_size_reader(
            file_path=self.environment.parsed_options.log_file,
            container_id=self.environment.parsed_options.container_id,
            on_start=True,
        )
        self.initial_log_entries = count_log_entries(
            file_path=self.environment.parsed_options.log_file,
            container_id=self.environment.parsed_options.container_id,
            on_start=True,
        )
