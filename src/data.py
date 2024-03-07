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


class Character:
    def __init__(
        self,
        name: str | None,
        hp: str | int | None,
        ac: str | int | None,
        strength: str | int | None,
        dexterity: str | int | None,
        constitution: str | int | None,
        intelligence: str | int | None,
        wisdom: str | int | None,
        charisma: str | int | None,
    ) -> None:
        if name:
            self.name = name
        else:
            self.name = None
        if hp:
            self.hp = int(hp)
        else:
            self.hp = None
        if ac:
            self.ac = int(ac)
        else:
            self.ac = None
        if strength:
            self.strength = int(strength)
        else:
            self.strength = None
        if dexterity:
            self.dexterity = int(dexterity)
        else:
            self.dexterity = None
        if constitution:
            self.constitution = int(constitution)
        else:
            self.constitution = None
        if intelligence:
            self.intelligence = int(intelligence)
        else:
            self.intelligence = None
        if wisdom:
            self.wisdom = int(wisdom)
        else:
            self.wisdom = None
        if charisma:
            self.charisma = int(charisma)
        else:
            self.charisma = None
        self.stat_dict = self._stats_dict()

    def __setitem__(self, key, value):
        self[key] = value

    def __repr__(self):
        return str(self._stats_dict())

    def _stats_dict(self) -> dict:
        stats_dict = {
            "HP": self.hp,
            "AC": self.ac,
            "Strength": self.strength,
            "Dexterity": self.dexterity,
            "Constitution": self.constitution,
            "Intelligence": self.intelligence,
            "Wisdom": self.wisdom,
            "Charisma": self.charisma,
        }
        return stats_dict

    def get_stat(self, stat: str) -> int:
        if stat in self.stat_dict:
            return self.stat_dict[stat]
        else:
            raise KeyError(f"The '{stat}' stat doesn't exist for this entity.")  # noqa: TRY003

    def set_stat(self, stat: str, value: int | str) -> None:
        if stat in self.stat_dict:
            self[stat] = int(value)
        else:
            raise KeyError(f"The '{stat}' stat doesn't exist for this entity.")  # noqa: TRY003


def data_factory(data: dict, files: list, verbose: Literal[False] | Literal[True], config: dict) -> None:
    for file in files:  # noqa: B007
        pass  # TODO: Implement...
