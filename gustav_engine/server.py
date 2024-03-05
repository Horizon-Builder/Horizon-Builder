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
from typing import Literal

from click import echo, style
from flask import Flask
from parser import invoke_parser


def invoke_server(
    verbose: Literal[False] | Literal[True], address: str, port: int, config: dict, app_handler: Flask
) -> None:
    if verbose:
        echo(style(text="Verbose: Invoking parser...", fg="cyan"))
    invoke_parser(verbose=verbose, config=config, app_handler=app_handler)
    return
