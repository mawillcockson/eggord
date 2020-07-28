"""
Tests for the main portion of the application
"""

from typing import Callable

import pytest  # pylint: disable=unused-import
from typer.testing import CliRunner

import eggord
from eggord.eggord import cli

runner = CliRunner()


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
    result = runner.invoke(cli, "version")
    assert result.exit_code == 0
    assert result.stdout.strip() == distribution_version("eggord")


def test_hello_no_firstname() -> None:
    """
    Makes sure the hello command raises an error when it is not provided with a
    firstname
    """
    result = runner.invoke(cli, ["hello"])
    assert result.exit_code == 2
    # NOTE:WIP verify response to no arguments
    assert result.output == cli.info.short_help


@pytest.mark.parametrize("firstname", ["World", "you", " ", "{}"])
@pytest.mark.parametrize("lastname", ["World", "you", " ", "{}", None])
def test_hello(firstname: str, lastname: str) -> None:
    """
    Does the hello world command print hello world?
    """
    result = runner.invoke(cli, ["hello", firstname, lastname])
    assert result.exit_code == 0
    assert f"Hello, {firstname} {lastname}!" in result.stdout
