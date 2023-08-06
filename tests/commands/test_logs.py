import json

from unittest.mock import Mock, patch
from typer.testing import CliRunner
import yaml

from cortisol.commands.logs import app

runner = CliRunner()


def test_cost_estimate_yaml_config_file_only_happy_case():
    data = {
        "host": "http://10.20.31.32:8000",
        "log-file": "/path/to/logfile",
        "users": 100,
        "spawn-rate": 30,
        "run-time": "20m",
        "cortisol-file": "some_cortisol_file.py",
    }

    with runner.isolated_filesystem():
        with open("config.yml", "w") as file:
            yaml.dump(data, file)

        with patch("cortisol.commands.logs.get_cost_estimate"):
            result = runner.invoke(app, ["--config", "config.yml"])

    assert result.exit_code == 0


def test_cost_estimate_json_config_file_only_happy_case():
    data = {
        "host": "http://10.20.31.32:8000",
        "log-file": "/path/to/logfile",
        "users": 100,
        "spawn-rate": 30,
        "run-time": "20m",
        "cortisol-file": "some_cortisol_file.py",
        "container-id": "80f1bc1e7feb",
    }

    with runner.isolated_filesystem():
        with open("config.json", "w") as file:
            json.dump(data, file)

        with patch("cortisol.commands.logs.get_cost_estimate"):
            result = runner.invoke(app, ["--config", "config.json"])

    assert result.exit_code == 0


def test_cost_estimate_configs_in_args_happy_case():
    with patch("cortisol.commands.logs.get_cost_estimate"):
        result = runner.invoke(
            app,
            [
                "-h",
                "http://10.20.31.32:8000",
                "-l",
                "/path/to/logfile",
                "-u",
                "100",
                "-r",
                "30",
                "-t",
                "1h20m",
                "-f",
                "some_cortisol_file.py",
            ],
        )

    assert result.exit_code == 0


def test_cost_estimate_no_args_given():
    result = runner.invoke(app, [])

    assert result.exit_code == 1


def test_cost_estimate_one_missing_arg():
    result = runner.invoke(
        app,
        [
            "-h",
            "http://10.20.31.32:8000",
            "-l",
            "/path/to/logfile",
            "-u",
            "100",
            "-r",
            "30",
            "-t",
            "1h20m",
        ],
    )

    assert result.exit_code == 1
