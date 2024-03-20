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

from click import command, option, Path, open_file
from textual import log
from trogon import tui
from yaml import safe_load

from horizon_builder.cli.tui import Interface
from horizon_builder.data import parse_files
from horizon_builder.data.config import get_config


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
    context: dict = {}
    if config is None:
        try:
            with open(
                file=PurePath(PLPath(__file__).parent.parent, PLPath("config.yml")),
                mode="r",
            ) as f:
                context["config"] = safe_load(f.read())
        except FileNotFoundError:
            log.critical(msg="Internal config not found! Aborting.")
            exit(1)
    elif isinstance(config, (PLPath, Path)):
        with open_file(filename=str(config), encoding="utf-8") as f:
            context["config"] = safe_load(f.read())
    else:
        log.error(msg="No config file provided! Aborting.")
        exit(1)
    context["verbose"] = verbose
    context["config"] = get_config(config=context["config"])
    context["parsed_files"] = parse_files(verbose=verbose, content_folder="")
    app: Interface = Interface(context=context)
    app.run()
    return
