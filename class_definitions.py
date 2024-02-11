

# ========================================================================================================


import random
from char_creation_menus import *
from char_creation_rollers import *
from general_functions import *
from char_save_data import *
from char_properties import *
from class_enums import *

# Define an overall Character class


class Character:
    # Dictionary of races with their respective probability weights
    races = {
        'Human': 20,
        'Elf': 10,
        'Dwarf': 10,
        'Halfling': 10,
        'Gnome': 10,
        'Dragonborn': 5,
        'Orc': 10,
        'Goblin': 10,
        'Kobold': 10,
        'Gnoll': 5
    }
    human_origins = {
    'You are from Waterdeep, the City of Splendors.':40,
    'You are from Baldur\'s Gate.':20,
    'You are from Varisia, the Lands of Adventure':30,
    'You are from the Mwangi Expanse, the dense jungle heartland.':10
    }

    
    
    def __init__(self):
        # self.name = name
        self.gender = Gender.random()
        # self.race = Race.random()
        # self.age = age


    def roll(dictionary):
        # When provided with a dictionary consisting of Keys as strings adn Values as probabilities-out-of-100, roll according to probabilities and output the result.
        rolled = random.choices(list(dictionary.keys()), weights=dictionary.values(), k=1)
        rolled_string = rolled[0] # just the string of the result

        dict_items = list(dictionary.items())
        rolled_index = [id for id, key in enumerate(dict_items) if key[0] == rolled_string] # index of the result, used for conditionally targeting specific table results 
        # [ex. favorite drink; if you roll Milk, stop; if you roll Soda, ask what kind]

        # pack both string and index into a tuple for export
        return (rolled_string, rolled_index[0])

    def roll_race(stuff):
        # from char_creation_menus import races
        race_result = roll(races)
        return race_result

# print(f'Character gender is {Character.gender}')
char_dude = Character()
print(f'char_dude gender is {char_dude.gender}')

class Player(Character):
    def __init__(self): # , name=None, gender=None, race=None, age=None, job=None, origin=None, life_events=None):
        super().__init__() # (name, race, age, job)
        # self.race = race
        # self.origin = origin  # Origin object
        # self.life_events = life_events  # List of LifeEvent objects

    def roll_attribute(self, attribute_dict):
        rolled = random.choices(list(attribute_dict.keys()), weights=attribute_dict.values(), k=1)
        rolled_item = rolled[0]
        rolled_index = list(attribute_dict.keys()).index(rolled_item)
        return rolled_item, rolled_index
    
    def roll_race(self):
        self.race, self.race_index = self.roll_attribute(self.races)


# print(f'Player gender is {Player.gender}')
player_dude = Player()
print(f'player_dude gender is {player_dude.gender}')

class NPC(Character):
    def __init__(self):
        super().__init__()
        # self.gender = Gender.random()

# print(f'NPC gender is {NPC.gender}')
npc_dude = NPC()
print(f'npc_dude gender is {npc_dude.gender}')

class Ally(NPC):
    def __init__(self): #, name=None, gender=NPC.gender, race=None, age=None, job=None, meeting_circumstance=None, friendship_level=None):
        super().__init__()
        self.gender = gender
        self.job = AllyClass.random()
        self.meeting_circumstance = AllyMeet.random()
        self.friendship_level = friendship_level

        match self.gender:
            case gender.MALE: 
                he_she = 'he'
                him_her = 'him'
                his_hers = 'his'
                is_are = 'is'
            case gender.FEMALE:
                he_she = 'she'
                him_her = 'her'
                his_hers = 'hers'
                is_are = 'is'
            case gender.NB:
                he_she = 'they'
                him_her = 'them'
                his_hers = 'their'
                is_are = 'are'
# class AllyFactory: 
#     def __init__(self,name,gender,race,job):
#         self.name = name
#         self.gender = gender
#         self.race = race
#         self.job = job
#     @staticmethod
#     def create_ally(name=None, gender=Ally.gender, race=Ally.race, job=Ally.job):
#         return Ally(gender,race,job)
        
