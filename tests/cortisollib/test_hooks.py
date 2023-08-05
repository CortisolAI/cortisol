import unittest
from unittest.mock import patch
import prettytable
from locust.env import Environment
from unittest.mock import MagicMock
from cortisol.cortisollib.hooks import (
    on_init,
    on_request,
    on_quit,
    create_results_table,
)


class TestHooks(unittest.TestCase):
    def setUp(self):
        self.environment = MagicMock(spec=Environment)
        runner_mock = MagicMock()
        self.environment.runner = runner_mock

    def test_create_results_table(self):
        obs_stats = {
            "logs": {
                "log-volume": 100,
                "datadog-cost": 50,
                "grafana-cost": 30,
            }
        }
        table = create_results_table(obs_stats)
        self.assertIsInstance(table, prettytable.prettytable.PrettyTable)
        # You can add more assertions here based on the expected table content

    def test_on_init(self):
        on_init(self.environment)
        self.assertEqual({}, self.environment.runner.stats.custom_stats)

    def test_on_quit(self):
        environment = MagicMock()
        obs_stats = {
            "logs": {
                "log-volume": 100,
                "datadog-cost": 50,
                "grafana-cost": 30,
            }
        }
        environment.runner.stats.custom_stats = obs_stats
        on_quit(environment)
