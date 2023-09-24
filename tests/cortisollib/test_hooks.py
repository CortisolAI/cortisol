import os
import unittest
from pathlib import Path
from unittest.mock import patch
import prettytable
from locust.env import Environment
from unittest.mock import MagicMock
from cortisol.cortisollib.hooks import (
    on_init,
    on_request,
    on_quit,
    create_results_table,
    colorize,
    add_symbol,
)


class TestFormattingFunctions(unittest.TestCase):
    def test_colorize(self):
        value = "Some Text"
        key = "log-volume"
        expected_colorized_value = "\033[38;2;255;255;255mSome Text\033[0m"
        colorized_value = colorize(value, key)
        self.assertEqual(colorized_value, expected_colorized_value)

    def test_add_symbol(self):
        key = "log-volume"
        value = 150.0
        expected_formatted_value = "150.0 GiB"
        formatted_value = add_symbol(key, value)
        self.assertEqual(formatted_value, expected_formatted_value)


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

    def test_on_quit_table(self):
        obs_stats = {
            "stats_file": None,
            "n_requests": 10,
            "logs": {
                "log-volume": 100,
                "datadog-cost": 50,
                "grafana-cost": 30,
                "new-relic-cost": 30,
                "gcp-cloud-logging-cost": 30,
            },
        }
        self.environment.runner.stats.custom_stats = obs_stats
        result = on_quit(self.environment)
        self.assertIsInstance(result, prettytable.prettytable.PrettyTable)

    def test_on_quit_stats_file(self):
        stats_file_path = "cortisol_test_stats_file_exists.csv"
        obs_stats = {
            "stats_file": stats_file_path,
            "n_requests": 10,
            "logs": {
                "log-volume": 100,
                "datadog-cost": 50,
                "grafana-cost": 30,
                "new-relic-cost": 30,
                "gcp-cloud-logging-cost": 30,
            },
        }
        self.environment.runner.stats.custom_stats = obs_stats
        _ = on_quit(self.environment)
        if not Path(stats_file_path).resolve().is_file():
            raise AssertionError("File does not exist: %s" % str(stats_file_path))
        os.remove(stats_file_path)

    @patch("cortisol.cortisollib.readers.docker_log_file_size_reader")
    @patch("cortisol.cortisollib.readers.docker_count_log_entries")
    def test_on_request(
        self, mock_docker_count_log_entries, mock_docker_log_file_size_reader
    ):
        keys = [
            "log-volume",
            "datadog-cost",
            "grafana-cost",
            "new-relic-cost",
            "gcp-cloud-logging-cost",
        ]

        context = {
            "log_file": Path("/app/playground_app.log"),
            "container_id": "test_container_id",
            "start_time": 1,
            "initial_log_volume": 0,
            "initial_log_entries": 0,
            "stats_file": "file.csv",
        }
        mock_docker_log_file_size_reader.return_value = 1024
        mock_docker_count_log_entries.return_value = 3

        stats = on_request(
            request_type="test_request_type",
            name="test_request",
            response_time=1,
            response_length=1,
            exception=None,
            context=context,
        )

        for key in keys:
            self.assertIn(key, stats["logs"], f"{key} not found in the dictionary")
