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
from collections.abc import Callable
from os import mkdir
from os.path import exists
from pathlib import Path as PLPath
from pathlib import PurePath
from platform import system, version
from sys import argv, exit
from time import sleep
from typing import Literal, Optional, Union

from click import FileError, Path, command, echo, open_file, option, style
from flask import Flask
from yaml import safe_load

from Horizon_Builder.server import invoke_server  # type: ignore[import-not-found]

app_handler: Flask = Flask("Horizon Builder")
VERSION = "v0.0.1"


def check_environment(action: str, config: Optional[dict] = None) -> None:  # noqa: C901
    files = ["config.yml"]
    folders = [
        "plugins" "plugins/user",
        "content",
        "content/user",
        "characters",
        "characters/sheets",
    ]
    if action == "POST":
        if config["engine"]["version"] != 1:
            echo(
                style(
                    text=f"Error: Unsupported config version '{config['engine']['version'].lower()}'.",
                    fg="red",
                )
            )
            exit(1)
        for folder in folders:
            if folder == folders[0]:
                if not exists(str(config["engine"]["plugins"]["plugins_folder"])):
                    mkdir(str(config["engine"]["plugins"]["plugins_folder"]))
            elif folder == folders[1]:
                if not exists(
                    str(
                        PurePath(
                            PLPath(config["engine"]["plugins"]["plugins_folder"]),
                            PLPath("user"),
                        )
                    )
                ):
                    mkdir(
                        str(
                            PurePath(
                                PLPath(config["engine"]["plugins"]["plugins_folder"]),
                                PLPath("user"),
                            )
                        )
                    )
            elif folder == folders[2]:
                if not exists(str(config["engine"]["content"]["content_folder"])):
                    mkdir(str(config["engine"]["content"]["content_folder"]))
            elif folder == folders[3]:
                if not exists(
                    str(
                        PurePath(
                            PLPath(config["engine"]["content"]["content_folder"]),
                            PLPath("user"),
                        )
                    )
                ):
                    mkdir(
                        str(
                            PurePath(
                                PLPath(config["engine"]["content"]["content_folder"]),
                                PLPath("user"),
                            )
                        )
                    )
            elif folder == folders[4]:
                if not exists(str(config["engine"]["characters"]["characters_folder"])):
                    mkdir(str(config["engine"]["characters"]["characters_folder"]))
            elif folder == folders[5]:  # noqa: SIM102
                if not exists(
                    str(
                        PurePath(
                            PLPath(config["engine"]["characters"]["characters_folder"]),
                            PLPath("sheets"),
                        )
                    )
                ):
                    mkdir(
                        str(
                            PurePath(
                                PLPath(config["engine"]["characters"]["characters_folder"]),
                                PLPath("sheets"),
                            )
                        )
                    )
    elif action == "INIT":
        for file in files:
            if not exists(str(PurePath(PLPath(argv[0]).resolve().parent, PLPath(file)))):
                with open(str(PurePath(PLPath(argv[0]).resolve().parent, PLPath(file))), "a+") as f:
                    f.write(
                        """engine:
  version: 1
  content:
    content_folder: ./content/
  characters:
    characters_folder: ./characters/
  plugins:
    plugins_folder: ./plugins/
    enabled: false
  web:
    address: 127.0.0.1
    port: 80"""
                    )
                    f.close()
    return


@command()
@option("--verbose", "-V", is_flag=True, help="Enable verbose logging.")
@option("--address", "-A", type=str, show_default=True, help="Specify the host address.")
@option("--port", "-P", type=int, show_default=True, help="Specify the host HTTP port.")
@option(
    "--config",
    "-C",
    default="config.yml",
    type=Path(
        exists=True,
        readable=True,
        file_okay=True,
        dir_okay=False,
        resolve_path=True,
        path_type=PLPath,
    ),
    show_default=True,
    help="Specify the config file.",
)
@option("--server-only", "-So", is_flag=True, help="Only run the server.")
@option("--interface-only", "-Io", is_flag=True, help="Only run the interface.")
# ^ Make the server not open connection for outside, and remove/stop protocols related to it
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
    echo(
        style(
            text=f"Gustav-Engine: Running version '{VERSION}' on {system()} {version()}.\n",
            fg="magenta",
        )
    )
    if verbose:
        echo(style(text="Warning: Verbose logging enabled!", fg="yellow"))
    if interface_only:
        echo(style(text="Warning: Interface only mode enabled!", fg="yellow"))
    if server_only:
        echo(style(text="Warning: Server only mode enabled!", fg="yellow"))
    if server_only and interface_only:
        echo(
            style(
                text="Error: Server only mode and interface mode are both enabled!",
                fg="red",
            )
        )
        exit(1)
    try:
        with open_file(filename=str(config)) as f:
            config = safe_load(f.read())
    except FileError as error:
        echo(style(text=f"Error: {error}! Exiting...", fg="red"))
        exit(1)
    check_environment(action="POST", config=config)
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
            echo(style(text="Error: HTTP port not configured! Exiting...", fg="red"))
            exit(1)
    if verbose:
        echo(style(text=f"Verbose: Host set to '{address}'.", fg="cyan"))

    out, stop_servers = invoke_server(
        verbose=verbose,
        address=address,
        port=port,
        config=config,
        app_handler=app_handler,
        server_only=server_only,
        interface_only=interface_only,
    )
    if out is True and isinstance(stop_servers, Callable):  # type: ignore[arg-type]
        while True:
            try:
                sleep(0.01)  # TODO: implement interactive UI logic from this point on
            except KeyboardInterrupt:
                stop_servers()
                break
        sleep(0.01)  # Fixes some weird echo() behavior near the closing of the program.
    else:
        echo(style(text="Error: Server had problems running! Exiting...", fg="red"))
        exit(1)
    return


if __name__ == "__main__":  # pragma: no cover
    check_environment(action="INIT")
    if len(argv) == 1:
        cli.main(["--help"])
    else:
        cli()
