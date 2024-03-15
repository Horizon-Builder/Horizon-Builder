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
# from threading import Thread
from collections.abc import Callable
from typing import Any, Literal, Union

from click import echo, style
from flask import Flask, Response
from flask_socketio import SocketIO  # type: ignore[import-untyped]

from Horizon_Builder.data import data_factory
from Horizon_Builder.endpoints.data import data
from Horizon_Builder.endpoints.index import index
from Horizon_Builder.parser import invoke_parser
from Horizon_Builder.websockets.session import session


def invoke_server(
    verbose: Literal[True, False],
    address: str,
    port: int,
    config: dict,
    app_handler: Flask,
    server_only: Literal[True, False],
) -> Union[tuple[Literal[True], Callable, dict], None]:
    yml_data: dict = invoke_parser(action="parse", verbose=verbose, config=config)
    yml_files: list = invoke_parser(action="list", verbose=verbose, config=config)
    interpreted_data: dict = data_factory(data=yml_data, files=yml_files, verbose=verbose, config=config)

    app_sockets: SocketIO = SocketIO(app_handler, async_mode="gevent")  # type: ignore[no-any-unimported]

    @app_sockets.on(message="session", namespace="/session")
    def test(json: Any) -> Any:
        return session(json=json)

    @app_handler.get(rule="/")
    def _index() -> Union[dict, Response]:
        return index(app_handler=app_handler)

    @app_handler.route(rule="/data/image-handler/<image-id>", methods=["GET", "PATCH"])
    def _data(image_id: str) -> Union[dict, Response]:
        return data(app_handler=app_handler, action="Image_handler", image_id=image_id)

    def start_server() -> None:
        echo(
            style(
                text=f"Info: WebSockets server running on 'wss://{address}:{port}'.",
                fg="green",
            )
        )
        echo(
            style(
                text=f"Info: HTTP server running on 'http://{address}:{port}'.",
                fg="green",
            )
        )

        app_sockets.run(host=address, port=port, app=app_handler)
        return

    def stop_servers() -> None:
        if verbose:
            echo(style(text="Verbose: Servers are exiting...", fg="cyan"))
        app_sockets.stop()
        return

    start_server()
    return True, stop_servers, interpreted_data  # Everything is set up, returning to main.py
