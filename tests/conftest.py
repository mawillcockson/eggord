"""
This is a pytest-specific file for defining fixtures
https://docs.pytest.org/en/latest/fixture.html#conftest-py-sharing-fixture-functions
"""
from typing import Callable

import pytest

# NOTE:BUG python/mypy#1153
# Would love to do the below, but can't until this issue is resolved:
# https://github.com/python/mypy/issues/1153
# try:
#     from importlib.metadata import version
# except ImportError:
#     from importlib_metadata import version
#
# Using workarounds from:
# https://github.com/python/mypy/issues/1153#issuecomment-560119116
# https://github.com/bhrutledge/mypy-importlib-metadata
import sys  # isort: skip pylint: disable=wrong-import-order

if sys.version_info >= (3, 8):
    from importlib.metadata import version
else:
    from importlib_metadata import version  # pylint: disable=import-error


@pytest.fixture()
def distribution_version() -> Callable[[str], str]:
    """
    builds a function that uses importlib.metadata or its backport to find the
    version string of a package
    """

    def inner(distribution_name: str) -> str:
        """
        wrapper around importlib.metadata.version

        raises TypeError if API changes
        """
        # NOTE:TYPE mypy can't detect the return type of backported version()
        # Needs typing.cast(str, version()) on Python 3.7-
        version_identifier = version(distribution_name)
        if not isinstance(version_identifier, str):
            raise TypeError("importlib_metadata.version return type is not str")

        return version_identifier

    return inner
