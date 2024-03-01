from dnd.class_enums import WeightedEnum

class SavageOrigins(WeightedEnum):
    GUTTER = ('You grew up always fighting for survival, scrabbling together a life in the dirt and gutter of society.', 35)
    WARRIOR_CHILD = ('You grew up the child of a powerful warrior, and everyone expected you to live up to their accomplishments.', 25)
    SAVAGE_ORIGIN_3 = ('You grew up C', 25)
    SAVAGE_ORIGIN_4 = ('You grew up D', 15)

class SavageFlavor(WeightedEnum):
    SURVIVAL = ('Life in your homeland was tough. You had to fight to survive.',30)
    NECESSARY = ('Only the strongest survive. You did whatever necessary to be the best.',70)

class SavageHomes(WeightedEnum):
    BADLANDS = ('Badlands',25)
    SWAMPS = ('Swamps',15)
    RUINS = ('Ruins',10)
    CAMP = ('War Camp', 25)
    CAVERN = ('Underground Caverns', 25)