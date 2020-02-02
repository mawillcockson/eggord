# eggord

Be an egghead

## Current build

Used [`nuitka` following these instructions](http://nuitka.net/doc/user-manual.html#id7):

1. Install scoop
1. Install [`anaconda3`](https://anaconda.net)
1. Run Anaconda Prompt
1. `conda install m2w64-gcc libpython` and `conda install -c conda-forge nuitka`
1. `python -m nuitka --standalone --show-progress --show-scons eggord.py`