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
from logging import getLogger
from threading import Thread
from time import sleep
from typing import Literal
from webbrowser import open as web_open

from click import echo, style
from data import data_factory  # type: ignore[import-not-found]
from endpoints.endpoint_api import endpoint_api  # type: ignore[import-not-found]
from endpoints.endpoint_index import endpoint_index  # type: ignore[import-not-found]
from flask import Flask, Response
from parser import invoke_parser  # type: ignore[import-not-found]
from werkzeug.serving import make_server


def invoke_server(  # noqa: C901
    verbose: Literal[True, False],
    address: str,
    port: int,
    config: dict,
    app_handler: Flask,
    server_only: Literal[True, False],
    interface_only: Literal[True, False],
) -> None:
    app_log = getLogger("werkzeug")
    app_log.disabled = False
    if config["engine"]["web"]["logs"]["enabled"]:
        app_log.setLevel("INFO")
    else:
        app_log.setLevel("ERROR")

    yml_data: dict = invoke_parser(action="parse", verbose=verbose, config=config)
    yml_files: list = invoke_parser(action="parse", verbose=verbose, config=config)
    data_factory(data=yml_data, files=yml_files, verbose=verbose, config=config)

    class ServerThread(Thread):
        def __init__(self, app: Flask) -> None:
            Thread.__init__(self)
            self.server = make_server(host=address, port=port, app=app_handler, ssl_context="adhoc")
            self.ctx = app.app_context()
            self.ctx.push()

        def run(self) -> None:
            if verbose:
                echo(style(text="Verbose: Starting server...", fg="cyan"))
            echo(style(text=f"Web server running on 'https://{address}:{port}'", fg="cyan"))
            self.server.serve_forever()
            return

        def shutdown(self) -> None:
            if verbose:
                echo(style(text="Verbose: Shutting down server...", fg="cyan"))
            self.server.shutdown()
            return

    app_server: ServerThread = ServerThread(app_handler)

    def start_server() -> None:
        @app_handler.route("/")
        def index() -> Response:
            return endpoint_index(address=address, port=port)  # type: ignore[no-any-return]

        @app_handler.route("/api")
        def api() -> Response:
            return endpoint_api()  # type: ignore[no-any-return]

        app_server.start()
        if not server_only:
            web_open(url=f"https://{address}:{port}/")
        return

    def stop_server() -> None:
        app_server.shutdown()
        return

    start_server()
    while True:
        try:
            sleep(0.01)  # TODO: implement interactive UI logic from this point on
        except KeyboardInterrupt:
            stop_server()
            break
    sleep(0.01)  # Fixes some weird echo() behavior near the closing of the program.
    return
