import logging
import os
import docker
from pathlib import Path


def local_log_file_size_reader(file_path: Path):
    """
    Reads the size of a log file from a locally running service.

    This function retrieves the size of a log file located at the specified file path
    for a service running locally.

    Args:
        file_path (Path): Path to the log file.

    Returns:
        int: The size of the log file in bytes.

    Raises:
        FileNotFoundError: If the specified file does not exist.

    Example:
        log_file_path = Path("path/to/log_file.log")
        log_file_size = local_log_file_size_reader(log_file_path)
    """
    try:
        if not os.path.exists(file_path):
            raise FileNotFoundError("File not found")

        # Get the file size in bytes
        file_size_bytes = os.path.getsize(file_path)
        return file_size_bytes

    except FileNotFoundError as e:
        raise FileNotFoundError(f"Error while accessing file: {e}")


def docker_log_file_size_reader(container_id: str, file_path: Path):
    """
    Reads the size of a log file from a service running within a Docker container.

    This function retrieves the size of a log file located at the specified file path
    for a service running within a Docker container.

    Args:
        container_id (str): Identifier of the Docker container.
        file_path (Path): Path to the log file within the container.

    Returns:
        int: The size of the log file in bytes.

    Raises:
        Exception: If the Docker container is not found or an API error occurs.

    Example:
        container_id = "my-container"
        log_file_path = Path("/app/playground_app.log")
        log_file_size = docker_log_file_size_reader(container_id, log_file_path)
    """
    docker_client = docker.from_env()
    try:
        container = docker_client.containers.get(container_id)
        exec_result = container.exec_run(
            ["du", "-b", str(file_path)], stdout=True, stderr=True, stream=True
        )

        # Concatenate the stream content to get the output
        exec_output = b"".join(exec_result.output)

        # Parse the file size from the output (e.g., "123   /app/playground_app.log\n")
        file_size_bytes = int(exec_output.split()[0])
        return file_size_bytes

    except docker.errors.NotFound:
        raise Exception("Container not found")

    except docker.errors.APIError as e:
        raise Exception(f"Error while executing command in the container {e}")


def log_file_size_reader(
    file_path: Path, container_id: str = "", on_start: bool = False
):
    """
    Reads the size of a log file from a service running locally with or without Docker.

    This function reads the size of a log file located at the specified file path.
    If a container ID is provided, it reads the file size from a Docker container.
    Otherwise, it reads the file size from a locally running service.

    Args:
        file_path (Path): Path to the log file.
        container_id (str, optional): Identifier of the Docker container (default: "").
        on_start: (bool, optional): True if it's called on the start of the load test (default: False).

    Returns:
        int: The size of the log file in bytes.

    Example:
        # Read log file size from a locally running service
        log_file_path = Path("path/to/log_file.log")
        log_file_size = log_file_size_reader(log_file_path)

        # Read log file size from a Docker container
        container_id = "my-container"
        log_file_size = log_file_size_reader(log_file_path, container_id, on_start=False)
    """
    try:
        if container_id != "":
            file_size = docker_log_file_size_reader(container_id, file_path)
            return file_size
        file_size = local_log_file_size_reader(file_path)
        return file_size
    except FileNotFoundError as e:
        if on_start:
            return 0
        raise FileNotFoundError(e)
    except ValueError:
        if on_start:
            return 0
        raise FileNotFoundError(file_path)


def local_count_log_entries(file_path):
    """
    Count the number of log entries in a log file.

    This function reads the specified log file and counts the number of log entries
    by counting the number of lines in the file.

    Args:
        file_path (Path): Path to the log file.

    Returns:
        float: The number of log entries in the file in millions.

    Example:
        file_path = "path/to/log_file.log"
        entry_count = local_count_log_entries(file_path)
    """
    try:
        with open(file_path, "r") as file:
            log_entries = file.readlines()
        return len(log_entries) / 1000000
    except FileNotFoundError:
        print(f"Log file '{file_path}' not found.")
        return 0


def docker_count_log_entries(container_id, file_path):
    """
    Count the number of log entries in a log file within a Docker container.

    This function reads the specified log file from a Docker container and counts
    the number of log entries by splitting the log data into lines.

    Args:
        container_id (str): Identifier of the Docker container.
        file_path (Path): Path to the log file within the container.

    Returns:
        float: The number of log entries in the file in millions.

    Example:
        container_id = "my-container"
        file_path = "/app/log_file.log"
        entry_count = docker_count_log_entries(container_id, file_path)
    """
    docker_client = docker.from_env()

    try:
        container = docker_client.containers.get(container_id)
        log_data = container.exec_run(["cat", file_path]).output
        log_entries = log_data.decode("utf-8").split("\n")
        return len(log_entries) / 1000000
    except docker.errors.NotFound:
        print(f"Container '{container_id}' not found.")
        return 0


def count_log_entries(file_path: Path, container_id: str = "", on_start: bool = False):
    """
    Count the number of log entries in a log file, locally or within a Docker container.

    This function counts the number of log entries in a log file located at the specified
    file path. If a container ID is provided, it counts log entries within the Docker container.
    Otherwise, it counts log entries from a local log file.

    Args:
        file_path (Path): Path to the log file.
        container_id (str, optional): Identifier of the Docker container (default: "").
        on_start: (bool, optional): True if it's called on the start of the load test (default: False).

    Returns:
        int: The number of log entries in the file in millions.

    Example:
        # Count log entries from a local log file
        log_file_path = Path("path/to/log_file.log")
        entry_count = count_log_entries(log_file_path)

        # Count log entries from a Docker container log file
        container_id = "my-container"
        log_file_path = Path("/app/log_file.log")
        entry_count = count_log_entries(log_file_path, container_id, False)
    """
    try:
        if container_id != "":
            return docker_count_log_entries(container_id, file_path)
        return local_count_log_entries(file_path)
    except FileNotFoundError as e:
        if on_start:
            logging.info("ON START")
            return 0
        raise FileNotFoundError(e)
    except ValueError:
        if on_start:
            return 0
        raise FileNotFoundError(file_path)
