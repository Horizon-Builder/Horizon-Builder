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
from sys import exit
from threading import Thread
from time import sleep
from typing import Literal

from click import echo, style
from flask import Flask
from parser import XMLError, invoke_parser
from werkzeug.serving import make_server


def invoke_server(  # noqa: C901
    verbose: Literal[False] | Literal[True], address: str, port: int, config: dict, app_handler: Flask
) -> None:
    if verbose:
        echo(style(text="Verbose: Invoking parser...", fg="cyan"))
    try:
        xml_data: dict = invoke_parser(verbose=verbose, config=config)
        if verbose:
            echo(style(text=f"Debug: XML Data: {xml_data}", fg="green"))
    except XMLError as error:
        echo(style(text=f"Error: {error}! Exiting...", fg="red"))
        exit(1)

    class ServerThread(Thread):
        def __init__(self, app: Flask) -> None:
            Thread.__init__(self)
            self.server = make_server(host=address, port=port, app=app_handler)
            self.ctx = app.app_context()
            self.ctx.push()

        def run(self) -> None:
            if verbose:
                echo(style(text="Verbose: Starting server...", fg="cyan"))
            self.server.serve_forever()

        def shutdown(self) -> None:
            if verbose:
                echo(style(text="Verbose: Shutting down server...", fg="cyan"))
            self.server.shutdown()

    app_server: ServerThread = ServerThread(app_handler)

    def start_server() -> None:
        @app_handler.route("/")
        def hello_world() -> str:
            return "<p>Hello, World!</p>"

        app_server.start()
        return

    def stop_server() -> None:
        app_server.shutdown()
        return

    start_server()
    while True:
        try:
            sleep(0.01)
        except KeyboardInterrupt:
            stop_server()
            break
    return
