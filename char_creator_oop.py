# from dnd.general_functions import *

# from dnd import char_data
import inquirer
from dnd.player_class import Player
from dnd.life_events import LifeEvent
from dnd.character_class import Character
from dnd.race import Race
from dnd.origin_human import HumanOrigins
from dnd.

def ask_reroll(question_text, roll_result):
    choice_menu = {
        inquirer.List('menu',
                    message=f'{question_text} {roll_result}',
                    choices=['Accept', 'Reroll'], default=['Accept']
        )
    }
    answer = inquirer.prompt(choice_menu)

    if answer['menu'] == 'Reroll':
        print('Rerolling...')
        return True
    else:
        return False


rolled_race = Race.random()
does_player_reroll = ask_reroll("Select race: ", rolled_race)
while does_player_reroll == True:
    print('Reroll!')
    rolled_race = Race.random()
    does_player_reroll = ask_reroll('Select race: ', rolled_race)
print(f'Accepted player race is {rolled_race}')



player_background = HumanOrigins.random()