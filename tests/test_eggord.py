"""
Tests for the main portion of the application
"""

from functools import partial
from typing import Callable

import pytest  # pylint: disable=unused-import
from typer.testing import CliRunner

import eggord
from eggord.eggord import cli

runner = CliRunner()
run = partial(runner.invoke, cli)


VersionFinder = Callable[[str], str]


def test_version_string(distribution_version: VersionFinder) -> None:
    """
    Make sure the version string built into the package matches the module's
    version string
    """
    assert eggord.__version__ == distribution_version("eggord")


def test_version(distribution_version: VersionFinder) -> None:
    """
    Make sure the version command returns the tool's current version
    """
    result = run("version")
    assert result.exit_code == 0
    assert result.stdout.strip() == distribution_version("eggord")


# NOTE:WIP verify response to no arguments
@pytest.mark.xfail(reason="Do not know how to get help output from Typer instance")
def test_hello_no_args() -> None:
    """
    Makes sure the hello command raises an error when it is not provided with any arguments
    """
    result = run("hello")
    assert result.exit_code == 2
    assert result.output == cli.info.short_help


@pytest.mark.parametrize("firstname", ["World", "you"])
@pytest.mark.parametrize("lastname", ["World", "you"])
def test_hello(firstname: str, lastname: str) -> None:
    """
    Does the hello world command print hello world?
    """
    result = run(["hello", firstname, lastname])
    assert result.exit_code == 0
    assert f"Hello, {firstname} {lastname}!" in result.stdout


@pytest.mark.xfail(
    reason="Don't know how to indicate a positional argument as optional"
)
@pytest.mark.parametrize("firstname", ["first", " "])
def test_hello_no_lastname(firstname: str) -> None:
    """
    Ensure hello's lastname is optional
    """
    result = run(["hello", firstname])
    assert result.exit_code == 0
    assert f"Hello, {firstname}!" in result.output


def test_hello_yell_no_lastname() -> None:
    """
    Ensure hello's --yell option capitalizes just a firstname
    """
    result = run(["hello", "--yell", "first"])
    assert result.exit_code == 0
    assert result.output.isupper()
    assert "HELLO, FIRST!" in result.output


def test_hello_yell_full_name() -> None:
    """
    Ensure hello's --yell option capitalizes a whole name
    """
    result = run(["hello", "--yell", "first", "last"])
    assert result.exit_code == 0
    assert result.output.isupper()
    assert "HELLO, FIRST LAST!" in result.output
