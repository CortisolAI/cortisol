import ast
import threading
import time
import subprocess
from pathlib import Path
import os
from jinja2 import Template

_FILE_DIR_PATH = os.path.dirname(os.path.realpath(__file__))


def animation_process(timeout, done):
    animation = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
    start_time = time.time()
    while True:
        elapsed_time = time.time() - start_time
        if done.is_set():
            break
        remaining_seconds = max(0.0, timeout - elapsed_time)
        minutes = int(remaining_seconds / 60)
        seconds = int(remaining_seconds % 60)
        timer_text = f"{minutes:02d}:{seconds:02d}"
        animation_index = int(elapsed_time * 10) % len(animation)
        animation_char = animation[animation_index]
        print(
            f"{animation_char} Hold tight cortisol is estimating your monthly log cost {animation_char} Remaining time: {timer_text}",
            end="\r",
        )
        time.sleep(0.1)


def _get_classes_extending_httpuser(code):
    tree = ast.parse(code)

    class_names = []
    for node in ast.walk(tree):
        if isinstance(node, ast.ClassDef):
            for base in node.bases:
                if isinstance(base, ast.Name) and base.id == "CortisolHttpUser":
                    class_names.append(node.name)

    formatted_string = "[" + ", ".join(class_names) + "]"
    return formatted_string


def render_locustfile(cortisol_file: Path):
    """
    Render a Locustfile template with user input and save the result.

    This function reads a Jinja2 template for a Locust load test scenario from the template file,
    merges it with the user-provided input from the specified 'cortisol_file', and then writes
    the rendered content to a new Locustfile. The rendered content is returned.

    Args:
        cortisol_file (Path): Path to the user input file containing parameters for the load test.

    Returns:
        str: The rendered content of the Locustfile after merging the template with user input.

    Example:
        cortisol_file = Path("path/to/user_input.yaml")
        rendered_content = render_locustfile(cortisol_file)
    """
    with open(
        os.path.join(_FILE_DIR_PATH, "./templates/cli_loadtest.py.j2"), "r"
    ) as template_file:
        template_content = template_file.read()

    # Create a Jinja template object
    template = Template(template_content)

    with open(cortisol_file, "r") as user_input_file:
        user_input = user_input_file.read()
        user_classes = _get_classes_extending_httpuser(user_input)

    # Render the template with the user input
    rendered_content = template.render(
        cortisolfile=user_input, user_classes=user_classes
    )

    with open(
        os.path.join(_FILE_DIR_PATH, "./templates/locustfile.py"), "w"
    ) as merged_file:
        merged_file.write(rendered_content)

    return rendered_content


def render_locust_command(
    host: str,
    log_file: Path,
    num_users: int,
    spawn_rate: int,
    run_time: str,
    container_id: str,
):
    """
    Generate a command for running a Locust load test in headless mode.

    This function generates a command list that can be used to run a Locust load test
    in headless mode. The command includes options such as the Locustfile path,
    number of users, spawn rate, run time, container ID, and log file path.

    Args:
        log_file (Path): Path to the log file where Locust logs will be stored.
        num_users (int): Number of concurrent users/clients to simulate.
        spawn_rate (int): The rate at which new users are spawned per second.
        run_time (str): The duration of the load test run (e.g., '10m' for 10 minutes).
        container_id (str): Identifier for the Docker container, if applicable.

    Returns:
        List[str]: A list representing the command for running the Locust load test.

    Example:
        log_file = Path("path/to/locust_logs.log")
        num_users = 100
        spawn_rate = 10
        run_time = '15m'
        container_id = 'my-locust-container'

        command = render_locust_command(log_file, num_users, spawn_rate, run_time, container_id)
        # Execute the command using subprocess or other method
    """
    command = [
        "locust",
        "-f",
        os.path.join(_FILE_DIR_PATH, "./templates/locustfile.py"),
        "--headless",
        "--host",
        host,
        "--users",
        str(num_users),
        "--spawn-rate",
        str(spawn_rate),
        "--run-time",
        str(run_time),
        "--container-id",
        container_id,
        "--log-file",
        log_file,
    ]

    return command


def get_cost_estimate(
    cortisol_file: Path,
    host: str,
    log_file: Path,
    num_users: int,
    spawn_rate: int,
    run_time: str,
    container_id: str = "",
):
    """
    Calculate the estimated cost of logs.

    This function calculates the estimated cost of logs using the Locust
    load testing tool. It renders the Locustfile specified in 'cortisol_file', generates
    the Locust command based on the provided parameters, executes the command, captures
    the output, and returns the return code of the process.

    Args:
        cortisol_file (Path): Path to the Locustfile containing the load test scenario.
        host (str): Host to load test in the following format: http://10.21.32.33
        log_file (Path): Path to the log file where Locust logs will be stored.
        num_users (int): Number of concurrent users/clients to simulate.
        spawn_rate (int): The rate at which new users are spawned per second.
        run_time (str): The duration of the load test run (e.g., '10m' for 10 minutes).
        container_id (str): Identifier for the Docker container, if applicable.

    Returns:
        int: The return code of the subprocess that executed the Locust load test.

    Example:
        cortisol_file = Path("path/to/locustfile.py")
        log_file = Path("path/to/locust_logs.log")
        num_users = 100
        spawn_rate = 10
        run_time = '15m'
        container_id = 'my-locust-container'

        return_code = get_cost_estimate(cortisol_file, log_file, num_users, spawn_rate, run_time, container_id)
    """
    render_locustfile(cortisol_file)

    command = render_locust_command(
        host, log_file, num_users, spawn_rate, run_time, container_id
    )

    done = threading.Event()
    process = None
    animation_thread = None
    try:
        process = subprocess.Popen(
            command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
        )

        if run_time.endswith("m"):
            total_seconds = float(run_time[:-1]) * 60
        elif run_time.endswith("s"):
            total_seconds = float(run_time[:-1])
        else:
            raise ValueError(
                "Invalid runtime format. Use 'Xm' for minutes or 'Xs' for seconds."
            )

        animation_thread = threading.Thread(
            target=animation_process,
            args=(
                total_seconds,
                done,
            ),
        )
        animation_thread.start()

        try:
            output, error = process.communicate(timeout=total_seconds + 2)
        except subprocess.TimeoutExpired as e:
            process.kill()
            output, error = process.communicate()
            stderr_output = error.strip()
            print(stderr_output)
            raise TimeoutError(stderr_output) from e

        if process.returncode == 0:
            print(output)
        else:
            print(error.strip())

    except KeyboardInterrupt as e:
        if process is not None:
            process.terminate()
            _, error = process.communicate()
            stderr_output = error.strip()
            print(stderr_output)
            raise KeyboardInterrupt(stderr_output) from e
        raise KeyboardInterrupt from e

    finally:
        if process and process.poll() is None:
            process.terminate()
        if animation_thread is not None:
            done.set()
            animation_thread.join()

    return process.returncode
