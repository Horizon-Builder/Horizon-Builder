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
from typing import Union

from flask import (
    Flask,
    Response,
)


def index(app_handler: Flask) -> Union[dict, Response]:
    """
    A function that takes in an app_handler parameter of type Flask and returns a Union of dictionary or Response.
    """
    return {"ping": "pong"}  # TODO: Implement logic...
