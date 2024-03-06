import inquirer
import random
from dnd.player_class import Player
from dnd.life_events import LifeEvent
from dnd.character_class import Character
from dnd.race import Race
from dnd.childhood import Childhood
from dnd.origin_human import HumanOrigins, HumanFlavor, HumanHomes
from dnd.origin_fey import FeyOrigins, FeyFlavor, FeyHomes
from dnd.origin_savage import SavageOrigins, SavageFlavor, SavageHomes
from dnd.parents_status import ParentsStatus
from dnd.parent_class import Parent
from dnd.jobs_menu import PlayerJob, NPCJob, AllyJob


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

player_char.name = name_input()

player_char.race = creator_question('Select race: ', Race)

player_char.bg_childhood = creator_question('Your origin: ', Childhood)

match player_char.race:
    case Race.HUMAN:
        player_char.bg_homeland = creator_question('You hail from ', HumanHomes)
        player_char.bg_origin = creator_question('You were raised in ', HumanOrigins)
        player_char.bg_flavor = creator_question('As you were growing up, ', HumanFlavor)


    case Race.ELF | Race.HALFLING | Race.GNOME:
        player_char.bg_homeland = creator_question('You hail from ', FeyHomes)
        player_char.bg_origin = creator_question('You were raised in ', FeyOrigins)
        player_char.bg_flavor = creator_question('As you were growing up, ', FeyFlavor)
    
    case Race.DRAGONBORN | Race.ORC | Race.GOBLIN | Race.KOBOLD | Race.GNOLL:
        player_char.bg_homeland = creator_question('You hail from ', SavageHomes)
        player_char.bg_origin = creator_question('You were raised in ', SavageOrigins)
        player_char.bg_flavor = creator_question('As you were growing up, ', SavageFlavor)

    case _:
        print('ERROR')


# Player family is composed of 0 - 2 parents and 0 - 3 siblings
player_char.parent_count = random.randint(1,2)
print(f'You were raised by {player_char.parent_count} parents.')
# Family fate

match player_char.bg_childhood:
    
    case Childhood.BORN:
        if player_char.parent_count == 1:
            pc_mother = Parent(gender='Female', race=player_char.race, job=NPCJob.random())
            print(f'Your mother is a {pc_parent.gender} {pc_parent.race} {pc_parent.job}.')
        else:
            pc_mother = Parent(gender='Female', race=player_char.race, job=NPCJob.random())
            pc_parent = Parent(gender='Male', race=player_char.race, job=NPCJob.random())


    case Childhood.ADOPTED:
        print('You were adopted.')

        pc_parent = Parent(gender='Male', race=Race.random(), job=NPCJob.random())

        print(f'Your adoptive parent is a {pc_parent.gender} {pc_parent.race} {pc_parent.job}.')

        

player_char.parents = creator_question('Status of your parents: ', ParentsStatus)

match player_char.parents_status:
    case ParentsStatus.ALIVE:
        print('Lucky you!')
        pass
    case ParentsStatus.INCIDENT:
        print('Something happened to your parents.')