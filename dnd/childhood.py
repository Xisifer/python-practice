from dnd.class_enums import WeightedEnum

class Birth(WeightedEnum):
    BORN = ('Born: You were born naturally.', 33)
    ADOPTED = ('Adopted: You were adopted and raised by a different family than the one that birthed you.', 33)
    ORPHAN = ('Orphan: You HAD parents, but they\'re dead now.', 33)

class Childhood(WeightedEnum):
    growup = ['']