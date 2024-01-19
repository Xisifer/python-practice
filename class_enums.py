
from enum import Enum
import random

class WeightedEnum(Enum):
    def __init__(self, str, weight):
        self.str = str
        self.weight = weight

    def __str__(self):
        return self.str

    @classmethod
    def random(cls):
        all = list(cls)
        weights = [x.weight for x in all]
        return random.choices(all, weights)[0]

class Race(WeightedEnum):
    HUMAN = ("Human", 20)
    ELF = ("Elf", 10)
    DWARF = ("Dwarf", 10)
    HALFLING = ("Halfling", 10)
    GNOME = ("Gnome", 10)
    DRAGONBORN = ("Dragonborn", 5)
    ORC = ("Orc", 10)
    GOBLIN = ("Goblin", 10)
    KOBOLD = ("Kobold", 10)
    GNOLL = ("Gnoll", 5)

class HumanOrigins(WeightedEnum):
    WATERDEEP = ("Waterdeep, the City of Splendors", 40)
    BALDUR = ("Baldur's Gate", 20)
    VARISIA = ("Varisia, the Lands of Adventure", 30)
    MWANGI = ("the Mwangi Expanse, the dense jungle heartland", 10)

class HumanHomes(WeightedEnum):
    FAERUN = ("Faerun", 50)
    GOLARION = ("Golarion", 50)

class FeyHomes(WeightedEnum):
    FOREST = ('Forest',55)
    MOUNTAINS = ('Mountains',15)
    OCEAN = ('Ocean',20)
    JUNGLE = ('Jungle',10)

class SavageHomes(WeightedEnum):
    BADLANDS = ('Badlands', 25)
    SWAMP = ('Swamps', 15)
    RUINS = ('Ruins', 10)
    CAMP = ('War Camp', 25)
    CAVE = ('Underground Caverns', 25)




class Character:
    def __init__(self):
        self.race = Race.random()
        match self.race:
            case Race.HUMAN:
                self.origin = HumanOrigins.random()
            case Race.HALFLING:
                self.origin = "Halfland"
            case _:
                self.origin = "Hell"

player = Character()
print(f'Race: {player.race}, Origin: You are from {player.origin}.')


