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
#
from textual.app import App, ComposeResult
from textual.widgets import Footer


class Interface(App):
    BINDINGS = [
        ("ctrl+q", "quit", "Quit"),
    ]

    def __init__(self, context: dict) -> None:
        super().__init__()
        self.context = context

    def compose(self) -> ComposeResult:
        yield Footer()

    async def on_mount(self) -> None:
        pass

    def action_quit(self) -> None:
        self.app.exit(result=None, return_code=0)
