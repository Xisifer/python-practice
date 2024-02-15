

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
        self.name = "Steve"
        self.gender = Gender.random()
        self.race = Race.random()
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
# char_dude = Character()
# print(f'char_dude gender is {char_dude.gender}')

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


# print(f'Player gender is {Player.gender}')
# player_dude = Player()
# print(f'player_dude gender is {player_dude.gender}')

class NPC(Character):
    def __init__(self):
        super().__init__()
        # self.gender = Gender.random()

# print(f'NPC gender is {NPC.gender}')
# npc_dude = NPC()
# print(f'npc_dude gender is {npc_dude.gender}')

class Ally(NPC):
    def __init__(self, job=None): 
        super().__init__()
        if not job:
            self.job = AllyJob.random()
        else:
            self.job = job



        # print(f'before match: Ally is {self.gender}')
        match self.gender:
            case Gender.MALE: 
                # print(f'in match male: Ally is {self.gender}')
                self.he_she = 'he'
                self.him_her = 'him'
                self.his_hers = 'his'
                self.is_are = 'is'
            case Gender.FEMALE:
                # print(f'in match female: Ally is {self.gender}')
                self.he_she = 'she'
                self.him_her = 'her'
                self.his_hers = 'hers'
                self.is_are = 'is'
            case Gender.NB:
                # print(f'in match NB: Ally is {gender}')
                self.he_she = 'they'
                self.him_her = 'them'
                self.his_hers = 'their'
                self.is_are = 'are'
                
        self.meeting_circumstance = AllyMeeting.random()
        print('=====================')
        
        match self.meeting_circumstance:
            case AllyMeeting.SAVED_THEM:
                print(f'You saved {self.him_her} from something',10)
            case AllyMeeting.SAVED_YOU:
                print(f'{self.he_she} saved you from something'.capitalize())

        self.friendship_level = AllyRelation.random()


# def prettify(words, f):
#     print('Are we pretty?')
#     print(str(words).format(f))
#     print('I\'m pretty!')


# class AllyMeet(LifeEvent):
#     ally_meeting = {
#         f'You saved {Ally.him_her} from something':10,
#         f'{Ally.he_she} saved you from something':10,
#         f'you met {him_her} in a tavern':10,
#         f'You fought together against something':10,
#         f'You were trapped together somehow':10,
#         f'You met while traveling':10,
#         f'You hired {him_her} to do something':10,
#         f'{he_she} hired you to do something':10,
#         f'You fought against each other and came to mutual respect through combat':10,
#         f'You were forced to work together':10
#     }

# llyMeeting(WeightedEnum):
#     SAVED_THEM = (f'You saved them from something',10)
#     SAVED_YOU = (f'They saved you from something',10)
#     TAVERN = (f'you met them in a tavern',10)
#     ALLIES = ('You fought together against something',10)
#     TRAPPED = ('You were trapped together somehow',10)
#     TRAVELING = ('You met while traveling',10)
#     HIRED_THEM = ('You hired them to do something',10)
#     HIRED_YOU = ('They hired you to do something',10)
#     ENEMIES = ('You fought against each other and came to mutual respect through combat',10)
#     RELUCTANT_ALLY = ('You











# print(f'Ally gender is {Ally.gender}')
ally_dude = Ally(AllyJob.PEASANT)
print(f'Ally_dude gender is {ally_dude.gender}')
print(f'======Ally pronoun is: {ally_dude.he_she}')


contacts = []
for _ in range(5):
    contact = Ally()
    contacts.append(contact)
    print(f'Met a {contact.gender} {contact.race} person named {contact.name} who is a {contact.job}.')



# class Enemy(NPC):
#     def __init__(self, name, gender, race, age, job, positions, ex_friend, ex_lover, relative,
#                  childhood_enemy, cause_of_enmity, social_power, knowledge, physical_power, minions, magical_power):
#         super().__init__(name, gender, race, age, job)
#         self.positions = positions
#         self.ex_friend = ex_friend
#         self.ex_lover = ex_lover
#         self.relative = relative
#         self.childhood_enemy = childhood_enemy
#         self.cause_of_enmity = cause_of_enmity
#         self.social_power = social_power
#         self.knowledge = knowledge
#         self.physical_power = physical_power
#         self.minions = minions
#         self.magical_power = magical_power




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
        self.event_type = LifeEventType.random()
        match self.self.event_type:
            case LifeEventType.FORTUNE:
                print(f'rolled fortune {self.event_type}')
            case LifeEventType.MISFORTUNE:
                print(f'rolled misfortune {self.event_type}')
            case LifeEventType.ALLY: 
                print(f'rolled ally {self.event_type}')
            case LifeEventType.ENEMY: 
                print(f'rolled enemy {self.event_type}')
            case LifeEventType.ROMANCE:
                print(f'rolled romance {self.event_type}')



class MeetEnemy(LifeEvent):
    pass



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
