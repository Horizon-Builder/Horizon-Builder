from typing import Union

from click import Path
from flask import Flask


def invoke_server(verbose: Union[None | False | True], address: str, port: int, config: Path, app_handler: Flask):
    pass
