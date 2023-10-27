import random
# from char_properties import Character
# from char_creator import roll

# RACE DATA

races = {
    'Human':20,
    'Elf':10,
    'Dwarf':10,
    'Halfling':10,
    'Gnome':10,
    'Dragonborn':5,
    'Orc':10,
    'Goblin':10,
    'Kobold':10,
    'Gnoll':5
}

# ORIGIN DATA

human_origins = {
    'You are from Waterdeep, the City of Splendors.':40,
    'You are from Baldur\'s Gate.':20,
    'You are from Varisia, the Lands of Adventure':30,
    'You are from the Mwangi Expanse, the dense jungle heartland.':10
}
fey_origins = {
    'You are from Sherwood Forest, and were raised under the cruel thumb of the King\'s tax collectors.':50,
    'You are from Lothlorien, the final bastion of your dying people.':50
}
savage_origins = {
    'You grew up always fighting for survival, scrabbling together a life in the dirt and gutter of society.':35,
    'You grew up the child of a powerful warrior, and everyone expected you to live up to their accomplishments.':25,
    'You grew up C':25,
    'You grew up D:':15
}
urban_flavor = {
    'The city was cramped, dirty, poor and vicious.':70,
    'The city was rich and opulent. You lived like nobility.':30
}
wild_flavor = {
    'You lived in harmony with nature. The animals were your childhood friends.':70,
    'Growing up in the wild taught you to be tough and self-sufficient.':30
}
savage_flavor = {
    'Life in your homeland was tough. You had to fight to survive.':30,
    'Only the strongest survive. You did whatever necessary to be the best.':70
}



#  HOMELAND DATA

human_homes = {
        'Faerun':50,
        'Golarion':50
}
fey_homes = {
        'Forest':55,
        'Mountains':15,
        'Ocean':20,
        'Jungle':10
}
savage_homes = {
        'Badlands':25,
        'Swamps':15,
        'Ruins':10,
        'War Camp':25,
        'Underground Caverns':25
}



#  FAMILY DATA

family_status = {
    'Your family is alive and well.':30,
    'Something happened to your family.':70
}
family_fate_human = {
    'Human family fate 1':25,
    'Human family fate 2':25,
    'Human family fate 3':25,
    'Human family fate 4':25
}
family_fate_fey = {
    'Fey family fate 1':30,
    'Fey family fate 2':30,
    'Fey family fate 3':30,
    'Fey family fate 4':10
}
family_fate_savage = {
    'Savage family fate 1':30,
    'Savage family fate 2':30,
    'Savage family fate 3':30,
    'Savage family fate 4':10
}

parents_status = {
    'Your parents are alive.':30,
    'Something happened to your parents.':70
}
parents_fate = {
    'Something happened to your father':50,
    'Something happened to your mother':50
}
father_fate = {
    'A thing happened to your father 1':25,
    'A thing happened to your father 2':25,
    'A thing happened to your father 3':25,
    'A thing happened to your father 4':25
}
mother_fate = {
    'A thing happened to your mother 1':25,
    'A thing happened to your mother 2':25,
    'A thing happened to your mother 3':25,
    'A thing happened to your mother 4':25
}

family_event = {
    'An event happened to your family 1':25,
    'An event happened to your family 2':25,
    'An event happened to your family 3':25,
    'An event happened to your family 4':25
}
siblings_human = {
    'You have {1} sibling':40,
    'You have no siblings':40,
    'You have {2} siblings':20
}
# sibling details
sibling_gender = {'Male':50, 'Female':50},
sibling_age = {'Younger than you':40, 'Older than you':50, 'Twins':10},
sibling_personality = {
    'Quirky':25,
    'Evil':10,
    'Prankster':25,
    'Compassionate':15
},
sibling_attitude = {
    'Hates you':10,
    'Loves you':60,
    'Jealous of you':30
}
fortune_misfortune = {
    'Fortune':50,
    'Misfortune':50
}


#  LIFE EVENT DATA
life_event = {
    'Fortune or Misfortune':50,
    'Allies and Enemies':25,
    'Romance':25
}


#  #########
#  FORTUNES
#  #########


#  Random variables
d10 = random.randint(1,10)
gold = d10 * 100

# Random table for tamed wild animal
wild_animal = {
    'Wild Dog':50,
    'Wolf':50
}
wild_animal_result = str(random.choices(list(wild_animal.keys()), weights=wild_animal.values(), k=1))




fortunes = {
    f'Fortune 1: Gain {gold} gold pieces':10,
    'Fortune 2':10,
    'Fortune 3':10,
    'Fortune 4':10,
    'Fortune 5':10,
    'Fortune 6':10,
    f'Fortune 7: Tamed a: {wild_animal_result}':10,
    'Fortune 8':10, 
    'Fortune 9':10,
    'Fortune 10':10
}




