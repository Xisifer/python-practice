from dnd.character_class import Character
from dnd.race import Race

# Define the Parent class with a race property
class Parent(Character):
    def __init__(self, gender=None, race=None, job=None):
        super().__init__()
        self.gender = gender
        self.race = race
        self.job = job



# Example usage:
# Create a few Parent instances to demonstrate the randomness
# for _ in range(5):
#     parent = Parent()
#     print(f'Created a {parent.race} parent.')

