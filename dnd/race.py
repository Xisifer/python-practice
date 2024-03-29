from dnd.class_enums import WeightedEnum

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


    