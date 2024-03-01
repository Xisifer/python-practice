from dnd.class_enums import WeightedEnum

class Childhood(WeightedEnum):
    NUCLEAR = ('You were born to a mother and a father.', 80)
    ADOPTED = ('You were adopted and raised by a different family than the one that birthed you.', 15)
    ORPHAN = ('You HAD parents, but they\'re dead now.', 5)