victim_choices = {'Friend':50,'Lover':30,'Relative':20}
victim = random.choices(list(victim_choices.keys()), weights=victim_choices.values(), k=1)

causeofdeath_choices = {'an accident':30, 'monsters':30, 'bandits':40}
causeofdeath = random.choices(list(causeofdeath_choices.keys()), weights=causeofdeath_choices.values(), k=1)

false_crime_choices = {'theft':30, 'cowardice or betrayal':20, 'murder':10, 'assault':30, 'witchcraft':10}
false_crime = random.choices(list(false_crime_choices.keys()), weights=false_crime_choices.values(), k=1)

law_hunters_choices = {'a few guards':30, 'a small town':40, 'a major city':20, 'an entire kingdom':10}
law_hunters = random.choices(list(law_hunters_choices.keys()), weights=law_hunters_choices.values(), k=1)

betrayal_choices = {'a family member':20, 'a friend':30, 'a loved one':10, 'an ally':40}
betrayer = random.choices(list(betrayal_choices.keys()), weights=betrayal_choices.values(), k=1)

months = d10 * 5
accident_choices = {'A spell went off in your face. You are Disfigured.':30, 
    f'You were attacked by a wolf pack and it took {months} months to heal.':40,
    f'You fell off a roof and suffered amnesia. You forgot {d10} months of your life.':30}
accident = random.choices(list(accident_choices.keys()), weights=accident_choices.values(), k=1)

incap_choices = {'You broke your arm.':30, 'You broke your leg.':30, 'You broke your nose.':40}
incap = random.choices(list(incap_choices.keys()), weights=incap_choices.values(), k=1)


misfortunes = {
    f'Misfortune 1: In debt for {gold} gold pieces':15,
    f'Misfortune 2: Imprisoned for {d10} months':10,
    f'Misfortune 3: You got some mud splashed on you, ruining your favorite shirt!':10,
    f'Misfortune 4: Your {victim[0]} was killed by {causeofdeath[0]}.':10,
    f'Misfortune 5: You were falsely accused of {false_crime[0]} and were imprisoned for {d10} months':10,
    f'Misfortune 6: You committed some crime and were hunted by law enforcement of {law_hunters[0]}':10,
    f'Misfortune 7: You were betrayed somehow by {betrayer[0]}':10,
    f'Misfortune 8: You had a horrible accident. {accident[0]}':10, 
    f'Misfortune 9: You had a bad accident and were incapacitated for {d10} months. {incap[0]}':10,
    f'Misfortune 10: You were cursed.':5
}


#  ###################
#  ALLIES AND ENEMIES
#  ###################

gender = {
    'Male':45,
    'Female':45,
    'Nonbinary':10
}
allegiance = {
    'Ally':50,
    'Enemy':50
}

# Outline
#  An ALLY consists of:
    #  Gender: Male or Female
    #  1/10 possible positions/jobs
    #  1/10 possible meeting circumstances
    # How close is the relationship
    # Ally's current location/region/fate


# he_she
# him_her
# his_hers
def roller(dictionary):
    # When provided with a dictionary consisting of Keys as strings adn Values as probabilities-out-of-100, roll according to probabilities and output the result.
    rolled = random.choices(list(dictionary.keys()), weights=dictionary.values(), k=1)
    rolled_string = rolled[0] # just the string of the result

    dict_items = list(dictionary.items())
    rolled_index = [id for id, key in enumerate(dict_items) if key[0] == rolled_string] # index of the result, used for conditionally targeting specific table results 
    # [ex. favorite drink; if you roll Milk, stop; if you roll Soda, ask what kind]

    # pack both string and index into a tuple for export
    return (rolled_string, rolled_index[0])

