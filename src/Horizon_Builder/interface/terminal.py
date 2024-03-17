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
from pathlib import Path, PurePath
from sys import argv

from textual.app import App, ComposeResult
from textual.widgets import Footer


class HorizonBuilder(App):
    """
    TODO: Write docstring
    """

    CSS_PATH = PurePath(Path(argv[0]).resolve().parent, Path("resources"), Path("style.scss"))

    def __init__(self, config: dict, interpreted_data: dict) -> None:
        """
        TODO: Write docstring...
        """
        self.config: dict = config
        self.data: dict = interpreted_data
        return

    def compose(self) -> ComposeResult:
        """
        TODO: Write docstring...
        """
        yield Footer()


def terminal_ui(config: dict, interpreted_data: dict) -> None:
    """
    TODO: Write docstring...
    """
    HorizonBuilder(config=config, interpreted_data=interpreted_data).run()
    return
