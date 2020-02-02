import sys
from argparse import ArgumentParser, ArgumentTypeError, Namespace
from datetime import datetime, timezone, timedelta
from pathlib import Path

assert sys.version_info>=(3,7), "Python version ~=3.7 needed"

def get_date() -> str:
    # https://stackoverflow.com/a/39079819/5059062
    # https://docs.python.org/3/library/datetime.html#datetime.datetime.astimezone
    # https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior
    return datetime.now(
        tz=timezone(
            offset=timedelta(0)
        )
    ).astimezone().strftime("%Y-%m-%dT%H%M%z")

def main(args: Namespace) -> None:
    dt = get_date()
    path = args.path
    new_entry = path/(dt+".md")
    new_entry.touch()

if __name__ == "__main__":
    parser = ArgumentParser(description="Creates a new empty blog entry")
    def non_empty_file(path: str) -> Path:
        path = Path(path)
        if path.is_dir():
            return path
        else:
            raise ArgumentTypeError("PATH needs to be a directory that exists")
    parser.add_argument("-p", "--path", help="Folder in which the new entry will be created", default=Path("."))
    main(parser.parse_args())