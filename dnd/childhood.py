from dnd.class_enums import WeightedEnum

class Childhood(WeightedEnum):
    BORN = ('You were born naturally.', 100)
    ADOPTED = ('You were adopted and raised by a different family than the one that birthed you.', 55)
    ORPHAN = ('You HAD parents, but they\'re dead now.', 5)
