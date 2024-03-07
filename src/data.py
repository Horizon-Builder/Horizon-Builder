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
from typing import Literal, Optional, Union

from click import echo, style
from pydantic import BaseModel


class Grant(BaseModel):  # TODO: Figure out how to do this
    property: any  # noqa: A003


class Selection(BaseModel):
    name: str
    grants: Optional[list[Grant]]


class DieRoll(BaseModel):
    die_count: int
    die_size: int


class Property(BaseModel):
    name: str
    type: str  # noqa: A003
    description: Optional[str]


class Damage(BaseModel):
    type: Optional[str]  # noqa: A003
    roll: Optional[DieRoll]
    additional: Optional[int]


class Proficiency(BaseModel):
    name: str


class Weapon(BaseModel):
    name: str
    type: list["WeaponCategory"]  # noqa: A003
    proficiency: Optional[Proficiency]
    description: Optional[str]
    damage: Optional[list[Damage]]
    properties: Optional[list[Property]]


class WeaponCategory(BaseModel):  # Simple, Martial, Ranged, Melee, Longsword, exc
    name: str
    description: Optional[str]
    weapons: Optional[list[Union[Weapon | "WeaponCategory"]]]


class MagicWeapon(BaseModel):
    name: str
    parent: list[Union[Weapon | WeaponCategory]]
    description: Optional[str]
    damage: Optional[list[Damage]]
    properties: Optional[list[Property]]
    damage_bonus: Optional[int]
    hit_bonus: Optional[int]


class Armor(BaseModel):
    name: str
    type: list["ArmorCategory"]  # noqa: A003
    proficiency: Optional[Proficiency]
    description: Optional[str]
    armor_class: int
    stealth_disadvantage: bool
    weight: int


class ArmorCategory(BaseModel):  # Light, Medium, Heavy, Shield
    name: str
    description: Optional[str]
    armors: Optional[list[Union[Armor | "ArmorCategory"]]]
    strength_requirement: Optional[int]
    ac_calculation: Optional[str]  # TODO: Figure out how to do this


class MagicArmor(BaseModel):
    name: str
    parent: list[Union[Armor | ArmorCategory]]
    description: Optional[str]
    armor_class: int
    stealth_disadvantage: bool  # Overridden the parent
    ac_calculation: Optional[str]  # Overridden the parent
    weight: int


class Vision(BaseModel):
    name: str
    description: Optional[str]
    distance: int


class Language(BaseModel):
    name: str
    description: Optional[str]


class BackgroundFeature(BaseModel):
    name: str
    description: Optional[str]
    grants: Optional[list[Union[Grant | Selection]]]


class Background(BaseModel):
    name: str
    version: str
    description: Optional[str]
    background_features: Optional[list[BackgroundFeature]]
    languages: Optional[list[Language]]
    grants: Optional[list[Union[Grant | Selection]]]  # Includes proficiencies, feats, etc


class FeatFeature(BaseModel):
    name: str
    description: Optional[str]
    grants: Optional[list[Union[Grant | Selection]]]


class Feat(BaseModel):
    name: str
    description: Optional[str]
    grants: Optional[list[Union[Grant | Selection]]]
    feat_features: Optional[list[FeatFeature]]


class Stat(BaseModel):
    name: str
    value: int
    stat_type: str


class Skill(BaseModel):
    name: str
    calculation: str


class RaceFeature(BaseModel):
    name: str
    description: Optional[str]
    grants: Optional[list[Union[Grant | Selection]]]


class Race(BaseModel):
    name: str
    description: Optional[str]
    subrace = Optional[list["SubRace"]]
    size: str
    speed: int
    vision: Optional[Vision]
    race_features: Optional[list[RaceFeature]]


class SubRace(BaseModel):
    name: str
    description: Optional[str]
    parent: Optional[Race]
    vision: Optional[Vision]
    race_features: Optional[list[RaceFeature]]


class ClassFeature(BaseModel):
    name: str
    description: Optional[str]
    grants: Optional[list[Union[Grant | Selection]]]


class Class(BaseModel):
    name: str
    description: Optional[str]
    subclass = Optional[list["SubClass"]]
    class_features: Optional[list[ClassFeature]]
    grants: Optional[list[Union[Grant | Selection]]]


class SubClass(BaseModel):
    name: str
    parent: Optional[Class]
    description: Optional[str]
    class_features: Optional[list[ClassFeature]]
    grants: Optional[list[Union[Grant | Selection]]]


class Character(BaseModel):
    level: int
    experience: Optional[float]
    race: Optional[Union[Race | SubRace]]  #
    character_class: Optional[list[Class]]
    stats: Optional[list[Stat]]
    skills: Optional[list[Skill]]
    proficiency: Optional[list[Proficiency]]


def data_factory(data: dict, files: list, verbose: Literal[False] | Literal[True], config: dict) -> None:
    if config["engine"]["content"]["type"].lower() != "yml":
        echo(style(text=f"Error: Unsupported content type '{config['engine']['content']['type'].lower()}'.", fg="red"))
        return
    for file in files:
        if verbose:
            echo(style(text=f"Verbose: Trying to process contents of '{file}'", fg="cyan"))
        data = data[file]
        if data["engine"]["encoding"].lower() != "utf-8":
            echo(style(text=f"Error: Unsupported encoding '{data['engine']['encoding'].lower()}'.", fg="red"))
            continue
        else:
            pass  # TODO: Implement this...
    return
