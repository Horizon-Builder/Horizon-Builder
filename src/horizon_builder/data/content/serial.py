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
from typing import Type, Optional

from click import style
from pydantic import BaseModel, ValidationError
from textual import log

from horizon_builder.data.content.models import Class

prefix_to_model: dict[str, Type[BaseModel]] = {"ID_CLASS_": Class}
model_to_dict: dict[Type[BaseModel], dict] = {
    Class: {},
}


def new_class(class_data: Class) -> None:
    return


def initialize_content(
    serial_dict: dict, content_files: Optional[list] = None
) -> dict[Type[BaseModel], dict]:
    if isinstance(content_files, list):
        for file in content_files:
            try:
                for key, value in serial_dict[file].items():
                    for prefix, model in prefix_to_model.items():
                        try:
                            if key.startswith(prefix):
                                model_to_dict[model][key[len(prefix) :]] = model(
                                    **value
                                ).model_dump()
                                break
                        except (
                            ValidationError,
                            AttributeError,
                            IndexError,
                            KeyError,
                        ) as error:
                            log.warning(
                                style(
                                    text=f"{error}! Skipping...",
                                    fg="yellow",
                                )
                            )
                            continue
            except (KeyError, AttributeError) as error:
                log.warning(
                    style(
                        text=f"{error}! Skipping...",
                        fg="yellow",
                    )
                )
                continue
    else:
        for key, value in serial_dict.items():
            for prefix, model in prefix_to_model.items():
                try:
                    if key.startswith(prefix):
                        model_to_dict[model][key[len(prefix) :]] = model(
                            **value
                        ).model_dump()
                        break
                except (
                    ValidationError,
                    AttributeError,
                    IndexError,
                    KeyError,
                ) as error:
                    log.warning(
                        style(
                            text=f"{error}! Skipping...",
                            fg="yellow",
                        )
                    )
                    continue
    return model_to_dict
