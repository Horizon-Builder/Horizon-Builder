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

# TODO: Check if json library could be used instead.
from Horizon_Builder.endpoints.data_endpoints.image_handler import image_handler


def data(app_handler: Flask, action: str, **kwargs) -> Union[dict, Response]:  # type: ignore[no-untyped-def]
    valid_actions: dict = {
        "Image_handler": image_handler,  # TODO: Implement more robust endpoints.
    }
    if action in valid_actions:
        return valid_actions[action](app_handler, **kwargs)  # type: ignore[no-any-return]
    else:
        return {"error": 404}
