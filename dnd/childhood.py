from dnd.class_enums import WeightedEnum

class Birth(WeightedEnum):
    BORN = ('Born: You were born naturally.', 45)
    ADOPTED = ('Adopted: You were adopted and raised by a different family than the one that birthed you.', 45)
    ORPHAN = ('Orphan: You HAD parents, but they\'re dead now.', 10)

class Childhood(WeightedEnum):
    growup = ['']

