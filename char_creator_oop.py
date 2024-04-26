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
    does_player_reroll = True
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


def generate_parents():
    # pc_childhood starts empty
    pc_childhood = ''
    print('Generating parents...')
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

    num_parents = 2

    player_char.bg_birth = Birth.random()
    
    match player_char.bg_birth:
        case Birth.ORPHAN:
            pc_childhood += 'You are an orphan.'
            pc_parent2=None
            pc_parent1=None
        case Birth.BORN:
            s = "s" if num_parents > 1 else ""
            pc_childhood += f"As a {player_char.race}, you were born to {num_parents} {player_char.race} parent{s}.\n"
            for parent in pc_parent1, pc_parent2:
                if parent:
                    if parent.gender == Gender.FEMALE: 
                        pc_childhood += "Your mother is a {}.\n".format(parent.job)
                    elif parent.gender == Gender.MALE: 
                        pc_childhood += "Your father is a {}.\n".format(parent.job)
                    else:
                        pc_childhood += "Your non-binary parent is a {}.\n".format(parent.job)
        case Birth.ADOPTED:
            pc_parent2 = random.choice([None, pc_parent2])
            num_parents = bool(pc_parent1) + bool(pc_parent2)

            for parent in pc_parent1, pc_parent2:
                if parent:
                    parent.race = Race.random()
                    parent.gender = Gender.random()

            s = "s" if num_parents > 1 else ""
            pc_childhood += "You are a {}, but you were adopted by {} parent{}.\n".format(player_char.race, num_parents, s)
            for parent in pc_parent1, pc_parent2:
                if parent:
                    if parent.gender == Gender.FEMALE: 
                        pc_childhood += "Your mother is a {} {}.\n".format(parent.race,parent.job)
                    elif parent.gender == Gender.MALE: 
                        pc_childhood += "Your father is a {} {}.\n".format(parent.race,parent.job)
                    else:
                        pc_childhood += "Your parent is a non-binary {} {}.\n".format(parent.race,parent.job)
        case _:
            print ('This should never happen.')
  
    parents = []
    for parent in pc_parent1, pc_parent2:
        if parent:
            parents.append(parent)
    finished_childhood = pc_childhood
    print(finished_childhood)
    return finished_childhood, parents


def reroll_childhood(childhood):
    rerolled_childhood = generate_parents()
    return rerolled_childhood

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
    does_player_reroll = True
    while does_player_reroll == True:
        result, parents = generate_parents()
        does_player_reroll = randomizer_reroll("Accept or Reroll?")
    return result, parents


# if pc_childhood: print(f'pc_childhood is {pc_childhood}')


finished_childhood, parents = randomizer_question('Your childhood growing up:')

player_char.bg_childhood = finished_childhood
print('Player background accepted and saved.')

print('Saving parents data...')
# print(len(parents))
# # if parents[0] in parents: 
#     pc_parent1 = Parent(parents[0].gender, parents[0].race, parents[0].job)
#     print('Saved {}, a {} {} {}.'.format('pc_parent1', pc_parent1.gender, pc_parent1.race, pc_parent1.job))
# if parents[1] in parents: 
#     pc_parent2 = Parent(parents[1].gender, parents[1].race, parents[1].job)
#     print('Saved {}, a {} {} {}.'.format('pc_parent2', pc_parent2.gender, pc_parent2.race, pc_parent2.job))

print(f'len(parents) is {len(parents)}')
if len(parents) == 0:
    print('Orphan!')
elif len(parents) >= 1:
    pc_parent1 = Parent(parents[0].gender, parents[0].race, parents[0].job)
    print('Saved {}, a {} {} {}.'.format('pc_parent1', pc_parent1.gender, pc_parent1.race, pc_parent1.job))
elif len(parents) >= 2:
    pc_parent2 = Parent(parents[1].gender, parents[1].race, parents[1].job)
    print('Saved {}, a {} {} {}.'.format('pc_parent2', pc_parent2.gender, pc_parent2.race, pc_parent2.job))

# for i in len(parents):
#     pc_parent = Parent(parents[i].gender, parents[i].race, parents[i].job)
#     print('Saved {}, a {} {} {}.'.format('pc_parent1', pc_parent1.gender, pc_parent1.race, pc_parent1.job))


# print(player_char.bg_childhood)


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
