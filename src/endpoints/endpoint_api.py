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
from endpoints.api_actions.action_ping import action_ping  # type: ignore[import-not-found]
from flask import Response, jsonify, request

valid_api_actions = {"ping": action_ping}


def endpoint_api() -> Response:
    action = request.args.get(key="action", type=str)

    if action is None:
        response: dict = {"Error": "No action provided."}
        return jsonify(response)
    elif action in valid_api_actions:
        return valid_api_actions[action]()  # type: ignore[no-any-return]
    else:
        response: dict = {"Error": f"No valid action action found for '{action}'."}  # type: ignore[no-redef]
        return jsonify(response)
