from char_creation_menus import *
from char_creation_rollers import *
from general_functions import *
from char_save_data import *
from char_properties import *
from class_definitions import *

char_question("Select race: ", )

# Player.roll_race()
player = Player()
player.roll_race()
origin, origin_index = player.roll_attribute(Player.human_origins)
print(f'Creating a new player...')
print(f'Race: {player.race}, Index: {player.race_index}, Origin: {origin}')

for _ in range(5):
    event = EventFactory.create_event()
    print(f'Created a {event.event_type} event.')