from dnd.character_class import Character
import random

class Player(Character):
    def __init__(self): 
        super().__init__() # (name, race, age, job)
        self.origin = origin  # Origin object
        self.life_events = life_events  # List of LifeEvent objects
        