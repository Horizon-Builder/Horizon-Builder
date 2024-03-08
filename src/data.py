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

# TODO: Implement without '*'
# from models import *  # type: ignore[import-not-found]


def data_factory(data: dict, files: list, verbose: Literal[True, False], config: dict) -> None:
    if config["engine"]["content"]["type"].lower() != "yml":
        echo(style(text=f"Error: Unsupported content type '{config['engine']['content']['type'].lower()}'.", fg="red"))
        return
    for file in files:
        if verbose:
            echo(style(text=f"Verbose: Trying to process contents of '{file}'", fg="cyan"))
        data = data[file]
        if data["engine"]["encoding"].lower() != "utf-8":
            echo(style(text=f"Error: Unsupported encoding '{data['engine']['encoding'].lower()}'.", fg="red"))
            continue
        else:
            pass  # TODO: Implement this...
    return
