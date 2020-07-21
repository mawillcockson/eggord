import pytest
from typer.testing import CliRunner

import eggord
from eggord.eggord import cli

runner = CliRunner()


def test_cli() -> None:
    result = runner.invoke(cli)
    assert result.exit_code == 0
    assert "Hello, World!" in result.stdout
