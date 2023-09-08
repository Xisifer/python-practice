
# RACE DATA

races = [
    'Human',
    'Elf',
    'Dwarf',
    'Halfling',
    'Gnome',
    'Dragonborn',
    'Orc',
    'Goblin',
    'Kobold',
    'Gnoll'
]

# ORIGIN DATA

human_origins = [
    'You are from Waterdeep, the City of Splendors.',
    'You are from Baldur\'s Gate.',
    'You are from Varisia, the Lands of Adventure',
    'You are from the Mwangi Expanse, the dense jungle heartland.'
]
fey_origins = [
    'You are from Sherwood Forest, and were raised under the cruel thumb of the King\'s tax collectors.',
    'You are from Lothlorien, the final bastion of your dying people.'
]
savage_origins = [
    'You grew up always fighting for survival, scrabbling together a life in the dirt and gutter of society.',
    'You grew up the child of a powerful warrior, and everyone expected you to live up to their accomplishments.',
    'You grew up C',
    'You grew up D'
]
urban_flavor = [
    'The city was cramped, dirty, poor and vicious.',
    'The city was rich and opulent. You lived like nobility.'
]
wild_flavor = [
    'You lived in harmony with nature. The animals were your childhood friends.',
    'Growing up in the wild taught you to be tough and self-sufficient.'
]
savage_flavor = [
    'Life in the {homeland} was tough. You fought to survive.',
    'Only the strongest survive. You did whatever necessary to be the best.'
]



#  HOMELAND DATA

human_homes = [
        'Faerun',
        'Golarion'
]
fey_homes = [
        'Forest',
        'Mountains',
        'Ocean',
        'Jungle'
]
savage_homes = [
        'Badlands',
        'Swamps',
        'Ruins',
        'War Camp',
        'Underground Caverns'
]



#  FAMILY DATA

family_status = [
    'Your family is alive and well.',
    'Something happened to your family.'
]
family_fate_human = [
    'Human family fate 1',
    'Human family fate 2',
    'Human family fate 3',
    'Human family fate 4'
]
family_fate_fey = [
    'Fey family fate 1',
    'Fey family fate 2',
    'Fey family fate 3',
    'Fey family fate 4'
]
family_fate_savage = [
    'Savage family fate 1',
    'Savage family fate 2',
    'Savage family fate 3',
    'Savage family fate 4'
]

parents_status = [
    'Your parents are alive.',
    'Something happened to your parents.'
]
parents_fate = [
    'Something happened to your father',
    'Something happened to your mother'
]
father_fate = [
    'A thing happened to your father 1',
    'A thing happened to your father 2',
    'A thing happened to your father 3',
    'A thing happened to your father 4'
]
mother_fate = [
    'A thing happened to your mother 1',
    'A thing happened to your mother 2',
    'A thing happened to your mother 3',
    'A thing happened to your mother 4'
]

family_event = [
    'An event happened to your family 1',
    'An event happened to your family 2',
    'An event happened to your family 3',
    'An event happened to your family 4'
]
siblings_human = [
    'You have {1} sibling',
    'You have no siblings',
    'You have {2} siblings'
]
# sibling details
sibling_gender = ['Male', 'Female'],
sibling_age = ['Younger than you', 'Older than you', 'Twins'],
sibling_personality = [
    'Quirky',
    'Evil',
    'Prankster',
    'Compassionate'
],
sibling_attitude = [
    'Hates you',
    'Loves you',
    'Jealous of you'
]



#  LIFE EVENT DATA
life_event = [
    'Fortune or Misfortune',
    'Allies and Enemies',
    'Romance'
]
d10 = random.randint(1,10)
gold = d10 * 100
wild_animal = [
    'Wild Dog',
    'Wolf'
]
wild_animal_result = str(random.choice(wild_animal))
fortunes = [
    f'Fortune 1: Gain {gold} gold pieces',
    'Fortune 2',
    'Fortune 3',
    'Fortune 4',
    'Fortune 5',
    'Fortune 6',
    f'Fortune 7: Tamed a: {wild_animal_result}',
    'Fortune 8', 
    'Fortune 9',
    'Fortune 10'
]



misfortunes = [
    f'Misfortune 1: In debt for {gold} gold pieces',
    f'Misfortune 2: Imprisoned for {d10} months',
    f'Misfortune 3: You got some mud splashed on you, ruining your favorite shirt!',
    f'Misfortune 4: Your {victim} was killed by {causeofdeath}.',
    f'Misfortune 5: You were falsely accused of {false_crime} and were imprisoned for {d10} months',
    f'Misfortune 6: You committed some crime and were hunted by law enforcement of {law_hunters}',
    f'Misfortune 7: You were betrayed somehow by {betrayer}',
    f'Misfortune 8: You had a horrible accident. {accident}', 
    f'Misfortune 9: You had a bad accident and were incapacitated for {d10} months. {incap}',
    f'Misfortune 10: You were cursed.'
]

victim_choices = ['Friend','Lover','Relative']
victim = random.choice(victim_choices)
causeofdeath_choices = ['an accident', 'monsters', 'bandits']
causeofdeath = random.choice(causeofdeath_choices)
false_crime_choices = ['theft', 'cowardice or betrayal', 'murder', 'assault', 'witchcraft']
false_crime = random.choice(false_crime_choices)
law_hunters_choices = ['a few guards', 'a small town', 'a major city', 'an entire kingdom']
law_hunters = random.choice(law_hunters_choices)
betrayal_choices = ['a family member', 'a friend', 'a loved one', 'an ally']
betrayer = random.choice(betrayal_choices)
months = d10 * 5



accident_choices = ['A spell went off in your face. You are Disfigured.', 
    f'You were attacked by a wolf pack and it took {months} to heal.',
    f'You fell off a roof and suffered amnesia. You forgot {d10} months of your life.']
accident = random.choice(accident_choices)
incap_choices = ['You broke your arm.', 'You broke your leg.', 'You broke your nose.']
incap = random.choice(incap_choices)