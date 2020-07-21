# Notes

Using `typer`'s tutorial for creating a package, and trying to get it to compile with `nuitka`:

<https://typer.tiangolo.com/tutorial/package/>

## nuitka

Installed with

```sh
poetry add --dev nuitka
poetry run python -m pip install --user -U nuitka
```

Run with:

```sh
poetry run python -m nuitka --standalone eggord --include-package=eggord --output-dir=build --show-progress --run
```

## tox

For multiple versions of python, on linux I'm using pyenv, and on windows, scoop.

Not much actual management seems to be necessary: tox picks up additional python versions without fuss.

### scoop

```powershell
scoop bucket add versions
scoop install python37
scoop reset python
```

The second to last command updates all the shims scoop maintains to point to python3.7, and the last command resets them to point back at the default python, which is currently 3.8

## bugs

I've included `# NOTE:BUG` markers in source files to indicate workarounds of known bugs. If there's an open issue, I try to link to it.

I'd love to find a workflow that helps me periodically check on these, so I can remove cruft from my code instead of having a bunch of workarounds build up.
