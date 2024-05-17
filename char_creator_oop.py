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
from dnd.appearance import HairColor, EyeColor, SkinColor, ScalesColor

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



def generate_appearance():

    pc_appearance = []
    
    match player_char.race:
        case Race.HUMAN:
            pc_appearance_eyes = EyeColor.random()
            pc_appearance_hair = HairColor.random()
            pc_appearance_skin = SkinColor.random()

        case Race.ELF | Race.HALFLING | Race.GNOME:
            pc_appearance_eyes = EyeColor.random()
        
        case Race.DRAGONBORN | Race.ORC | Race.GOBLIN | Race.KOBOLD | Race.GNOLL:
            pc_appearance_eyes = EyeColor.random()

        case _:
            print('ERROR')

    return pc_appearance

# ===================================================
# Parents and Family



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


finished_childhood, parents = randomizer_question('Your childhood growing up:')

player_char.bg_birth = finished_childhood
print('Player background accepted and saved.')

print('Saving parents data...')
# print(len(parents))
# # if parents[0] in parents: 
#     pc_parent1 = Parent(parents[0].gender, parents[0].race, parents[0].job)
#     print('Saved {}, a {} {} {}.'.format('pc_parent1', pc_parent1.gender, pc_parent1.race, pc_parent1.job))
# if parents[1] in parents: 
#     pc_parent2 = Parent(parents[1].gender, parents[1].race, parents[1].job)
#     print('Saved {}, a {} {} {}.'.format('pc_parent2', pc_parent2.gender, pc_parent2.race, pc_parent2.job))

# print(f'len(parents) is {len(parents)}')
if len(parents) == 0:
    print('Orphan!')
elif len(parents) == 1:
    pc_parent1 = Parent(parents[0].gender, parents[0].race, parents[0].job)
    print('Saved {}, a {} {} {}.'.format('pc_parent1', pc_parent1.gender, pc_parent1.race, pc_parent1.job))
elif len(parents) == 2:
    pc_parent1 = Parent(parents[0].gender, parents[0].race, parents[0].job)
    print('Saved {}, a {} {} {}.'.format('pc_parent1', pc_parent1.gender, pc_parent1.race, pc_parent1.job))
    pc_parent2 = Parent(parents[1].gender, parents[1].race, parents[1].job)
    print('Saved {}, a {} {} {}.'.format('pc_parent2', pc_parent2.gender, pc_parent2.race, pc_parent2.job))



# print(pc_growup)
  
# player_char.childhood = ask_reroll(pc_childhood, Childhood)

# player_char.parents = creator_question('Status of your parents: ', ParentsStatus)

# match player_char.parents_status:
#     case ParentsStatus.ALIVE:
#         print('Lucky you!')
#         pass
#     case ParentsStatus.INCIDENT:
#         print('Something happened to your parents.')


player_char.bg_childhood = creator_question('As a child, ', Childhood)
print('When you were growing up...')
print('')

player_char.childhood = ""

player_char.job = creator_question('Your class: ', PlayerJob)


# You were born in the month of [sign] (Aspects: A, B, C. Game effects: A, B, C) to be a [gender] [race]. You have [color] hair, [color] eyes and a [color] complexion.
# Your parents belonged to the lower class. They were honest hard-working people, who did everything to enable you to live a comfortable and fine life. They were not very succesful.
# As a child you had to survive pretty harsh times since your parents seemed to have run out of luck. Their wealth was ever-declining and times were very hard.
# During your youth you had lots of fun playing with other kids of your age. You always wer a natural leader and the enter of interest.
# As a young adult, you tried many occupations before finally deciding on one to pursur. This has left you with a vrey broad base of lore.
# At the age of [num] you end your apprenticeship. You are now a fully learned [class].

