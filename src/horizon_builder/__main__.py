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
from sys import argv

from horizon_builder.cli import horizon_builder_cli

if __name__ == "__main__":
    if "--help" in argv or len(argv) <= 1:
        horizon_builder_cli(["tui-help"])
    elif argv[1] != "start" and argv[1] != "help":
        horizon_builder_cli(["tui-help"])
    else:
        horizon_builder_cli()
