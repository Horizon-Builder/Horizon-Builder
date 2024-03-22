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
#
from os import getcwd
from pathlib import Path as PLPath, PurePath
from sys import exit
from typing import Literal, Union

from auto_click_auto import enable_click_shell_completion
from auto_click_auto.constants import ShellType
from click import command, option, Path, open_file, style
from textual import log
from trogon import tui
from yaml import safe_load

from horizon_builder.cli.context import Context
from horizon_builder.cli.tui.app import Interface
from horizon_builder.data.config import get_config
from horizon_builder.data.content.parser import parse_files
from horizon_builder.data.manager.check import initialize_environment


@tui(name="horizon_builder", command="tui-help")
@command(name="start", context_settings={"ignore_unknown_options": True})
@option(
    "--config",
    type=Path(
        exists=True,
        readable=True,
        dir_okay=False,
        file_okay=True,
        resolve_path=True,
        path_type=PLPath,
    ),
    help="The config file to use.",
)
@option("--verbose", "-v", is_flag=True, help="Enable verbose mode.")
def horizon_builder_cli(
    config: Union[PLPath, None],
    verbose: Literal[True, False],
) -> None:
    try:
        enable_click_shell_completion(
            program_name="horizon_builder",
            shells={ShellType.BASH, ShellType.ZSH, ShellType.FISH},
            verbose=verbose,
        )
    except NotImplementedError as error:
        if verbose:
            log.warning(style(text=f"{error}!", fg="yellow"))
    kwargs: dict = {}
    if config is None:
        try:
            with open_file(
                filename=str(PurePath(PLPath(getcwd()), PLPath("config.yml"))),
                mode="r",
                encoding="utf-8",
            ) as f:
                kwargs["pre-config"] = safe_load(f.read())
        except FileNotFoundError:
            try:
                with open_file(
                    filename=str(
                        PurePath(
                            PurePath(PLPath(__file__)).parents[1], PLPath("config.yml")
                        )
                    ),
                    mode="r",
                    encoding="utf-8",
                ) as f:
                    kwargs["pre-config"] = safe_load(f.read())
            except FileNotFoundError:
                log.error(
                    style(text="Internal config not found! Aborting...", fg="red")
                )
                exit(1)
    elif isinstance(config, (PLPath, Path)):
        with open_file(filename=str(config), encoding="utf-8") as f:
            kwargs["pre-config"] = safe_load(f.read())
    else:
        log.error(style(text="No config file provided! Aborting...", fg="red"))
        exit(1)
    kwargs["verbose"] = verbose
    kwargs["config"] = get_config(config=kwargs["pre-config"])
    initialize_environment(kwargs["config"])
    kwargs["data"] = parse_files(content_folder=kwargs["config"].content.content_folder)
    app: Interface = Interface(context=Context(**kwargs))
    app.run()
    return
