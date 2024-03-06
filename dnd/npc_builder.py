from dnd.class_enums import WeightedEnum
from dnd.gender import Gender
from dnd.jobs_menu import PlayerJob, AllyJob, NPCJob

class NPC(WeightedEnum):

    # ===OUTLINE==
        # A character consists of:
        # A name
            # Parents share same last name as player
        # A gender
            # STATIC: Father and Mother have predefined gender. What about gay couples? Does that fall under Adoption? :think:
        # A race
            # Parents share same race as player UNLESS player is adopted
        # A job
            # Different job lists for Ally, Parents, and Enemy. Should Siblings have a job?
    
        # Relation to player
            # Ally: Meeting circumstance
            # Enemy: Cause of aggression
            # Current Fate: Seeking the player? Hunting the player? Adventuring with the player? Dead?
        

    def __init__(self):
        self.name = char_name


    @staticmethod
    def create_parent(gender=None, race='Human', age=None, job=None, biological=True):
        # race = Player.race
        if biological == True:
            race = Character.roll_race


# def roll_ally(ally_gender): 
#     if ally_gender[1] == 0: # Male
#         he_she = 'he'
#         him_her = 'him'
#         his_hers = 'his'
#         is_are = 'is'
#     elif ally_gender[1] == 1: # Female
#         he_she = 'she'
#         him_her = 'her'
#         his_hers = 'hers'
#         is_are = 'is'
#     else: # Nonbinary
#         he_she = 'they'
#         him_her = 'them'
#         his_hers = 'their'
#         is_are = 'are'
#     ally_race = roller(races)
#     ally_position = {
#         'Bounty Hunter':10,
#         'Mage':10,
#         'Mentor or Teacher':10,
#         'Childhood Friend':10,
#         'Craftsman or Merchant':10,
#         'Former Enemy':10,
#         'Noble':10,
#         'Peasant':10,
#         'Soldier':10,
#         'Bard':10
#     }
#     ally_meeting = {
#         f'You saved {him_her} from something':10,
#         f'{he_she} saved you from something':10,
#         f'you met {him_her} in a tavern':10,
#         f'You fought together against something':10,
#         f'You were trapped together somehow':10,
#         f'You met while traveling':10,
#         f'You hired {him_her} to do something':10,
#         f'{he_she} hired you to do something':10,
#         f'You fought against each other and came to mutual respect through combat':10,
#         f'You were forced to work together':10
#     }
#     ally_relationship = {
#         'Acquaintances':40,
#         'Friends':20,
#         'Close Friends':20,
#         'Inseperable':10,
#         'Sworn companions/partners':10
#     }

#     ally_locations = {
#         'a nearby town':30,
#         'the country\'s grand capitol':30,
#         'a peaceful village':20,
#         'a small hut in the middle of nowhere':10
#     }
#     al_location_tuple = roller(ally_locations)
#     al_location = al_location_tuple[0]
#     ally_fate = {
#         f'{he_she} {is_are} gone in a far-off land':30,
#         f'{he_she} {is_are} frequently somewhere nearby when you least expect {him_her}':25,
#         f'{he_she} settled down in {al_location}.':30,
#         f'{he_she} wanders the roads of adventure like you. Who knows where {he_she} {is_are} now?':10,
#         f'Surprise! {he_she} {is_are} travelling with you as a party member! Work with your Game Master to create this character.':5
#     }




#     # al_gender_tuple = roller(gender)
#     # al_gender = al_gender_tuple[0]
#     al_position_tuple = roller(ally_position)
#     al_position = al_position_tuple[0]
#     al_meeting_tuple = roller(ally_meeting)
#     al_meeting = al_meeting_tuple[0]
#     al_relationship_tuple = roller(ally_relationship)
#     al_relationship = al_relationship_tuple[0]
#     al_race = ally_race[0]

#     al_fate_tuple = roller(ally_fate)
#     al_fate = al_fate_tuple[0]


#     complete_ally = [
#         ally_gender[0],
#         al_race,
#         al_position,
#         al_meeting,
#         al_relationship,
#         al_location,
#         al_fate
#     ]
#     return complete_ally

# # An ENEMY consists of:
#     # Gender: Male or Female
#     # 1/10 possible position/relationships-to-you
#     # Power level on a scale of 1-10
#     # Nature of their power
#     # Conflict:
#         # 1/10 possible Causes
#         # Who was wronged
#         # How far has it escalated?

# # enemy_position = {
# #     'Former Friend':10,
# #     'Former Lover':10,
# #     'Relative':10,
# #     'Childhood Enemy':10,
# #     'A Bandit':10,
# #     'A Noble':10,
# #     'A Mage':10,
# #     'A Sentient Monster':5,
# #     'A Soldier':10,
# #     'A prevoiusly defeated villain':5
# # }

# enemy_position = {
#     'Position 1':10,
#     'Position 2':10,
#     'Position 3':10,
#     'Position 4':10,
#     'Position 5':10,
#     'Position 6':10,
#     'Position 7':10,
#     'Position 8':10,
#     'A Sentient Monster':5,
#     'A prevoiusly defeated villain':5
# }
# enemy_power = [1,2,3,4,5,6,7,8,9,10]

# enemy_strength = {
#     'Social Power':20,
#     'Knowledge':20,
#     'Physical':30,
#     'Minions':20,
#     'Magic':10
# }
# # enemy_conflict_cause = {
# #     'Assaulted the offended party':10,
# #     'Caused the loss of a loved one':10,
# #     'A major humiliation':10,
# #     'Caused a monster attack':10,
# #     'Romantic rejection':10,
# #     'Accused of witchcraft':10,
# #     'Blackmail':10,
# #     'Grievous wound':10,
# #     'Foiled plans':10,
# #     'Cursed':10
# # }
# enemy_conflict_cause = {
#     'Conflict Cause ':10,
#     'Conflict Cause ':10,
#     'Conflict Cause ':10,
#     'Conflict Cause ':10,
#     'Conflict Cause ':10,
#     'Conflict Cause ':10,
#     'Conflict Cause ':10,
#     'Conflict Cause ':10,
#     'Conflict Cause ':10,
#     'Conflict Cause ':10
# }
# enemy_conflict_victim = {
#     'The enemy wronged you':50,
#     'You wronged the enemy':50
# }
# enemy_conflict_escalation = {
#     'Conflict has mostly been forgotten':20,
#     'They/You plan to Backstab':20,
#     'They/You will attack if encountered':30,
#     'They/You are hunting for revenge':20,
#     'They/You are out for blood':20
# }