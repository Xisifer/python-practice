

# Define the Parent class with a race property
class Parent(Character):
    def __init__(self):
        super().__init__()
        # self.race = race
        self.biological = True

# Define the ParentFactory class with a factory method to create Parent instances
class ParentFactory:

    @staticmethod
    def create_parent(gender=None, race='Human', age=None, job=None, biological=True):
        # race = Player.race
        if biological == True:
            race = Character.roll_race
        
        return 

# Example usage:
# Create a few Parent instances to demonstrate the randomness
for _ in range(5):
    parent = Parent()
    print(f'Created a {parent.race} parent.')

