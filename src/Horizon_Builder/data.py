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
from typing import Literal

from click import echo, style


def parse_weapon(element_data: dict) -> dict:
    # Define required and optional attributes
    required_attributes = ["category", "proficiency", "damage"]
    optional_attributes = ["description", "properties", "weight"]

    # Check for required attributes
    for attributes in required_attributes:
        if attributes not in element_data:
            raise ValueError(f"Error: Missing required attribute '{attributes}' in subclass element")  # noqa: TRY003

    # Check for optional attributes
    for attributes in optional_attributes:
        if attributes not in element_data:
            element_data[attributes] = None

    return element_data


def data_factory(data: dict, files: list, verbose: Literal[True, False], config: dict) -> dict:
    valid_entries: dict = {
        "weapon": parse_weapon  # TODO: Add more types...
    }
    parsed_elements = {}
    for file in files:
        if verbose:
            echo(style(text=f"Verbose: Trying to process contents of '{file}'.", fg="cyan"))
            data: dict = data[file]  # type: ignore[no-redef]
            if data.get("engine", {}).get("encoding").lower() != "utf-8":
                echo(
                    style(
                        text=f"Error: Unsupported encoding '{data['engine']['encoding'].lower()}'.",
                        fg="red",
                    )
                )
                continue
            else:
                data: dict = data.get("elements", {})  # type: ignore[no-redef]
                for element_name, element_data in data.items():
                    if "type" in element_data:
                        element_type = element_data["type"]
                        if element_type in valid_entries:
                            parsed_element = valid_entries[element_type](element_data)
                            parsed_elements[element_name] = parsed_element
                        else:
                            echo(
                                style(
                                    text=f"Error: Unsupported element '{element_type}'! Skipping...",
                                    fg="red",
                                )
                            )
                            continue
                    else:
                        echo(
                            style(
                                text="Error: No element type has been given! Skipping...",
                                fg="red",
                            )
                        )
                        continue

    return parsed_elements
