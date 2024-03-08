'Holds the models for the D&D 5e elements'

from typing import Optional, Union

from pydantic import BaseModel


class Grant(BaseModel):
    """
    A grant is a way to give a character a bonus or ability.
    """
    property: any # TODO: Figure out how to do this

class Selection(BaseModel):
    """
    A choice of grants.

    name: str - The lable of the selection field
    grants: Optional[list[Grant]] - The list of grants that the selection can give
    """
    name: str
    grants: Optional[list[Grant]]

class DieRoll(BaseModel):
    """
    A die roll.

    die_count: int - The number of dice to roll
    die_size: int - The size of the die to roll
    """
    die_count: int
    die_size: int

class Property(BaseModel):
    """
    Misc information accociated with a 5e element.
    Examples: age, height, weight, deity, faction, exc

    name: str - The name of the property
    type: str - The type/field that the property is associated with
    description: Optional[str] - The value associated with the property
    """
    name: str
    type: str
    description: Optional[str]

class Stat(BaseModel):
    """
    A stat.

    name: str - The name of the stat
    value: int - The value of the stat
    type: str - The type of the stat
    """
    name: str
    value: int
    type: str

class Skill(BaseModel):
    """
    A skill.

    name: str - The name of the skill
    calculation: str - The calculation used to determine the value of the skill
    """
    name: str
    calculation: str

class Damage(BaseModel):
    """
    A damage type.

    type: Optional[str] - The type of damage
    roll: Optional[DieRoll] - The roll of the damage
    additional: Optional[int] - Additional damage that is added to the result of the roll
    """
    type: Optional[str] # Slashing, Fire, exc
    roll: Optional[DieRoll]
    additional: Optional[int]

class Spell(BaseModel):
    """
    A spell.

    name: str - The name of the spell
    description: Optional[str] - The description of the spell
    level: int - The level of the spell
    school: Optional[str] - The school of the spell
    casting_time: str - The casting time of the spell
    range: Optional[int] - The range of the spell
    components_s: bool - If the spell has a somatic component
    components_v: bool - If the spell has a verbal component
    components_m: Optional[list[str]] - If the spell has a material component
    duration: str - The duration of the spell
    concentration: bool - If the spell requires concentration
    ritual: bool - If the spell can be cast as a ritual
    damage: Optional[list[Damage]] - The damage of the spell
    properties: Optional[list[Property]] - The properties of the spell
    """
    name: str
    description: Optional[str]
    level: int
    school: Optional[str]
    casting_time: str
    range: Optional[int]
    components_s: bool
    components_v: bool
    components_m: Optional[list[str]]
    duration: str
    concentration: bool
    ritual: bool
    damage: Optional[list[Damage]]
    properties: Optional[list[Property]]

class Spellcasting(BaseModel):
    """
    A spellcasting class.

    source: Optional['Class'|any] - Tie it to a class for bonuses, etc
    type: str - Prepared, Known
    spellcasting_ability: Optional[Union['Stat', str]] - The ability that the class uses to cast spells
    spells: list[Spell] - The list of spells that the class can cast
    optional_rules: Optional[str] - Any optional rules that the class uses
    """
    source: Optional['Class'|any] # Tie it to a class for bonuses, etc
    type: str # Prepared, Known
    spellcasting_ability: Optional[Union[Stat, str]]
    spells: list[Spell]
    optional_rules: Optional[str]

class Proficiency(BaseModel):
    """
    A proficiency.

    name: str - The name of the proficiency
    type: str - The type of the proficiency
    description: Optional[str] - The description of the proficiency
    """
    name: str
    type: str
    description: Optional[str]

class Weapon(BaseModel):
    """
    A weapon.

    name: str - The name of the weapon
    type: list['WeaponCategory'] - The type of the weapon
    proficiency: Optional[Proficiency] - The proficiency of the weapon
    description: Optional[str] - The description of the weapon
    damage: Optional[list[Damage]] - The damage of the weapon
    properties: Optional[list[Property]] - The properties of the weapon
    weight: Optional[int] - The weight of the weapon
    """
    name: str
    type: list['WeaponCategory']
    proficiency: Optional[Proficiency]
    description: Optional[str]
    damage: Optional[list[Damage]]
    properties: Optional[list[Property]]
    weight: Optional[int]

class WeaponCategory(BaseModel):
    """
    A category to group weapons.
    Examples: Simple, Martial, Ranged, Melee, Longsword, exc

    name: str - The name of the weapon category
    description: Optional[str] - The description of the weapon category
    weapons: Optional[list[Union[Weapon,'WeaponCategory']]] - The weapons in the category
    """
    name: str
    description: Optional[str]
    weapons: Optional[list[Union[Weapon,'WeaponCategory']]]

