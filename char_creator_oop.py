from dnd import __char_data__
from dnd import __event_data__


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

