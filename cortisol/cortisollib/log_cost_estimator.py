import subprocess
from pathlib import Path
from jinja2 import Template


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
        "./cortisol/cortisollib/templates/cli_loadtest.py.j2", "r"
    ) as template_file:
        template_content = template_file.read()

    # Create a Jinja template object
    template = Template(template_content)

    with open(cortisol_file, "r") as user_input_file:
        user_input = user_input_file.read()

    # Render the template with the user input
    rendered_content = template.render(cortisolfile=user_input)

    with open("./cortisol/cortisollib/templates/locustfile.py", "w") as merged_file:
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
        "./cortisol/cortisollib/templates/locustfile.py",
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

    # Execute the command and capture the output
    process = subprocess.run(command, stdout=subprocess.PIPE)
    output = process.stdout.decode("utf-8")
    print(output)
    return process.returncode
