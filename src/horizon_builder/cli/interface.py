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
from pathlib import Path as PLPath, PurePath
from sys import exit
from typing import Literal, Union

from click import command, option, Path, argument
from loguru import logger
from trogon import tui
from yaml import safe_load

from .tui import Interface


@logger.catch()
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
@argument("other", nargs=-1, add_help_option=False)
def horizon_builder_cli(
    config: Union[PLPath, None],
    verbose: Literal[True, False],
    other: Union[tuple, None],
) -> None:
    if other is not None:
        if len(other) > 0:
            horizon_builder_cli(["tui-help"])
    context: dict = {}
    if config is None:
        try:
            with open(
                file=PurePath(PLPath(__file__).parent.parent, PLPath("config.yml")),
                mode="r",
            ) as f:
                context["config"] = safe_load(f.read())
        except FileNotFoundError:
            logger.critical("Internal config not found! Aborting.")
            exit(1)
    elif isinstance(config, PLPath):
        context["config"] = safe_load(config.read())
    else:
        logger.error("No config file provided! Aborting.")
        exit(1)
    context["verbose"] = verbose
    app = Interface(context=context)
    app.run()
    return
