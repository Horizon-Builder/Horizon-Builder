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
from defusedxml.ElementTree import parse
from flask import Flask


def invoke_parser(verbose: Literal[False] | Literal[True], config: dict, app_handler: Flask) -> None:
    if verbose:
        echo(style(text="Verbose: Loading XML contents...", fg="cyan"))
    for xml_file in listdir(PurePath(config["engine"]["content_folder"])):
        if xml_file.endswith(".xml"):
            parsed_xml = parse(source=PurePath(config["engine"]["content_folder"], Path(xml_file)), forbid_dtd=True)
            parsed_xml_root = parsed_xml.getroot()
            if parsed_xml_root.tag == "elements" and parsed_xml_root.attrib == {}:
                for element in parsed_xml_root.iter("element"):
                    for child in element.iter():
                        if verbose:
                            echo(
                                style(
                                    text=f"Debug: {parsed_xml_root.tag} {element.tag} {element.attrib} {child.tag} {child.attrib} {child.text}",
                                    fg="green",
                                )
                            )
    return
