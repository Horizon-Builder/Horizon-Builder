from os import listdir
from pathlib import Path, PurePath
from typing import Literal

from click import echo
from defusedxml.ElementTree import parse
from flask import Flask


def invoke_parser(verbose: Literal[False] | Literal[True], config: dict, app_handler: Flask) -> None:
    if verbose:
        echo("Verbose: Load XML content...")
    for xml_file in listdir(PurePath(config["engine"]["content_folder"])):
        if xml_file.endswith(".xml"):
            parsed_xml = parse(source=PurePath(config["engine"]["content_folder"], Path(xml_file)), forbid_dtd=True)
            parsed_xml_root = parsed_xml.getroot()
            if parsed_xml_root.tag == "elements" and parsed_xml_root.attrib == {}:
                for element in parsed_xml_root.iter("element"):
                    for child in element.iter():
                        echo(
                            f"{parsed_xml_root.tag} {element.tag} {element.attrib} {child.tag} {child.attrib} {child.text}"
                        )
    return
