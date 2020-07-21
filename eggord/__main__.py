"""
This file is executed when this program is run with
python -m package_name

More:
https://docs.python.org/3/library/__main__.html

It's also run by a compiled nuitka binary
"""
from eggord.eggord import cli

cli(prog_name="eggord")
