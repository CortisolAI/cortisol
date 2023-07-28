from pathlib import Path

import typer

app = typer.Typer()


@app.command()
def cost_estimate(
    cortisol_file: Path = typer.Option(None, '-f', '--cortisol-file', help='Path to the CORTISOL_FILE'),
    host: str = typer.Option(None, '-h', '--host', help='Host in the following format: http://10.20.31.32 or http://10.20.31.32:8000'),
    log_file: Path = typer.Option(None, '-l', '--log-file', help='Path to log file'),
    num_users: int = typer.Option(None, '-u', '--users', help='Peak number of concurrent users'),
    spawn_rate: int = typer.Option(None, '-r', '--spawn-rate', help='Rate to spawn users at (users per second)'),
    run_time: str = typer.Option(None, '-t', '--run-time', help='Stop after the specified amount of time, e.g. (50, 30s, 200m, 5h, 2h30m, etc.). Default unit in seconds.'),
    config: Path = typer.Option(None, '--config', help='Path to config file')
):
    """
    Forecast log costs pre-production with Cortisol for Datadog, New Relic, and Grafana
    """
    if not config and any(var is None for var in (cortisol_file, host, log_file, num_users, spawn_rate, run_time)):
        typer.echo("Option '--config' is required or the following options '-f' / '--cortisol-file', "
                   "'-l' / '--log-file', '-h' / '--host', '-u' / '--users', '-r' / '--spawn-rate', '-t' / '--run-time")
        raise typer.Abort()
    
    typer.echo("Cost estimate command in the making")


if __name__ == "__main__":
    app()