class MagicWeapon(BaseModel):
    """
    A magic weapon is an enhanced version .

    name: str - The name of the weapon
    parent: Optional[Weapon] - The base version of the weapon
    description: Optional[str] - The description of the weapon
    damage: Optional[list[Damage]] - The additional damage of the weapon
    damage_bonus: Optional[int] - The flat damage bonus of the weapon
    grants: Optional[list[Union[Grant,Selection]]] - The grants of the weapon
    properties: Optional[list[Property]] - The properties of the weapon
    hit_bonus: Optional[int] - The hit bonus of the weapon
    """
    name: str
    parent: Optional[Weapon]
    description: Optional[str]
    damage: Optional[list[Damage]]
    damage_bonus: Optional[int]
    grants: Optional[list[Union[Grant,Selection]]]
    properties: Optional[list[Property]]
    hit_bonus: Optional[int]

class Armor(BaseModel):
    """
    An armor.

    name: str - The name of the armor
    type: list['ArmorCategory'] - The type of the armor
    proficiency: Optional[Proficiency] - The proficiency of the armor
    description: Optional[str] - The description of the armor
    armor_class: int - The armor class of the armor
    stealth_disadvantage: bool - If the armor gives stealth disadvantage
    weight: Optional[int] - The weight of the armor
    properties: Optional[list[Property]] - The properties of the armor
    """
    name: str
    type: list['ArmorCategory']
    proficiency: Optional[Proficiency]
    description: Optional[str]
    armor_class: int
    stealth_disadvantage: bool
    weight: Optional[int]
    properties: Optional[list[Property]]

class ArmorCategory(BaseModel):
    """
    A category to group armors.
    Examples: Light, Medium, Heavy, Shield

    name: str - The name of the armor category
    description: Optional[str] - The description of the armor category
    armors: Optional[list[Union[Armor,'ArmorCategory']]] - The armors in the category
    strength_requirement: Optional[int] - The strength requirement of the armor
    ac_calculation: Optional[str] - The standard calculation used to determine the armor class of the armor
    """
    name: str
    description: Optional[str]
    armors: Optional[list[Union[Armor,'ArmorCategory']]]
    strength_requirement: Optional[int]
    ac_calculation: Optional[str]

class MagicArmor(BaseModel):
    """
    A magic armor is an enhanced version of an armor.

    name: str - The name of the armor
    parent: Optional[Armor] - The base version of the armor
    description: Optional[str] - The description of the armor
    armor_bonus: Optional[int] - Additional armor bonus of the armor
    ac_calculation_override: Optional[str] - The calculation used to override the standard armor class calculation
    stealth_disadvantage_override: Optional[bool] - If the armor gives stealth disadvantage
    strength_requirement_override: Optional[int] - The new strength requirement of the armor
    weight_override: Optional[int] - The new weight of the armor
    grants: Optional[list[Union[Grant,Selection]]] - The grants of the armor
    properties: Optional[list[Property]] - The properties of the armor
    """
    name: str
    parent: Optional[Armor]
    description: Optional[str]
    armor_bonus: Optional[int]
    ac_calculation_override: Optional[str]
    stealth_disadvantage_override: bool
    strength_requirement_override: Optional[int]
    weight_override: Optional[int]
    grants: Optional[list[Union[Grant,Selection]]]
    properties: Optional[list[Property]]

class Vision(BaseModel):
    """
    A vision type.

    name: str - The name of the vision type
    description: Optional[str] - The description of the vision type
    distance: int - The distance of the vision type
    """
    name: str
    description: Optional[str]
    distance: int

class Language(BaseModel):
    """
    A language.

    name: str - The name of the language
    description: Optional[str] - The description of the language
    """
    name: str
    description: Optional[str]

class BackgroundFeature(BaseModel):
    """
    A background feature.

    name: str - The name of the background feature
    description: Optional[str] - The description of the background feature
    grants: Optional[list[Union[Grant|Selection]]] - The grants of the background feature
    """
    name: str
    description: Optional[str]
    grants: Optional[list[Union[Grant|Selection]]]

class Background(BaseModel):
    """
    A background.

    name: str - The name of the background
    version: str - The version of the background Example: PHB2014, PHB2024, ONEDND_PLAYTEST
    description: Optional[str] - The description of the background
    background_features: Optional[list[BackgroundFeature]] - The background features of the background
    languages: Optional[list[Language]] - The languages of the background
    stats: Optional[list[Stat]] - The stats given by the background (PHB2024, ONEDND_PLAYTEST)
    grants: Optional[list[Union[Grant|Selection]]] - The grants of the background
    """
    name: str
    version: str
    description: Optional[str]
    background_features: Optional[list[BackgroundFeature]]
    languages: Optional[list[Language]]
    stats: Optional[list[Stat]]
    grants: Optional[list[Union[Grant|Selection]]] # Includes proficiencies, feats, etc

class FeatFeature(BaseModel):
    """
    A feature granted by a feat.

    name: str - The name of the feature
    description: Optional[str] - The description of the feature
    grants: Optional[list[Union[Grant|Selection]]] - The grants of the feature
    """
    name: str
    description: Optional[str]
    grants: Optional[list[Union[Grant|Selection]]]

