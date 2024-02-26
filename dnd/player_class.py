
class Player(Character):
    def __init__(self): # , name=None, gender=None, race=None, age=None, job=None, origin=None, life_events=None):
        super().__init__() # (name, race, age, job)
        # self.origin = origin  # Origin object
        # self.life_events = life_events  # List of LifeEvent objects

    def roll_attribute(self, attribute_dict):
        rolled = random.choices(list(attribute_dict.keys()), weights=attribute_dict.values(), k=1)
        rolled_item = rolled[0]
        rolled_index = list(attribute_dict.keys()).index(rolled_item)
        return rolled_item, rolled_index
    
    def roll_race(self):
        self.race, self.race_index = self.roll_attribute(self.races)
