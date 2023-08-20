import os
import unittest
from unittest.mock import Mock, patch
from pathlib import Path

from cortisol.cortisollib.log_cost_estimator import (
    render_locustfile,
    render_locust_command,
    get_cost_estimate,
    _get_classes_extending_httpuser,
)

_FILE_DIR_PATH = os.path.normpath(
    os.path.join(os.path.dirname(__file__), "..", "..", "cortisol", "cortisollib")
)


class TestLibLogs(unittest.TestCase):
    def setUp(self):
        # Create temporary files for testing
        self.host = "http://127.0.0.1:8080"
        self.num_users = 100
        self.spawn_rate = 10
        self.run_time = "10m"
        self.container_id = "123mock"
        self.cortisol_file = Path("test_cortisol.py")
        self.log_file = Path("test_log.txt")

    def tearDown(self):
        # Clean up temporary files after testing
        self.cortisol_file.unlink(missing_ok=True)
        self.log_file.unlink(missing_ok=True)

    def test_render_locustfile(self):
        # Create a temporary cortisol input file for testing
        cortisol_input = "user_data: test"
        self.cortisol_file.write_text(cortisol_input)

        rendered_content = render_locustfile(self.cortisol_file)

        # Check if the rendered content contains the expected string
        self.assertIn("user_data: test", rendered_content)

    def test_render_locust_command(self):
        # Define test input values

        # Expected command
        expected_command = [
            "locust",
            "-f",
            os.path.join(_FILE_DIR_PATH, "./templates/locustfile.py"),
            "--headless",
            "--host",
            self.host,
            "--users",
            str(self.num_users),
            "--spawn-rate",
            str(self.spawn_rate),
            "--run-time",
            str(self.run_time),
            "--container-id",
            self.container_id,
            "--log-file",
            Path(self.log_file),
        ]

        result = render_locust_command(
            host=self.host,
            log_file=Path(self.log_file),
            num_users=self.num_users,
            spawn_rate=self.spawn_rate,
            run_time=self.run_time,
            container_id=self.container_id,
        )

        # Assert the result matches the expected command
        self.assertEqual(result, expected_command)

    @patch("cortisol.cortisollib.readers.log_file_size_reader")
    @patch("cortisol.cortisollib.log_cost_estimator.subprocess")
    @patch("cortisol.cortisollib.log_cost_estimator.render_locustfile")
    def test_get_cost_estimate(
        self, mock_render_locustfile, mock_subprocess, mock_log_file_size_reader
    ):
        process_mock = Mock(
            stdout=b"mocked_stdout", stderr=b"mocked_stderr", returncode=0
        )
        mock_subprocess.Popen.return_value.communicate.return_value = (
            process_mock.stdout,
            process_mock.stderr,
        )
        mock_subprocess.Popen.return_value.returncode = process_mock.returncode
        mock_log_file_size_reader.return_value = 1024
        mock_render_locustfile.return_value = 0

        cortisol_input = "user_data: test"
        self.cortisol_file.write_text(cortisol_input)

        result = get_cost_estimate(
            cortisol_file=self.cortisol_file,
            host=self.host,
            log_file=self.log_file,
            num_users=self.num_users,
            spawn_rate=self.spawn_rate,
            run_time=self.run_time,
            container_id=self.container_id,
        )

        self.assertEqual(result, 0)

    def test_single_class(self):
        code = """
class MyUser(CortisolHttpUser):
    pass
"""
        result = _get_classes_extending_httpuser(code)
        self.assertEqual(result, "[MyUser]")

    def test_multiple_classes(self):
        code = """
class MyUser(CortisolHttpUser):
    pass

class AnotherUser(CortisolHttpUser):
    pass
        """
        result = _get_classes_extending_httpuser(code)
        self.assertEqual(result, "[MyUser, AnotherUser]")
