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
from os import listdir, PathLike
from pathlib import Path, PurePath
from typing import Union

from click import FileError, open_file
from textual import log
from yaml import safe_load


def parse_files(content_folder: Union[str, PathLike[str]]) -> tuple[dict, list]:
    files_to_parse: list = []
    yml_dict: dict = {}
    for file in listdir(PurePath(content_folder)):
        try:
            if (
                str(file).endswith(".yml")
                and PurePath(content_folder, Path(file)) not in files_to_parse
            ):
                files_to_parse.append(PurePath(content_folder, Path(file)))
        except FileNotFoundError as error:
            log.error(f"{error}! Aborting.")
            exit(1)
    for yml_file in files_to_parse:
        try:
            with open_file(filename=str(yml_file), encoding="utf-8") as f:
                parsed_yml: dict = safe_load(stream=f.read())
                yml_dict[str(yml_file.name)] = parsed_yml
        except (FileNotFoundError, FileError, ValueError) as error:
            log.error(f"{error}! Skipping...")
            continue
    return yml_dict, files_to_parse
