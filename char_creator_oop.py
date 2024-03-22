import inquirer
import random
from dnd.player_class import Player
from dnd.life_events import LifeEvent
from dnd.character_class import Character
from dnd.race import Race
from dnd.childhood import Birth, Childhood
from dnd.origin_human import HumanOrigins, HumanFlavor, HumanHomes
from dnd.origin_fey import FeyOrigins, FeyFlavor, FeyHomes
from dnd.origin_savage import SavageOrigins, SavageFlavor, SavageHomes
from dnd.parents_status import ParentsStatus
from dnd.parent_class import Parent
from dnd.jobs_menu import PlayerJob, NPCJob, AllyJob
from dnd.gender import Gender

def name_input():
    char_name = input("Character name: ")
    name_stripped = str(char_name.strip())
    return name_stripped



def ask_reroll(question_text, roll_result):
    choice_menu = {
        inquirer.List('menu',
                    message=f'{question_text} {roll_result}',
                    choices=['Accept', 'Reroll'], default=['Accept']
        )
    }
    answer = inquirer.prompt(choice_menu)

    if answer['menu'] == 'Reroll':
        return True
    else:
        return False

def creator_question(question_text, attribute):
    rolled_result = attribute.random()
    does_player_reroll = ask_reroll(question_text, rolled_result)
    while does_player_reroll == True:
        rolled_result = attribute.random()
        does_player_reroll = ask_reroll(question_text, rolled_result)
    return rolled_result



player_char = Character()

# player_char.name = name_input()

player_char.race = creator_question('Select race: ', Race)

# player_char.bg_childhood = creator_question('Your origin: ', Childhood)

# match player_char.race:
#     case Race.HUMAN:
#         player_char.bg_homeland = creator_question('You hail from ', HumanHomes)
#         player_char.bg_origin = creator_question('You were raised in ', HumanOrigins)
#         player_char.bg_flavor = creator_question('As you were growing up, ', HumanFlavor)


#     case Race.ELF | Race.HALFLING | Race.GNOME:
#         player_char.bg_homeland = creator_question('You hail from ', FeyHomes)
#         player_char.bg_origin = creator_question('You were raised in ', FeyOrigins)
#         player_char.bg_flavor = creator_question('As you were growing up, ', FeyFlavor)
    
#     case Race.DRAGONBORN | Race.ORC | Race.GOBLIN | Race.KOBOLD | Race.GNOLL:
#         player_char.bg_homeland = creator_question('You hail from ', SavageHomes)
#         player_char.bg_origin = creator_question('You were raised in ', SavageOrigins)
#         player_char.bg_flavor = creator_question('As you were growing up, ', SavageFlavor)

#     case _:
#         print('ERROR')


# ===================================================
# Parents and Family


# Both parents, single parent, orphan?
# By default, every character has a birth mother
pc_parent1 = Parent()
pc_parent1.gender = Gender.FEMALE
pc_parent1.race = player_char.race
pc_parent1.job = NPCJob.random()
# Second parent defaults to Father, but this can change
pc_parent2 = Parent()
pc_parent2.gender = Gender.MALE
pc_parent2.race = player_char.race
pc_parent2.job = NPCJob.random()


# pc_childhood starts empty
pc_childhood = ''

player_char.bg_birth = Birth.random()

print(f'player_char.bg_birth is: {str(player_char.bg_birth)}')


for parent in pc_parent1, pc_parent2:
    if parent:
        pc_childhood += "Your {} is a {} {}. ".format(
            "mother" if parent.gender == Gender.FEMALE else "father",
            parent.race, parent.job)

# pc_childhood now has parents info
match player_char.bg_birth:

    case Birth.ORPHAN:
        pc_parent1 = None
        pc_childhood += 'You are an orphan.'

            
    case _:
        pc_parent1 = random.choice([None, pc_parent1])
        pc_parent2 = random.choice([None, pc_parent2])
        num_parents = bool(pc_parent1) + bool(pc_parent2)


        pc_childhood += "You were {} {} parent{}.".format(
            "adopted by" if Birth.ADOPTED else "born to",
            num_parents,
            "s" if num_parents > 1 else "")
        

def reroll_childhood(childhood):
    print(childhood)

def randomizer_reroll(question_text):
    choice_menu = {
        inquirer.List('menu',
                    message=f'{question_text}',
                    choices=['Accept', 'Reroll'], default=['Accept']
        )
    }
    answer = inquirer.prompt(choice_menu)

    if answer['menu'] == 'Reroll':
        return True
    else:
        return False

def randomizer_question(question_text):
    result = reroll_childhood(question_text)
    does_player_reroll = randomizer_reroll(question_text)
    while does_player_reroll == True:
        result = reroll_childhood(question_text)
        does_player_reroll = randomizer_reroll(question_text)
    return result



print(f'pc_childhood is {pc_childhood}')
reroll_childhood(pc_childhood)
print('Rerolling...')
print(f'pc_childhood is now {pc_childhood}')


randomizer_question(pc_childhood)


# pc_growup = pc_childhood.append(Childhood.growup)
# print(pc_growup)
  
# player_char.childhood = ask_reroll(pc_childhood, Childhood)



# player_char.parents = creator_question('Status of your parents: ', ParentsStatus)

# match player_char.parents_status:
#     case ParentsStatus.ALIVE:
#         print('Lucky you!')
#         pass
#     case ParentsStatus.INCIDENT:
#         print('Something happened to your parents.')
