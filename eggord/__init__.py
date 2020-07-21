"""
Created by poetry:
    https://python-poetry.org

# NOTE:BUG
By default, poetry creates this file with a single line that sets the packages
dunder version attribute.
Poetry itself does _not_ update this string; it only updates version info in pyproject.toml

This GitHub issue is closed with "use importlib.metadata and its backport,
importlib_metadata"
# NOTE:FUTURE
importlib.metadata is available _provisionally_ on Python 3.8
https://github.com/python-poetry/poetry/issues/144
"""
# Get package version from metadata
# NOTE:BUG
# Would love to do the below, but can't until this issue is resolved:
# https://github.com/python/mypy/issues/1153
# try:
#     from importlib.metadata import version
# except ImportError:
#     from importlib_metadata import version

import sys

if sys.version_info >= (3, 8):
    from importlib.metadata import version
else:
    from importlib_metadata import version

__version__ = version("eggord")
