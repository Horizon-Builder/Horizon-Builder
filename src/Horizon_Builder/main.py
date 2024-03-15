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
from atexit import register
from collections.abc import Callable
from os import makedirs
from os.path import exists
from pathlib import Path as PLPath
from pathlib import PurePath
from platform import system, version
from sys import argv, exit
from time import sleep
from typing import Literal, Optional, Union

from click import (
    FileError,
    Path,
    command,
    echo,
    open_file,
    option,
    style,
)
from flask import Flask
from rich.text import Text
from textual.binding import Binding
from trogon import Trogon, constants, tui
from trogon.trogon import CommandBuilder
from trogon.widgets.about import TextDialog
from yaml import safe_load

from Horizon_Builder.server import invoke_server

app_handler: Flask = Flask("Horizon Builder")
VERSION = "v0.0.1"

# Setup Trogon
constants.APP_TITLE = "Horizon Builder"
Trogon.CSS_PATH = PurePath(PLPath(argv[0]).resolve().parent, PLPath("resources"), PLPath("style.scss"))
CommandBuilder.BINDINGS.remove(Binding(key="ctrl+r", action="close_and_run", description="Close & Run"))
CommandBuilder.BINDINGS.insert(0, Binding(key="ctrl+c", action="close", description="Close"))


class CustomAboutDialog(TextDialog):
    DEFAULT_CSS = """
    TextDialog > Vertical {
        border: thick $primary 50%;
    }
    """

    def __init__(self) -> None:
        title = "About Horizon Builder"
        message = Text.from_markup(
            "by [@click=app.visit('https://github.com/GustavoSchip')]GustavoSchip[/].\n\n"
            "Built with [@click=app.visit('https://github.com/textualize/textual')]Textual[/] "
            "[@click=app.visit('https://github.com/Horizon-Builder/Horizon-Builder')]",
        )
        super().__init__(title, message)


def action_close(self) -> None:
    self.app.exit()


def action_about(self) -> None:
    self.app.push_screen(CustomAboutDialog())


CommandBuilder.action_close_and_run = action_close
CommandBuilder.action_about = action_about


def before_exit() -> None:
    pass  # TODO: Implement a panic save for characters and/or cache.


