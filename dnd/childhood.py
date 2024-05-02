from dnd.class_enums import WeightedEnum

class Birth(WeightedEnum):
    BORN = ('Born: You were born naturally.', 45)
    ADOPTED = ('Adopted: You were adopted and raised by a different family than the one that birthed you.', 45)
    ORPHAN = ('Orphan: You HAD parents, but they\'re dead now.', 10)

class Childhood(WeightedEnum):
    UPPERCLASS = ('Your parents belong to the upper class. They were wealthy and affluent, and you never lacked for opportunities in life. Money opens doors, and you had the means to do and become anything you wanted to.')
    MIDDLECLASS = ('Your parents belong to the middle class. They were honest workers who tried to set you up for success in life. You never went hungry or cold at night, but you were taught to live modestly within your means, keeping your head down to get by in life.')
    LOWERCLASS = ('Your parents belong to the lower class. They were hard-working people who tried to give you the opportunities they never had, but were not usually successful. Times were often hard, and sometimes you had to go hungry or search for a new bed for the night.')
    

