import json
from pathlib import Path

import typer
import yaml

from cortisol.cortisollib.log_cost_estimator import get_cost_estimate

app = typer.Typer()


def _config_reader(file_path: Path):
    try:
        file_content = file_path.read_text()

        try:
            data = yaml.safe_load(file_content)
            return data
        except yaml.YAMLError:
            # If parsing as YAML fails, try parsing as JSON
            import pdb

            pdb.set_trace()
            data = json.loads(file_content)
            return data
        except json.JSONDecodeError:
            raise ValueError("Invalid YAML or JSON format in the input file.")
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found at path: {file_path}")


def _check_keys_in_file(file_path: Path):
    data = _config_reader(file_path)

    keys_to_check = [
        "cortisol-file",
        "host",
        "log-file",
        "run-time",
        "spawn-rate",
        "users",
    ]
    missing_keys = [key for key in keys_to_check if key not in data]

    if missing_keys:
        raise KeyError(f"Required keys are missing in the input file: {missing_keys}")


@app.command()
def cost_estimate(
    cortisol_file: Path = typer.Option(
        None, "-f", "--cortisol-file", help="Path to the CORTISOL_FILE"
    ),
    host: str = typer.Option(
        None,
        "-h",
        "--host",
        help="Host in the following format: http://10.20.31.32 or http://10.20.31.32:8000",
    ),
    log_file: Path = typer.Option(None, "-l", "--log-file", help="Path to log file"),
    num_users: int = typer.Option(
        None, "-u", "--users", help="Peak number of concurrent users"
    ),
    spawn_rate: int = typer.Option(
        None, "-r", "--spawn-rate", help="Rate to spawn users at (users per second)"
    ),
    run_time: str = typer.Option(
        None,
        "-t",
        "--run-time",
        help="Stop after the specified amount of time, e.g. (50, 30s, 200m, 5h, 2h30m, etc.). Default unit in seconds.",
    ),
    container_id: str = typer.Option(
        None,
        "-c",
        "--container-id",
        help="Optional docker container id where your application runs",
    ),
    config: Path = typer.Option(None, "--config", help="Path to config file"),
):
    """
    Forecast log costs pre-production with Cortisol for Datadog, New Relic, and Grafana
    """
    if not config and any(
        var is None
        for var in (cortisol_file, host, log_file, num_users, spawn_rate, run_time)
    ):
        typer.echo(
            "Option '--config' is required or the following options '-f' / '--cortisol-file', "
            "'-l' / '--log-file', '-h' / '--host', '-u' / '--users', '-r' / '--spawn-rate', '-t' / '--run-time"
            "'-c' / '--container-id' is required only if your application runs in a Docker container"
        )
        raise typer.Abort()

    if config:
        try:
            _check_keys_in_file(config)
            data = _config_reader(config)
            cortisol_file = data["cortisol-file"]
            host = data["host"]
            log_file = data["log-file"]
            num_users = data["users"]
            spawn_rate = data["spawn-rate"]
            run_time = data["run-time"]
            container_id = data.get("container-id", "")
        except (FileNotFoundError, ValueError, KeyError) as e:
            typer.echo(str(e))
            raise typer.Abort()

    typer.echo("Cost estimate command in the making")
    if not container_id:
        container_id = ""

    get_cost_estimate(
        cortisol_file=cortisol_file,
        host=host,
        log_file=log_file,
        num_users=num_users,
        spawn_rate=spawn_rate,
        run_time=run_time,
        container_id=container_id,
    )


if __name__ == "__main__":
    app()
