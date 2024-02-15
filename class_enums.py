
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

class Gender(WeightedEnum):
    MALE = ("Male", 45)
    FEMALE = ("Female", 45)
    NB = ("Nonbinary", 10)

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


class LifeEventType(WeightedEnum):
    FORTUNE = ('Fortunate Event', 20)
    MISFORTUNE = ('Unfortunate Event', 20)
    ALLY = ('Met an Ally', 20)
    ENEMY = ('Made an Enemy', 20)
    ROMANCE = ('Had a Romantic relationship', 20)



class AllyJob(WeightedEnum):
    BH = ('Bounty Hunter',10)
    MAGE = ('Mage',10)
    TEACHER = ('Mentor or Teacher',10)
    FRIEND = ('Childhood Friend',10)
    MERCHANT = ('Craftsman or Merchant',10)
    ENEMY = ('Former Enemy',10)
    NOBLE = ('Noble',10)
    PEASANT = ('Peasant',10)
    SOLDIER = ('Soldier',10)
    BARD = ('Bard',10)

class AllyMeeting(WeightedEnum):
    SAVED_THEM = ('You saved {} from something',10)
    SAVED_YOU = ('{} saved you from something',10)
    # TAVERN = ('you met them in a tavern',10)
    # ALLIES = ('You fought together against something',10)
    # TRAPPED = ('You were trapped together somehow',10)
    # TRAVELING = ('You met while traveling',10)
    # HIRED_THEM = ('You hired them to do something',10)
    # HIRED_YOU = ('They hired you to do something',10)
    # ENEMIES = ('You fought against each other and came to mutual respect through combat',10)
    # RELUCTANT_ALLY = ('You were forced to work together',10)

class AllyRelation(WeightedEnum):
    ACQUAINTANCE = ('Acquaintances',40)
    FRIEND = ('Friends',20)
    CLOSE_FRIEND = ('Close Friends',20)
    INSEPERABLE = ('Inseperable',10)
    SWORN = ('Sworn companions/partners',10)

class AllyLocation(WeightedEnum):
    TOWN = ('a nearby town',30)
    CAPITOL = ('the country\'s grand capitol',30)
    VILLAGE = ('a peaceful village',20)
    HUT = ('a small hut in the middle of nowhere',10)

class AllyFate(WeightedEnum):
    ('{he_she} {is_are} gone in a far-off land',30)
    ('{he_she} {is_are} frequently somewhere nearby when you least expect {him_her}',25)
    ('{he_she} settled down in {al_location}.',30)
    ('{he_she} wanders the roads of adventure like you. Who knows where {he_she} {is_are} now?',10)
    ('Surprise! {he_she} {is_are} travelling with you as a party member! Work with your Game Master to create this character.',5)


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


