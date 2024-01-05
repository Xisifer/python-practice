import random


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
    
    def __init__(self, name, gender, race, age, job):
        self.name = name
        self.gender = gender
        self.race = race
        self.age = age
        self.job = job

class Player(Character):
    def __init__(self, name, gender, race, age, job, origin, life_events):
        super().__init__(name, gender, race, age, job)
        self.origin = origin  # Origin object
        self.life_events = life_events  # List of LifeEvent objects
    @staticmethod
    def create_player():
        # Randomly select race based on the defined probabilities
        race = random.choices(list(ParentFactory.races.keys()), weights=ParentFactory.races.values(), k=1)[0]
        print(f'Created a {Player.race} player.')

class NPC(Character):
    pass

class Ally(NPC):
    def __init__(self, name, gender, race, age, job, jobs, meeting_circumstance, friendship_level):
        super().__init__(name, gender, race, age, job)
        self.jobs = jobs
        self.meeting_circumstance = meeting_circumstance
        self.friendship_level = friendship_level

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
    def __init__(self, name, gender, race, age, job, biological):
        super().__init__(name, gender, race, age, job)
        self.race = race
        self.biological = biological

# Define the ParentFactory class with a factory method to create Parent instances
class ParentFactory:


    @staticmethod
    def create_parent(gender, race, age, job, biological):
        
        # For simplicity, we're assuming biological is always True in this example
        biological = True
        return Parent(gender, race, age, job, biological)

# Example usage:
# Create a few Parent instances to demonstrate the randomness
for _ in range(5):
    parent = ParentFactory.create_parent(gender, race, age, job, biological)
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

class MeetEnemy(LifeEvent):
    pass

class MeetAlly(LifeEvent):
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
