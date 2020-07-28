"""
Created by poetry:
    https://python-poetry.org

# NOTE:BUG
By default, poetry creates this file with a single line that sets the packages
dunder version attribute.
Poetry itself does _not_ update this string; it only updates version info in
pyproject.toml

This GitHub issue is closed with "use importlib.metadata and its backport,
importlib_metadata"
# NOTE:FUTURE
importlib.metadata is available _provisionally_ on Python 3.8
https://github.com/python-poetry/poetry/issues/144
"""
# Get package version from metadata
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
# isort: off
import sys

if sys.version_info >= (3, 8):
    # NOTE:TYPE "as version" for mypy
    # https://mypy.readthedocs.io/en/stable/command_line.html#cmdoption-mypy-no-implicit-reexport
    from importlib.metadata import (  # pylint: disable=useless-import-alias
        version as version,
    )
else:
    from importlib_metadata import version  # pylint: disable=import-error
# isort: on

# NOTE:TYPE mypy can't detect the return type of backported
# importlib_metadata.version();
# Needs typing.cast(str, version()) on Python 3.7-
__version__ = str(version(__name__))