def check_environment(action: str, config: Optional[dict] = None) -> None:
    if action == "POST" and config is not None:
        folders = [
            config.get("engine", {}).get("plugins", {}).get("plugins_folder"),
            config.get("engine", {}).get("plugins", {}).get("plugins_folder", "") + "/user",
            config.get("engine", {}).get("content", {}).get("content_folder"),
            config.get("engine", {}).get("content", {}).get("content_folder", "") + "/user",
            config.get("engine", {}).get("characters", {}).get("characters_folder"),
            config.get("engine", {}).get("characters", {}).get("characters_folder", "") + "/sheets",
        ]
        try:
            if config.get("engine", {}).get("version") != 1:  # type: ignore[index]
                echo(
                    style(
                        text=f"Error: Unsupported config version '{config.get('engine', {}).get('version').lower()}'.",  # type: ignore[index]
                        fg="red",
                    )
                )
                exit(1)
        except (IndexError, TypeError, AttributeError):
            echo(
                style(
                    text="Fatal: The config version could not be found!",
                    fg="red",
                    blink=True,
                    bold=True,
                )
            )
            exit(1)
        for folder in folders:
            if folder and not exists(folder):
                makedirs(folder)
    elif action == "INIT":
        current_dir = PLPath(argv[0]).resolve().parent
        config_path = current_dir / "config.yml"
        resource_path = current_dir / "resources"
        style_path = resource_path / "style.scss"
        if not resource_path.exists():
            makedirs(resource_path)
        if not style_path.exists():
            with open(style_path, "w+") as f:
                f.write(
                    """* {
  scrollbar-color: $accent-lighten-2 20%;
}

#home-body {
  height: 100%;
  width: 1fr;
}

#home-body-scroll {
  width: 1fr;
  height: 1fr;

}

#home-exec-preview {
  dock: bottom;
  background: $panel-darken-2;
  height: auto;
}

#home-exec-preview-container {
  min-height: 3;
  max-height: 8;
  height: auto;
  scrollbar-size-vertical: 1;
}

#home-exec-button {
  height: 1fr;
  width: auto;
}

#home-exec-preview-static {
  width: 1fr;
  padding: 1 2;
  height: auto;
}

#home-exec-preview-buttons {
  dock: right;
  height: auto;
  width: auto;
}

#home-commands-label {
  color: $text;
  background: $background 50%;
  width: 100%;
  height: 4;
  padding: 1 2;
}

#home-sidebar {
  dock: left;
  width: auto;
}

#home-command-description {
  width: 1fr;
  height: 2;
}

#home-command-description-container {
  dock: top;
  width: 1fr;
  height: 4;
  padding: 1 2;
  color: $text;
  background: $accent-lighten-2 5%;
}

CommandBuilder .version-string {
  color: $text-muted;
  background: $background 50%;
  text-style: italic;
}

CommandBuilder .prompt {
  color: $success;
  background: $background-darken-2;
  text-style: bold;
}

CommandBuilder .command-name-syntax {
  color: $accent-lighten-2;
  background: $panel-darken-2;
  text-style: italic bold;
}

CommandTree {
  background: $background-lighten-1;
  scrollbar-gutter: stable;
  width: auto;
  height: 1fr;
  padding: 0 1;
  margin-bottom: 1;  /* why is this needed? */
  border: blank;
}


CommandTree:focus {
  border: tall $success;
}

CommandTree > .tree--cursor {
  background: $primary-darken-1;
}

CommandTree:focus > .tree--cursor {
  background: $primary-lighten-1;
}

CommandTree > .tree--guides {
  color: slategray;
}

CommandTree .group {
  color: $accent-lighten-2;
  text-style: bold;
}

CommandTree > .tree--guides-selected {
  color: $primary-lighten-2;
}

CommandTree > .tree--guides-hover {
  color: $primary-lighten-2;
}

ParameterControls {
  height: auto;
}

ControlGroup {
  height: auto;
  border: solid $panel-lighten-2;

}

ControlGroup.single-item {
  margin: 0;
  border: none;
}

ControlGroup.single-item:focus-within {
  margin: 0;
  border: none;
}

ControlGroup:focus-within {
  border: solid $primary;
}

ControlGroupsContainer {
  height: auto;
}

Pretty {
  height: auto;
}

.add-another-button {
  margin-right: 1;
  background: transparent;
  color: $success;
  border: none;
  background: $boost;
  height: 1;
 }

.add-another-button:hover {
  background: transparent;
}

.add-another-button-container {
  width: 1fr;
  height: auto;
  align: right top;
}

CommandInfo {
  align: center middle;
}

.command-info-header-text {
  padding: 1 1 0 2;
}

CommandForm .command-form-filter-input {
  margin: 1 2;
}

$command-info-header-bg: $primary-darken-1;

.command-info-header {
  dock: top;
  background: $command-info-header-bg;
  color: $text;
  height: auto;
}

.command-info-container {
  width: 80%;
  height: 60%;
  background: $panel;
}

#command-info-switcher {
  height: auto;
}

.command-info-text {
  padding: 2 4;
  height: auto;
}

.command-info-metadata {
  padding: 2 4;
  height: auto;
}

CommandInfo .title {
  background: $command-info-header-bg;
  text-style: bold;
}

CommandInfo .subtitle {
  background: $command-info-header-bg;
  color: $text-muted;
}

CommandInfo Tab {
  width: 1fr;
}

.command-info-tabs {
  width: 100%;
}

Tabs:focus .underline--bar {
  color: $accent-lighten-1;
}

Select.command-form-select  {

}

Select.command-form-select SelectCurrent {
  border: tall transparent;
}

Select.command-form-select:focus SelectCurrent {
  border: tall $accent;
}

.command-form-multiple-choice {
  margin-left: 0;
  border: tall transparent;
  background: $boost;
  padding: 0 1;
  margin-top: 0;
}

.command-form-multiple-choice:focus-within {

  border: tall $accent;
}
"""
                )
        if not config_path.exists():
            with open(config_path, "w+") as f:
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
    return


@tui(name="Horizon Builder", command="help", help="Open terminal UI.")
@command()
@option("--verbose", "-V", is_flag=True, help="Enable verbose logging.")
@option("--address", "-A", type=str, show_default=True, help="Specify host address.")
@option("--port", "-P", type=int, show_default=True, help="Specify host HTTP port.")
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
    help="Specify config file.",
)
@option("--server-only", "-So", is_flag=True, help="Only run server.")
# ^ Make the server not open connection for outside, and remove/stop protocols related to it
def horizon_builder_cli(  # noqa: C901
    verbose: Literal[True, False],
    address: Union[str, None],
    port: Union[int, None],
    config: PLPath,
    server_only: Literal[True, False],
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
    if server_only:
        echo(style(text="Warning: Server only mode enabled!", fg="yellow"))
    try:
        with open_file(filename=str(config)) as f:
            config = safe_load(f.read())
    except FileError as error:
        echo(style(text=f"Error: {error}! Exiting...", fg="red"))
        exit(1)
    check_environment(action="POST", config=config)  # type: ignore[arg-type]
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

    out, stop_servers, interpreted_data = invoke_server(  # type: ignore[misc]
        verbose=verbose,
        address=address,
        port=port,
        config=config,  # type: ignore[arg-type]
        app_handler=app_handler,
        server_only=server_only,
    )
    if verbose:
        echo(style(text=f"Verbose: Interpreted data: \n{interpreted_data}\n", fg="cyan"))
    if out is True and isinstance(stop_servers, Callable):  # type: ignore[arg-type]
        while True:
            try:
                sleep(0.01)  # TODO: implement interactive UI logic from this point on
            except KeyboardInterrupt:
                stop_servers()
                break
        sleep(0.01)  # Fixes some weird echo() behavior near the closing of the program.
    else:
        echo(style(text="Error: Server encountered problems! Exiting...", fg="red"))
        exit(1)
    return


if __name__ == "__main__":  # pragma: no cover
    register(before_exit)
    check_environment(action="INIT")
    if len(argv) == 1:
        horizon_builder_cli.main(["help"])
    else:
        horizon_builder_cli()
