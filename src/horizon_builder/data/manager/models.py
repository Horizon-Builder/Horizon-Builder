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

from pydantic import BaseModel, ConfigDict


class Content(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)
    content_folder: Union[str, PathLike[str]]


class Characters(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)
    characters_folder: Union[str, PathLike[str]]


class Plugins(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)
    plugins_folder: Union[str, PathLike[str]]
    enabled: bool


class Config(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)
    version: int
    content: Content
    characters: Characters
    plugins: Plugins
