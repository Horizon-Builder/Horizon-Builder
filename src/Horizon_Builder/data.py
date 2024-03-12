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
from typing import Literal

from click import echo, style

from Horizon_Builder.models import (
    Armor,
    ArmorCategory,
    Background,
    BackgroundFeature,
    Character,
    Class,
    ClassFeature,
    Damage,
    DieRoll,
    Feat,
    FeatFeature,
    Grant,
    Language,
    MagicArmor,
    MagicWeapon,
    Proficiency,
    Property,
    Race,
    RaceFeature,
    Selection,
    Skill,
    Spell,
    Spellcasting,
    Stat,
    SubClass,
    SubRace,
    VariantRace,
    Vision,
    Weapon,
    WeaponCategory,
)


class DataStorage:
    def __init__(self) -> None:
        self.data = []
        self.cls = [
            Grant,
            Selection,
            DieRoll,
            Property,
            Stat,
            Skill,
            Damage,
            Spell,
            Spellcasting,
            Proficiency,
            Weapon,
            WeaponCategory,
            MagicWeapon,
            Armor,
            ArmorCategory,
            MagicArmor,
            Vision,
            Language,
            BackgroundFeature,
            Background,
            FeatFeature,
            Feat,
            RaceFeature,
            Race,
            SubRace,
            VariantRace,
            ClassFeature,
            Class,
            SubClass,
            Character,
        ]

    def add_data(self, json_input: dict, name: str) -> None:
        if json_input["type"] in [cls.__name__ for cls in self.cls]:
            class_obj = next(cls for cls in self.cls if cls.__name__ == json_input["type"])
            if class_obj:  # noqa: SIM102
                if any(attr in json_input for attr in class_obj.__annotations__):
                    json_input["name"] = name
                    json_input.pop("type")
                    if json_input.get("parent", None) is not None:  # TODO: Fix parent syntax
                        parent_class = next(cls for cls in self.cls if cls.__name__ == json_input["parent"])
                        if parent_class:
                            json_input["parent"] = parent_class(**json_input["parent"])
                        else:
                            json_input.pop("Parent")
                    instance = class_obj(**json_input)
                    self.data.append(instance)
        else:
            echo(style(text=f"Error: Type '{json_input['type']}' not supported! Skipping...", fg="red"))

    def get_all_data(self) -> list:
        return self.data


def data_factory(data: dict, files: list, verbose: Literal[True, False], config: dict) -> list:
    storage = DataStorage()
    for file in files:
        if verbose:
            echo(style(text=f"Verbose: Trying to process contents of '{file}'.", fg="cyan"))
        data: dict = data[file]
        if data.get("engine", {}).get("encoding").lower() != "utf-8":
            echo(
                style(
                    text=f"Error: Unsupported encoding '{data['engine']['encoding'].lower()}'.",
                    fg="red",
                )
            )
            continue
        else:
            for element in data["elements"]:
                element_data: dict = data["elements"][element]
                storage.add_data(json_input=element_data, name=element)
    return storage.get_all_data()