class Feat(BaseModel):
    """
    A feat.

    name: str - The name of the feat
    description: Optional[str] - The description of the feat
    grants: Optional[list[Union[Grant|Selection]]] - The grants of the feat
    feat_features: Optional[list[FeatFeature]] - The features of the feat
    """
    name: str
    description: Optional[str]
    grants: Optional[list[Union[Grant,Selection]]]
    feat_features: Optional[list[FeatFeature]]

class RaceFeature(BaseModel):
    """
    A feature granted by a race.

    name: str - The name of the feature
    description: Optional[str] - The description of the feature
    grants: Optional[list[Union[Grant,Selection]]] - The grants of the feature
    """
    name: str
    description: Optional[str]
    grants: Optional[list[Union[Grant,Selection]]]

class Race(BaseModel):
    """
    The character's race.

    name: str - The name of the race
    description: Optional[str] - The description of the race
    subrace = Optional[list['SubRace'|'VarientRace']] - The selected Subrace/VarientRace
    size: str - The size of the creature. Example: Medium, Small
    speed: int - The base speed of the creature.
    vision: Optional[Vision] - The vision granted by the race
    race_features: Optional[list[RaceFeature]] - The features granted by the race
    """
    name: str
    description: Optional[str]
    subrace = Optional[list[Union['SubRace','VarientRace']]]
    size: str
    speed: int
    vision: Optional[Vision]
    race_features: Optional[list[RaceFeature]]

class SubRace(BaseModel):
    """
    A subrace

    name: str - The name of the subrace
    description: Optional[str] - The description of the subrace
    parent: The base race of the subrace
    vision: Optional[Vision] - The vision granted by the subrace
    race_features: Optional[list[RaceFeature]] - The features granted by the subrace
    """
    name: str
    description: Optional[str]
    parent: Race
    vision: Optional[Vision]
    race_features: Optional[list[RaceFeature]]

class VarientRace(BaseModel):
    """
    A subrace

    name: str - The name of the varient race
    description: Optional[str] - The description of the varient race
    parent: The base race of the varient race
    vision: Optional[Vision] - The vision granted by the varient race
    race_features: Optional[list[RaceFeature]] - The features granted by the varient race
    """
    name: str
    description: Optional[str]
    parent: Race
    vision: Optional[Vision]
    race_features: Optional[list[RaceFeature]]

class ClassFeature(BaseModel):
    """
    A feature granted by a class.

    name: str - The name of the feature
    description: Optional[str] - The description of the feature
    grants: Optional[list[Union[Grant|Selection]]] - The grants of the feature
    """
    name: str
    description: Optional[str]
    grants: Optional[list[Union[Grant|Selection]]]

class Class(BaseModel):
    """
    A class.

    name: str - The name of the class
    level: int - The current level class the class
    hit_die: int - The hit die of the class
    description: Optional[str] - The description of the class
    subclass = Optional[list['SubClass']] - The subclasses of the class
    class_features: Optional[list[ClassFeature]] - The features of the class
    proficiency: Optional[list[Proficiency]] - The proficiencies of the class
    saving_throws: Optional[list[Stat]] - The saving throws of the class
    grants: Optional[list[Union[Grant|Selection]]] - The grants of the class
    spellcasting: Optional[Spellcasting] - The spellcasting of the class
    """
    name: str
    level: int
    hit_die: int
    description: Optional[str]
    subclass = Optional[list['SubClass']]
    class_features: Optional[list[ClassFeature]]
    proficiency: Optional[list[Proficiency]]
    saving_throws: Optional[list[Stat]]
    grants: Optional[list[Union[Grant|Selection]]]
    spellcasting: Optional[Spellcasting]

class SubClass(BaseModel):
    """
    A subclass

    name: str - The name of the subclass
    parent: Class - The base class of the subclass
    description: Optional[str] - The description of the subclass
    class_features: Optional[list[ClassFeature]] - The features of the subclass
    grants: Optional[list[Union[Grant|Selection]]] - The grants of the subclass
    """
    name: str
    parent: Optional[Class]
    description: Optional[str]
    class_features: Optional[list[ClassFeature]]
    grants: Optional[list[Union[Grant|Selection]]]

class Character(BaseModel):
    """
    A character.

    name: str - The name of the character
    level: int - The current level of the character
    experience: Optional[float] - The current experience of the character
    background: Optional[Background] - The background of the character
    properties: Optional[list[Property]] - The properties of the character
    race: Optional[Race] - The race of the character
    character_class: Optional[list[Class]] - The classes of the character
    stats: Optional[list[Stat]] - The stats of the character
    skills: Optional[list[Skill]] - The skills of the character
    proficiency: Optional[list[Proficiency]] - The proficiencies of the character
    """
    level: int
    experience: Optional[float]
    background: Optional[Background]
    properties: Optional[list[Property]] # Diety, Age, exc
    race: Optional[Race]
    character_class: Optional[list[Class]]
    stats: Optional[list[Stat]]
    skills: Optional[list[Skill]]
    proficiency: Optional[list[Proficiency]]
