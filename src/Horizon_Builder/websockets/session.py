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
from uuid import uuid1

from flask_socketio import emit  # type: ignore[import-untyped]


def session(json: dict) -> None:
    """
    A function that takes in a JSON object, creates a session ID using uuid1, and emits a server message with the session data.

    Parameters:
    json (dict): A JSON object containing data for the session.

    Returns:
    None
    """
    emit("server", {"session": {"id": str(uuid1()), "data": json}})
    return
