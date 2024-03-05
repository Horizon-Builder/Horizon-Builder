from typing import Literal

from click import echo
from flask import Flask
from parser import invoke_parser


def invoke_server(
    verbose: Literal[False] | Literal[True], address: str, port: int, config: dict, app_handler: Flask
) -> None:
    if verbose:
        echo("Verbose: Invoking parser...")
    invoke_parser(verbose=verbose, config=config, app_handler=app_handler)
    return