# print(f'Ally gender is {Ally.gender}')
ally_dude = Ally()
print(f'Ally_dude gender is {ally_dude.gender}')

for _ in range(5):
    contact1 = Ally()
    print(f'Met a {contact1.gender} {contact1.race} person who is a {contact1.job}.')

class Enemy(NPC):
    def __init__(self, name, gender, race, age, job, positions, ex_friend, ex_lover, relative,
                 childhood_enemy, cause_of_enmity, social_power, knowledge, physical_power, minions, magical_power):
        super().__init__(name, gender, race, age, job)
        self.positions = positions
        self.ex_friend = ex_friend
        self.ex_lover = ex_lover
        self.relative = relative
        self.childhood_enemy = childhood_enemy
        self.cause_of_enmity = cause_of_enmity
        self.social_power = social_power
        self.knowledge = knowledge
        self.physical_power = physical_power
        self.minions = minions
        self.magical_power = magical_power




# Define the Parent class with a race property
class Parent:
    def __init__(self, gender=None, race=None, age=None, job=None, biological=True):
        super().__init__()
        self.race = race
        self.biological = biological

# Define the ParentFactory class with a factory method to create Parent instances
class ParentFactory:

    @staticmethod
    def create_parent(gender=None, race='Human', age=None, job=None, biological=True):
        # race = Player.race
        if biological == True:
            race = Character.roll_race
        
        return Parent(gender, race, age, job, biological)

# Example usage:
# Create a few Parent instances to demonstrate the randomness
for _ in range(5):
    parent = ParentFactory.create_parent()
    print(f'Created a {parent.race} parent.')


class Homeland:
    pass  # Assuming no attributes as not specified

class Family:
    def __init__(self, parents, siblings, fate):
        self.parents = parents  # List of Parent objects
        self.siblings = siblings  # List of Sibling objects
        self.fate = fate

class Sibling:
    pass  # Assuming no attributes as not specified

class LifeEvent:
    def __init__(self, age):
        self.age = age

class EventFactory: 
    @staticmethod
    def create_event(): 
        event_type = Player.roll_attribute(LifeEventType)
        match event_type:
            case LifeEventType.FORTUNE:
                print(f'rolled fortune {event_type}')
            case LifeEventType.MISFORTUNE:
                print(f'rolled misfortune {event_type}')
            case LifeEventType.ALLY: 
                print(f'rolled ally {event_type}')
            case LifeEventType.ENEMY: 
                print(f'rolled enemy {event_type}')
            case LifeEventType.ROMANCE:
                print(f'rolled romance {event_type}')

for _ in range(5):
    event = EventFactory.create_event()
    print(f'Created a {event.event_type} event.')


class MeetEnemy(LifeEvent):
    pass

class AllyMeet(LifeEvent):
    ally_meeting = {
        f'You saved {him_her} from something':10,
        f'{he_she} saved you from something':10,
        f'you met {him_her} in a tavern':10,
        f'You fought together against something':10,
        f'You were trapped together somehow':10,
        f'You met while traveling':10,
        f'You hired {him_her} to do something':10,
        f'{he_she} hired you to do something':10,
        f'You fought against each other and came to mutual respect through combat':10,
        f'You were forced to work together':10
    }

class Romance(LifeEvent):
    def __init__(self, age, tragedy, problematic, happy):
        super().__init__(age)
        self.tragedy = tragedy
        self.problematic = problematic
        self.happy = happy

class Misfortune(LifeEvent):
    def __init__(self, age, gold, thief=None):
        super().__init__(age)
        self.gold = gold
        self.thief = thief

class Fortune(LifeEvent):
    pass


class Origin:
    def __init__(self, homeland, family):
        self.homeland = homeland  # Homeland object
        self.family = family  # Family object
