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
from os import listdir
from pathlib import Path, PurePath
from typing import Literal, Union

from click import FileError, echo, open_file, style
from yaml import safe_load


def invoke_parser(action: str, verbose: Literal[True, False], config: dict) -> Union[dict, list]:  # type: ignore[return]
    files_to_parse: list = []
    yml_dict: dict = {}
    if action == "parse":
        for file in listdir(PurePath(config["engine"]["content"]["content_folder"])):
            if (
                str(file).endswith(".yml")
                and PurePath(config["engine"]["content"]["content_folder"], Path(file)) not in files_to_parse
            ):
                files_to_parse.append(PurePath(config["engine"]["content"]["content_folder"], Path(file)))
        for yml_file in files_to_parse:
            if verbose:
                echo(
                    style(
                        text=f"Verbose: Trying to parse contents of '{yml_file}'.",
                        fg="cyan",
                    )
                )
            try:
                with open_file(filename=str(yml_file), encoding="utf-8") as f:
                    parsed_yml = safe_load(stream=f.read())
                    yml_dict[str(yml_file.name)] = parsed_yml
            except (FileError, ValueError) as error:
                echo(style(text=f"Error: {error}! Skipping...", fg="red"))
                continue
        return yml_dict
    elif action == "list":
        return files_to_parse
