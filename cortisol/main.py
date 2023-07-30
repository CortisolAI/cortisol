from pathlib import Path

import typer

from cortisol.commands.logs import app as log_commands

_LOGO = """
   ____           _   _           _ 
  / ___|___  _ __| |_(_)___  ___ | |
 | |   / _ \| '__| __| / __|/ _ \| |
 | |__| (_) | |  | |_| \__ \ (_) | |
  \____\___/|_|   \__|_|___/\___/|_|
                                                                       
"""

app = typer.Typer()


@app.callback()
def display_logo():
    typer.echo(_LOGO)


app.add_typer(log_commands, name="logs")


if __name__ == "__main__":
    app()
