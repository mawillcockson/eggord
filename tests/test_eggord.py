import pytest
from typer.testing import CliRunner

from eggord import __version__


def test_version() -> None:
    assert __version__ == "0.1.0"


runner = CliRunner()
