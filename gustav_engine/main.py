from os.path import exists
from sys import argv
from typing import Literal

from click import Path, command, echo, option
from flask import Flask
from server import invoke_server
from yaml import safe_load

app_handler = Flask("Gustav-Engine")


@command()
@option("--verbose", "-v", is_flag=True, help="Enable verbose logging.")
@option("--address", "-a", default="127.0.0.1", type=str, show_default=True, help="Specify the host address.")
@option("--port", "-p", default=80, type=int, show_default=True, help="Specify the host port.")
@option("--config", "-p", default="~/config.yml", type=Path(), help="Specify the config file.")
def cli(verbose: Literal[False] | Literal[True], address: str, port: int, config: Path) -> None:
    """Gustav-Engine

    Attempt at a DnD 5e Character builder inspired by Aurora Builder.
    """
    if verbose:
        echo("Verbose logging enabled!")
    if exists(config):  # type: ignore[compatible]
        with open(config) as f:  # type: ignore[compatible]
            config = safe_load(f.read())

    invoke_server(verbose, address, port, config, app_handler)
    return


if __name__ == "__main__":  # pragma: no cover
    if len(argv) == 1:
        cli.main(["--help"])
    else:
        cli()
