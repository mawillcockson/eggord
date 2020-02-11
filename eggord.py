import sys
from argparse import ArgumentParser, ArgumentTypeError, Namespace
from datetime import datetime, timezone, timedelta
from pathlib import Path
from subprocess import run

assert sys.version_info>=(3,7), "Python version ~=3.7 needed"

def set_clipboard(string: str) -> None:
    if not isinstance(string, str):
        raise TypeError("string needs to be a str")
    run(args="", executable="C:\WINDOWS\system32\clip.exe", input=string, text=True)

def get_date() -> str:
    # https://stackoverflow.com/a/39079819/5059062
    # https://docs.python.org/3/library/datetime.html#datetime.datetime.astimezone
    # https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior
    return datetime.now(
        tz=timezone(
            offset=timedelta(0)
        )
    ).astimezone().strftime("%Y-%m-%dT%H%M%z")

def new_blog(path: Path) -> Path:
    if not isinstance(path, Path) or not path.is_dir():
        raise TypeError("'path' must be a pathlib.Path pointing to a directory")
    dt = get_date()
    new_entry = path/(dt+".md")
    new_entry.touch()
 
def date_to_clipboard() -> None:
    set_clipboard(get_date())

def main(args: Namespace) -> None:
    if args.path:
        new_blog(path)
    else:
        date_to_clipboard()
    
if __name__ == "__main__":
    parser = ArgumentParser(description="Generates my preferred ISO dates")
    def str_to_dir(path: str) -> Path:
        path = Path(path)
        if path.is_dir():
            return path
        else:
            raise ArgumentTypeError("PATH needs to be a directory that exists")
    parser.add_argument("-p", "--path", type=str_to_dir, help="Folder in which the new entry will be created")
    main(parser.parse_args())