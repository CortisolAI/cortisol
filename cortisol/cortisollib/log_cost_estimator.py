import subprocess
from pathlib import Path
from jinja2 import Template


def render_locustfile(cortisol_file: Path):
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
    log_file: Path, num_users: int, spawn_rate: int, run_time: str, container_id: str
):
    command = [
        "locust",
        "-f",
        "./cortisol/cortisollib/templates/locustfile.py",
        "--headless",
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
    log_file: Path,
    num_users: int,
    spawn_rate: int,
    run_time: str,
    container_id: str,
):
    render_locustfile(cortisol_file)

    command = render_locust_command(
        log_file, num_users, spawn_rate, run_time, container_id
    )

    # Execute the command and capture the output
    process = subprocess.run(command, stdout=subprocess.PIPE)
    output = process.stdout.decode("utf-8")
    print(output)
    return process.returncode
