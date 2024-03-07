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
from typing import Literal

from click import FileError, echo, open_file, style
from xmltodict import parse  # type: ignore[import-untyped]


def invoke_parser(verbose: Literal[False] | Literal[True], config: dict) -> dict:
    files_to_parse: list = []
    xml_dict: dict = {}
    for file in listdir(PurePath(config["engine"]["content"]["content_folder"])):
        if str(file).endswith(".xml"):
            files_to_parse.append(PurePath(config["engine"]["content"]["content_folder"], Path(file)))
    for xml_file in files_to_parse:
        if verbose:
            echo(style(text=f"Verbose: Trying to parse contents of '{xml_file}'", fg="cyan"))
        try:
            with open_file(filename=str(xml_file), encoding="utf-8") as f:
                parsed_xml = parse(xml_input=f.read())
                xml_dict[str(xml_file.name)] = parsed_xml
        except (FileError, ValueError) as error:
            echo(style(text=f"Error: {error}! Skipping...", fg="red"))
            continue
    return xml_dict
