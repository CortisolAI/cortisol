import os
import docker
from pathlib import Path


def local_log_file_size_reader(file_path: Path):
    """
    Reads log file size from a service running locally

    :param file_path:
    :type file_path:
    :return:
    :rtype:
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
    Reads log file size from a service running locally on docker

    :param container_id:
    :type container_id:
    :param file_path:
    :type file_path:
    :return:
    :rtype:
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


def log_file_size_reader(file_path: Path, container_id: str = ""):
    """
    Reads log file size from a service running locally with or without docker

    :param file_path:
    :type file_path:
    :param container_id:
    :type container_id:
    :return:
    :rtype:
    """
    if container_id != "":
        return docker_log_file_size_reader(container_id, file_path)
    else:
        return local_log_file_size_reader(file_path)
