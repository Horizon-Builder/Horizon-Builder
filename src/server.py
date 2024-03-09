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
from data import data_factory  # type: ignore[import-not-found]
from flask import Flask
from flask_socketio import SocketIO  # type: ignore[import-untyped]
from parser import invoke_parser  # type: ignore[import-not-found]
from websockets.session import session  # type: ignore[import-not-found]


def invoke_server(
    verbose: Literal[True, False],
    address: str,
    port: int,
    config: dict,
    app_handler: Flask,
    server_only: Literal[True, False],
    interface_only: Literal[True, False],
) -> Union[tuple[True, Callable], None]:
    yml_data: dict = invoke_parser(action="parse", verbose=verbose, config=config)
    yml_files: list = invoke_parser(action="parse", verbose=verbose, config=config)
    data_factory(data=yml_data, files=yml_files, verbose=verbose, config=config)

    app_sockets: SocketIO = SocketIO(app_handler, async_mode="gevent", ssl_context="adhoc")  # type: ignore[no-any-unimported]

    @app_sockets.on(message="session", namespace="/")
    def test(json: Any) -> Any:
        return session(json=json)

    def start_server() -> None:
        if verbose:
            echo(
                style(
                    text=f"Verbose: WebSockets running on 'wss://{address}:{port}'.",
                    fg="cyan",
                )
            )
        app_sockets.run(host=address, port=port, app=app_handler)
        return

    def stop_server() -> None:
        if verbose:
            echo(style(text="Verbose: WebSockets are exiting...", fg="cyan"))
        app_sockets.stop()
        return

    start_server()
    return (True, stop_server)  # Everything is set up, returning to main.py
