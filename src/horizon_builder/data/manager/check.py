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
from os import PathLike, makedirs, getcwd
from os.path import exists
from pathlib import PurePath, Path
from typing import Union

from click import open_file, FileError, style
from textual import log

from horizon_builder.data.manager.models import Config


def check(
    entries: Union[list[Union[PathLike, PurePath, str]], dict[PurePath, str]]
) -> Union[list[PurePath], dict[PurePath, str]]:
    if isinstance(entries, list):
        to_create: list = []
        for path in entries:
            if not exists(path):
                to_create.append(path)
    elif isinstance(entries, dict):
        to_create: dict = {}  # type: ignore[no-redef]
        for path, content in entries.items():
            if not exists(path):
                to_create[path] = content  # type: ignore[call-overload]
    else:
        raise TypeError(
            style(text="Invalid type for entries in check!", fg="red")
        )  # TODO: Better error...
    return to_create


def create_folders(folders: list[PurePath]) -> None:
    for folder in folders:
        makedirs(name=folder, exist_ok=True)
    return


def create_files(files: dict[PurePath, str]) -> None:
    for file, content in files.items():
        with open_file(filename=str(file), mode="w+", encoding="utf-8") as f:
            f.write(files.get(file, content))
    return


def initialize_environment(config: Config) -> None:
    try:
        working_directory: Path = Path(getcwd())
        required_folders: list = [
            PurePath(working_directory) / config.content.content_folder,
            PurePath(working_directory) / config.characters.characters_folder,
            PurePath(working_directory) / config.plugins.plugins_folder,
        ]
        files_relative: list[str] = [
            "config.yml",
        ]
        required_files: dict = {
            str(working_directory / files_relative[0]): "",
        }
        x: int = 0
        for file_path in required_files:
            with open_file(
                filename=str(
                    PurePath(
                        Path(__file__).parents[2],
                        Path(files_relative[x]),
                    )
                ),
                mode="r",
                encoding="utf-8",
            ) as f:
                required_files[file_path] = str(f.read())
                x += 1
        checked_folders: list = check(required_folders)  # type: ignore[assignment]
        checked_files: dict = check(required_files)  # type: ignore[assignment]
        create_folders(checked_folders)
        create_files(checked_files)
    except (FileError, TypeError) as error:
        log.error(style(text=f"{error}! Aborting...", fg="red"))
        exit(1)
    return
