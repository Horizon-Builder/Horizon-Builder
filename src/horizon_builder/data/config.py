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
from os import PathLike
from typing import Union

from pydantic import BaseModel


class Config(BaseModel):
    version: int
    content_folder: Union[str, PathLike]
    characters_folder: Union[str, PathLike]
    plugins_folder: Union[str, PathLike]
    plugin_mode: bool


def get_config(config: dict) -> Config:
    version: int = config.get("engine", {}).get("version", 0)
    if version != 1:
        raise NotImplementedError("Only version 1 is supported!")
    kwargs = {
        "version": version,
        "content_folder": config.get("engine", {})
        .get("content", {})
        .get("content_folder", ""),
        "characters_folder": config.get("engine", {})
        .get("characters", {})
        .get("characters_folder", ""),
        "plugins_folder": config.get("engine", {})
        .get("plugins", {})
        .get("plugins_folder", ""),
        "plugin_mode": config.get("engine", {})
        .get("plugins", {})
        .get("enabled", False),
    }
    processed_config = Config(**kwargs)
    return processed_config