def roll_ally(ally_gender): 
    if ally_gender[1] == 0: # Male
        he_she = 'he'
        him_her = 'him'
        his_hers = 'his'
        is_are = 'is'
    elif ally_gender[1] == 1: # Female
        he_she = 'she'
        him_her = 'her'
        his_hers = 'hers'
        is_are = 'is'
    else: # Nonbinary
        he_she = 'they'
        him_her = 'them'
        his_hers = 'their'
        is_are = 'are'
    ally_position = {
        'Bounty Hunter':10,
        'Mage':10,
        'Mentor or Teacher':10,
        'Childhood Friend':10,
        'Craftsman or Merchant':10,
        'Former Enemy':10,
        'Noble':10,
        'Peasant':10,
        'Soldier':10,
        'Bard':10
    }
    ally_meeting = {
        f'You saved {him_her} from something':10,
        f'{he_she} saved you from something':10,
        f'you met {him_her} in a tavern':10,
        f'You fought together against something':10,
        f'You were trapped together somehow':10,
        f'You met while traveling':10,
        f'You hired {him_her} to do something':10,
        f'{he_she} hired you to do something':10,
        f'You fought against each other and came to mutual respect through combat':10,
        f'You were forced to work together':10
    }
    ally_relationship = {
        'Acquaintances':40,
        'Friends':20,
        'Close Friends':20,
        'Inseperable':10,
        'Sworn companions/partners':10
    }

    ally_locations = {
        'a nearby town':30,
        'the country\'s grand capitol':30,
        'a peaceful village':20,
        'a small hut in the middle of nowhere':10
    }
    al_location_tuple = roller(ally_locations)
    al_location = al_location_tuple[0]
    ally_fate = {
        f'{he_she} {is_are} gone in a far-off land':30,
        f'{he_she} {is_are} frequently somewhere nearby when you least expect {him_her}':25,
        f'{he_she} settled down in {al_location}.':30,
        f'{he_she} wanders the roads of adventure like you. Who knows where {he_she} {is_are} now?':10,
        f'Surprise! {he_she} {is_are} travelling with you as a party member! Work with your Game Master to create this character.':5
    }




    # al_gender_tuple = roller(gender)
    # al_gender = al_gender_tuple[0]
    al_position_tuple = roller(ally_position)
    al_position = al_position_tuple[0]
    al_meeting_tuple = roller(ally_meeting)
    al_meeting = al_meeting_tuple[0]
    al_relationship_tuple = roller(ally_relationship)
    al_relationship = al_relationship_tuple[0]

    al_fate_tuple = roller(ally_fate)
    al_fate = al_fate_tuple[0]


    complete_ally = [
        ally_gender[0],
        al_position,
        al_meeting,
        al_relationship,
        al_location,
        al_fate
    ]
    return complete_ally

# An ENEMY consists of:
    # Gender: Male or Female
    # 1/10 possible position/relationships-to-you
    # Power level on a scale of 1-10
    # Nature of their power
    # Conflict:
        # 1/10 possible Causes
        # Who was wronged
        # How far has it escalated?

# enemy_position = {
#     'Former Friend':10,
#     'Former Lover':10,
#     'Relative':10,
#     'Childhood Enemy':10,
#     'A Bandit':10,
#     'A Noble':10,
#     'A Mage':10,
#     'A Sentient Monster':5,
#     'A Soldier':10,
#     'A prevoiusly defeated villain':5
# }

enemy_position = {
    'Position 1':10,
    'Position 2':10,
    'Position 3':10,
    'Position 4':10,
    'Position 5':10,
    'Position 6':10,
    'Position 7':10,
    'Position 8':10,
    'A Sentient Monster':5,
    'A prevoiusly defeated villain':5
}
enemy_power = [1,2,3,4,5,6,7,8,9,10]

enemy_strength = {
    'Social Power':20,
    'Knowledge':20,
    'Physical':30,
    'Minions':20,
    'Magic':10
}
# enemy_conflict_cause = {
#     'Assaulted the offended party':10,
#     'Caused the loss of a loved one':10,
#     'A major humiliation':10,
#     'Caused a monster attack':10,
#     'Romantic rejection':10,
#     'Accused of witchcraft':10,
#     'Blackmail':10,
#     'Grievous wound':10,
#     'Foiled plans':10,
#     'Cursed':10
# }
enemy_conflict_cause = {
    'Conflict Cause ':10,
    'Conflict Cause ':10,
    'Conflict Cause ':10,
    'Conflict Cause ':10,
    'Conflict Cause ':10,
    'Conflict Cause ':10,
    'Conflict Cause ':10,
    'Conflict Cause ':10,
    'Conflict Cause ':10,
    'Conflict Cause ':10
}
enemy_conflict_victim = {
    'The enemy wronged you':50,
    'You wronged the enemy':50
}
enemy_conflict_escalation = {
    'Conflict has mostly been forgotten':20,
    'They/You plan to Backstab':20,
    'They/You will attack if encountered':30,
    'They/You are hunting for revenge':20,
    'They/You are out for blood':20
}




#  ##########
#  ROMANCE
#  ########

romance_type = {
    'A happy love affair':10,
    'A romantic tragedy':30,
    'A problematic romance':20,
    'Sleeping around':40
}

romantic_tragedy = {
    'Tragedy 1':10,
    'Tragedy 2':10,
    'Tragedy 3':10,
    'Tragedy 4':10,
    'Tragedy 5':10,
    'Tragedy 6':10,
    'Tragedy 7':10,
    'Tragedy 8':10,
    'Tragedy 9':10,
    'Tragedy 10':10,
}
problematic_love = {
    'Romantic Problems 1':10,
    'Romantic Problems 2':10,
    'Romantic Problems 3':10,
    'Romantic Problems 4':10,
    'Romantic Problems 5':10,
    'Romantic Problems 6':10,
    'Romantic Problems 7':10,
    'Romantic Problems 8':10,
    'Romantic Problems 9':10,
    'Romantic Problems 10':10,
}