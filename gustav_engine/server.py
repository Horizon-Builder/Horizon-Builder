from typing import Literal

from click import Path
from flask import Flask


def invoke_server(
    verbose: Literal[False] | Literal[True], address: str, port: int, config: Path, app_handler: Flask
) -> None:
    return
