from os.path import exists
from pathlib import Path as PLPath
from platform import system, version
from sys import argv
from typing import Literal

from click import Path, command, echo, open_file, option
from flask import Flask
from server import invoke_server
from yaml import safe_load

app_handler = Flask("Gustav-Engine")
VERSION = "v0.0.1"


@command()
@option("--verbose", "-v", is_flag=True, help="Enable verbose logging.")
@option("--address", "-a", default="127.0.0.1", type=str, show_default=True, help="Specify the host address.")
@option("--port", "-p", default=80, type=int, show_default=True, help="Specify the host port.")
@option(
    "--config",
    "-p",
    default="config.yml",
    type=Path(exists=True, readable=True, file_okay=True, dir_okay=False, resolve_path=True, path_type=PLPath),
    help="Specify the config file.",
)
def cli(verbose: Literal[False] | Literal[True], address: str, port: int, config: Path) -> None:
    """Gustav-Engine

    Attempt at a DnD 5e Character builder inspired by Aurora Builder.
    """
    echo(f"Gustav-Engine: Running version '{VERSION}' on {system()} {version()}.")
    if verbose:
        echo("Verbose logging enabled!")
    if exists(str(config)):
        with open_file(str(config)) as f:
            config = safe_load(f.read())
    else:
        echo("No config file found! Exiting...")
        exit(1)

    if verbose:
        echo("Verbose: Invoking server...")
    invoke_server(verbose=verbose, address=address, port=port, config=config, app_handler=app_handler)
    return


if __name__ == "__main__":  # pragma: no cover
    if len(argv) == 1:
        cli.main(["--help"])
    else:
        cli()
