from __future__ import annotations
from time import time
from locust import HttpUser, between, task
from locust.user import User
from typing import Optional, Dict

from urllib3 import PoolManager

from locust.clients import HttpSession
from locust.exception import LocustError

from cortisol.cortisollib.readers import log_file_size_reader, count_log_entries


class CortisolHttpUser(User):
    """
    Represents an HTTP "user" which is to be spawned and attack the system that is to be load tested.

    The behaviour of this user is defined by its tasks. Tasks can be declared either directly on the
    class by using the :py:func:`@task decorator <locust.task>` on methods, or by setting
    the :py:attr:`tasks attribute <locust.User.tasks>`.

    This class creates a *client* attribute on instantiation which is an HTTP client with support
    for keeping a user session between requests.
    """

    abstract = True
    """If abstract is True, the class is meant to be subclassed, and users will not choose this locust during a test"""

    pool_manager: Optional[PoolManager] = None
    """Connection pool manager to use. If not given, a new manager is created per single user."""

    wait_time = between(2, 5)
    start_time = ""
    initial_log_volume = 0
    initial_log_entries = 0

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.host is None:
            raise LocustError(
                "You must specify the base host. Either in the host attribute in the User class, or on the command line using the --host option."
            )

        self.client = HttpSession(
            base_url=self.host,
            request_event=self.environment.events.request,
            user=self,
            pool_manager=self.pool_manager,
        )
        """
        Instance of HttpSession that is created upon instantiation of Locust.
        The client supports cookies, and therefore keeps the session between HTTP requests.
        """
        self.client.trust_env = False

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

    def context(self) -> Dict:
        default_context = {
            "log_file": self.environment.parsed_options.log_file,
            "container_id": self.environment.parsed_options.container_id,
            "start_time": self.start_time,
            "initial_log_volume": self.initial_log_volume,
            "initial_log_entries": self.initial_log_entries,
        }
        return default_context
