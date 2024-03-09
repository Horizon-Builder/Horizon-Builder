#   Copyright 2024 GustavoSchip
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
from typing import Literal, Union

from click import FileError, Path, command, echo, open_file, option, style
from flask import Flask
from server import invoke_server  # type: ignore[import-not-found]
from yaml import safe_load

app_handler = Flask("Horizon Builder")
VERSION = "v0.0.1"


@command()
@option("--verbose", "-V", is_flag=True, help="Enable verbose logging.")
@option("--address", "-A", type=str, show_default=True, help="Specify the host address.")
@option("--port", "-P", type=int, show_default=True, help="Specify the host port.")
@option(
    "--config",
    "-C",
    default="config.yml",
    type=Path(exists=True, readable=True, file_okay=True, dir_okay=False, resolve_path=True, path_type=PLPath),
    show_default=True,
    help="Specify the config file.",
)
@option("--server-only", "-So", is_flag=True, help="Only run the server.")
@option("--interface-only", "-Io", is_flag=True, help="Only run the interface.")
def cli(  # noqa: C901
    verbose: Literal[True, False],
    address: Union[str, None],
    port: Union[int, None],
    config: PLPath,
    server_only: Literal[True, False],
    interface_only: Literal[True, False],
) -> None:
    """Horizon Builder

    Attempt at a DnD 5e Character builder inspired by Aurora Builder.
    """
    echo(style(text=f"Gustav-Engine: Running version '{VERSION}' on {system()} {version()}.\n", fg="magenta"))
    if verbose:
        echo(style(text="Warning: Verbose logging enabled!", fg="yellow"))
    if interface_only:
        echo(style(text="Warning: Interface only mode enabled!", fg="yellow"))
    if server_only:
        echo(style(text="Warning: Server only mode enabled!", fg="yellow"))
    if server_only and interface_only:
        echo(style(text="Error: Server only mode and interface mode are both enabled!", fg="red"))
        exit(1)
    try:
        with open_file(filename=str(config)) as f:
            config = safe_load(f.read())
    except FileError as error:
        echo(style(text=f"Error: {error}! Exiting...", fg="red"))
        exit(1)
    if address is None:
        try:
            address = str(config["engine"]["web"]["address"])  # type: ignore[index]
        except KeyError:
            echo(style(text="Error: Address not configured! Exiting...", fg="red"))
            exit(1)
    if port is None:
        try:
            port = int(config["engine"]["web"]["port"])  # type: ignore[index]
        except KeyError:
            echo(style(text="Error: Port not configured! Exiting...", fg="red"))
            exit(1)
    if verbose:
        echo(style(text=f"Verbose: Host set to '{address}:{port}'.", fg="cyan"))

    invoke_server(
        verbose=verbose,
        address=address,
        port=port,
        config=config,
        app_handler=app_handler,
        server_only=server_only,
        interface_only=interface_only,
    )
    return


if __name__ == "__main__":  # pragma: no cover
    if len(argv) == 1:
        cli.main(["--help"])
    else:
        cli()
