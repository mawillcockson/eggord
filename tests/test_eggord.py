"""
Tests for the main portion of the application
"""

from typing import Callable

# NOTE:LINT Remove linting disable once pytest is in use
import pytest  # pylint: disable=unused-import

# Available because pytest is available
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


def test_hello() -> None:
    """
    Does the hello world command print hello world?
    """
    result = runner.invoke(cli, "hello")
    assert result.exit_code == 0
    assert "Hello, World!" in result.stdout
