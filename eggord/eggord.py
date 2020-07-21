"""
This file contains the functions specified for type to use as cli
commands
"""
import sys
from datetime import datetime

import typer

cli = typer.Typer()

assert sys.version_info >= (3, 8), "Python version ~=3.8 needed"


def get_date() -> str:
    """
    returns the current date and time as

    2020-01-01T0159-0600
    """
    # From:
    # https://stackoverflow.com/a/39079819/5059062
    # https://docs.python.org/3/library/datetime.html#datetime.datetime.astimezone
    # https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior
    return datetime.now().astimezone().strftime("%Y-%m-%dT%H%M%z")


@cli.command()
def main() -> None:
    """
    default cli command
    """
    typer.echo("Hello, World!")
