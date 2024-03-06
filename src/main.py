#   Copyright [2024] [GustavoSchip]
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
from pathlib import Path as PLPath
from platform import system, version
from sys import argv, exit
from typing import Literal

from click import FileError, Path, command, echo, open_file, option, style
from flask import Flask
from server import invoke_server
from yaml import safe_load

app_handler = Flask("Gustav-Engine")
VERSION = "v0.0.1"


@command()
@option("--verbose", "-v", is_flag=True, help="Enable verbose logging.")
@option("--address", "-a", type=str, show_default=True, help="Specify the host address.")
@option("--port", "-p", type=int, show_default=True, help="Specify the host port.")
@option(
    "--config",
    "-c",
    default="config.yml",
    type=Path(exists=True, readable=True, file_okay=True, dir_okay=False, resolve_path=True, path_type=PLPath),
    show_default=True,
    help="Specify the config file.",
)
def cli(verbose: Literal[False] | Literal[True], address: str | None, port: int | None, config: PLPath) -> None:
    """Gustav-Engine

    Attempt at a DnD 5e Character builder inspired by Aurora Builder.
    """
    echo(style(text=f"Gustav-Engine: Running version '{VERSION}' on {system()} {version()}.\n", fg="magenta"))
    if verbose:
        echo(style(text="Warning: Verbose logging enabled!", fg="yellow"))
    try:
        with open_file(filename=str(config)) as f:
            config = safe_load(f.read())
    except FileError as error:
        echo(style(text=f"Error: {error}! Exiting...", fg="red"))
        exit(1)
    if address is None:
        try:
            address = str(config["engine"]["address"])
        except KeyError:
            echo(style(text="Error: Address not configured! Exiting...", fg="red"))
            exit(1)
    if port is None:
        try:
            port = int(config["engine"]["port"])
        except KeyError:
            echo(style(text="Error: Port not configured! Exiting...", fg="red"))
            exit(1)
    if verbose:
        echo(style(text=f"Verbose: Host set to 'http://{address}:{port}'", fg="cyan"))

    if verbose:
        echo(style(text="Verbose: Invoking server...", fg="cyan"))
    invoke_server(
        verbose=verbose,
        address=address,
        port=port,
        config=config,  # type: ignore[arg-type]
        app_handler=app_handler,
    )
    return


if __name__ == "__main__":  # pragma: no cover
    if len(argv) == 1:
        cli.main(["--help"])
    else:
        cli()
