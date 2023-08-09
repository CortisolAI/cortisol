from pathlib import Path
from unittest import TestCase
from collections import namedtuple
import os
import docker
from unittest.mock import patch, MagicMock, mock_open
from cortisol.cortisollib.readers import (
    docker_log_file_size_reader,
    local_log_file_size_reader,
    log_file_size_reader,
    local_count_log_entries,
    docker_count_log_entries,
    count_log_entries,
)

ExecResult = namedtuple("ExecResult", "exit_code,output")


class TestFileSizeFunctions(TestCase):
    @patch("docker.from_env")
    def test_docker_log_file_size_reader_success(self, mock_docker):
        # Mock the Docker client and container object
        mock_container = mock_docker.return_value.containers.get.return_value
        mock_stream = MagicMock(spec=docker.types.daemon.CancellableStream)
        mock_stream.output = b"123   /app/playground_app.log\n"
        mock_stream.__iter__.return_value = [b"123   /app/playground_app.log\n"]

        mock_container.exec_run.return_value = ExecResult(
            exit_code=0,
            output=mock_stream,  # Mock the output as CancellableStream
        )

        # Test file size reading from Docker container
        container_id = "test_container_id"
        file_path = Path("/app/playground_app.log")
        result = docker_log_file_size_reader(container_id, file_path)
        self.assertEqual(result, 123)

    def test_local_file_size_reader_success(self):
        # Test file size reading from the local file system
        file_path = Path("test_file.txt")
        with open(file_path, "wb") as file:
            file.write(b"This is a test file.")

        result = local_log_file_size_reader(file_path)
        self.assertEqual(result, 20)

        # Clean up the test file
        os.remove(file_path)

    def test_local_file_size_reader_file_not_found(self):
        # Test handling of FileNotFoundError for local file reader
        file_path = Path("non_existent_file.txt")
        with self.assertRaises(FileNotFoundError):
            local_log_file_size_reader(file_path)

    @patch("docker.from_env")
    def test_log_file_size_reader_with_container_id(self, mock_docker):
        # Test get_file_size when container_id is provided
        mock_container = mock_docker.return_value.containers.get.return_value
        mock_stream = MagicMock(spec=docker.types.daemon.CancellableStream)
        mock_stream.output = b"456   /app/playground_app.log\n"
        mock_stream.__iter__.return_value = [b"456   /app/playground_app.log\n"]

        mock_container.exec_run.return_value = ExecResult(
            exit_code=0,
            output=mock_stream,  # Mock the output as CancellableStream
        )

        container_id = "test_container_id"
        file_path = Path("/app/playground_app.log")
        result = log_file_size_reader(file_path, container_id)
        self.assertEqual(result, 456)

    def test_log_file_size_reader_without_container_id(self):
        # Test get_file_size without container_id (use local_file_size_reader)
        file_path = Path("test_file.txt")
        with open(file_path, "wb") as file:
            file.write(b"This is a test file.")

        result = local_log_file_size_reader(file_path)
        self.assertEqual(result, 20)

        # Clean up the test file
        os.remove(file_path)


class TestLogEntryCount(TestCase):
    def test_local_count_log_entries(self):
        with patch("builtins.open", mock_open(read_data="line1\nline2\nline3")):
            file_path = Path("test.log")
            entry_count = local_count_log_entries(file_path)
            self.assertEqual(3e-6, entry_count)

    @patch("docker.from_env")
    def test_docker_count_log_entries(self, mock_docker):
        mock_container = mock_docker.return_value.containers.get.return_value
        mock_container.exec_run.return_value = ExecResult(
            exit_code=0,
            output=b"line1\nline2\nline3",  # Mock the output as CancellableStream
        )

        container_id = "test-container"
        file_path = Path("/app/test.log")
        entry_count = docker_count_log_entries(container_id, file_path)
        self.assertEqual(3e-6, entry_count)

    def test_count_log_entries_local(self):
        with patch("builtins.open", mock_open(read_data="line1\nline2\nline3")):
            file_path = Path("test.log")
            entry_count = count_log_entries(file_path)
            self.assertEqual(3e-6, entry_count)

    @patch("docker.from_env")
    def test_count_log_entries_docker(self, mock_docker):
        mock_container = mock_docker.return_value.containers.get.return_value
        mock_container.exec_run.return_value = ExecResult(
            exit_code=0,
            output=b"line1\nline2\nline3",  # Mock the output as CancellableStream
        )

        container_id = "test-container"
        file_path = Path("/app/test.log")
        entry_count = count_log_entries(file_path, container_id)
        self.assertEqual(3e-6, entry_count)
