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
poetry run python -m nuitka --standalone eggord --include-package=eggord --follow-imports --output-dir=build --show-progress --run
```
