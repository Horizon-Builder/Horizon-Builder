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
from os import listdir
from pathlib import Path, PurePath
from typing import Literal

from click import echo, style
from defusedxml.ElementTree import parse  # type: ignore[import-untyped]


class XMLError(Exception):
    def __init__(self, message: str, error: Exception) -> None:
        super().__init__(message)
        self.exception = error  # TODO: update exception


def invoke_parser(verbose: Literal[False] | Literal[True], config: dict) -> any:
    files_to_parse = []
    xml_dict = {}
    if verbose:
        echo(style(text="Verbose: Loading XML contents...", fg="cyan"))
    try:
        for file in listdir(PurePath(config["engine"]["content_folder"])):
            if str(file).endswith(".xml"):
                files_to_parse.append(PurePath(config["engine"]["content_folder"], Path(file)))
        for xml_file in files_to_parse:
            parsed_xml = parse(source=xml_file, forbid_dtd=True)
            parsed_xml_root = parsed_xml.getroot()
            if parsed_xml_root.tag == "elements" and parsed_xml_root.attrib == {}:
                for element in parsed_xml_root.iter("element"):  # noqa: B007
                    pass
                for child in element.iter():  # noqa: B007
                    pass
    except Exception as error:
        if verbose:
            echo(style(text=f"Verbose: XML Data: {xml_dict}", fg="cyan"))
        raise XMLError(message=f"{error}", error=error)  # noqa: B904 TRY200
    return xml_dict
