from typer.testing import CliRunner

from cortisol.commands.logs import app

runner = CliRunner()


def test_cost_estimate_config_file_only_happy_case():
    result = runner.invoke(app, ["--config", "some_config_file.yaml"])

    assert result.exit_code == 0


def test_cost_estimate_configs_in_args_happy_case():
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
