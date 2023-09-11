import inquirer
import random
from char_properties import Character
from math import floor
from char_creation_menus import *

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
    'Life in the {homeland} was tough. You fought to survive.':30,
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



#  LIFE EVENT DATA
life_event = {
    'Fortune or Misfortune':60,
    'Allies and Enemies':20,
    'Romance':20
}
d10 = random.randint(1,10)
gold = d10 * 100
wild_animal = {
    'Wild Dog':50,
    'Wolf':50
}
wild_animal_result = str(random.choice(wild_animal))
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
    f'You were attacked by a wolf pack and it took {months} to heal.':40,
    f'You fell off a roof and suffered amnesia. You forgot {d10} months of your life.':30}
accident = random.choices(list(accident_choices.keys()), weights=accident_choices.values(), k=1)
incap_choices = {'You broke your arm.':30, 'You broke your leg.':30, 'You broke your nose.':40}
incap = random.choices(list(incap_choices.keys()), weights=incap_choices.values(), k=1)


misfortunes = {
    f'Misfortune 1: In debt for {gold} gold pieces':15,
    f'Misfortune 2: Imprisoned for {d10} months':10,
    f'Misfortune 3: You got some mud splashed on you, ruining your favorite shirt!':10,
    f'Misfortune 4: Your {victim} was killed by {causeofdeath}.':10,
    f'Misfortune 5: You were falsely accused of {false_crime} and were imprisoned for {d10} months':10,
    f'Misfortune 6: You committed some crime and were hunted by law enforcement of {law_hunters}':10,
    f'Misfortune 7: You were betrayed somehow by {betrayer}':10,
    f'Misfortune 8: You had a horrible accident. {accident}':10, 
    f'Misfortune 9: You had a bad accident and were incapacitated for {d10} months. {incap}':10,
    f'Misfortune 10: You were cursed.':5
}