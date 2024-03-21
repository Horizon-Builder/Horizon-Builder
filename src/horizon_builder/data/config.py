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
from click import style
from pydantic import ValidationError
from textual import log

from horizon_builder.data.manager.models import Config


def get_config(config: dict) -> Config:
    engine_config = config.get("engine", {})
    if engine_config.get("version", 0) != 1:
        log.error(style(text="Only version 1 is supported! Aborting...", fg="red"))
        exit(1)
    try:
        processed_config = Config(**engine_config)
    except (ValidationError, AttributeError) as error:
        log.error(style(text=f"{error}! Aborting...", fg="red"))
        exit(1)
    return processed_config
