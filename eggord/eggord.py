"""
This file contains the functions specified for type to use as cli
commands
"""
from datetime import datetime

import typer

import eggord

cli = typer.Typer()


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
def hello(firstname: str, lastname: str, yell: bool = False) -> None:
    """
    Says hello
    """
    if lastname:
        greeting = f"Hello, {firstname} {lastname}!"
    else:
        greeting = f"Hello, {firstname}!"

    if yell:
        typer.echo(greeting.upper())
    else:
        typer.echo(greeting)


@cli.command()
def version() -> None:
    """
    Prints the version string
    """
    typer.echo(eggord.__version__)
