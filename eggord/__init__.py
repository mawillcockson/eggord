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
import sys  # isort: skip

if sys.version_info >= (3, 8):
    from importlib.metadata import version
else:
    from importlib_metadata import version  # pylint: disable=import-error

# NOTE:TYPE mypy can't detect the return type of backported version()
# Needs typing.cast(str, version()) on Python 3.7-
__version__ = str(version(__name__))
