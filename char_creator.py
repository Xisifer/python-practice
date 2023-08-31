import inquirer
import random
from char_properties import Character
from math import floor



def name_input():
    char_name = input("Do you want to roll dice? Y/N ")
    name_stripped = str(char_name.strip())
    print(f'You said: {name_stripped}')


def store_data(category, selection):
    print(f'Saving {selection} into character {category}...')
    Character.category = selection
    #  if category is X, store thing
    if category == 'race':
        Character.race = selection
        print(f'Data saved. Character\'s {category} is now {Character.race}')
    if category == 'home':
        Character.home = selection
        print(f'Data saved. Character\'s {category} is now {Character.home}')
    if category == 'origin':
        Character.origin = selection
        print(f'Data saved. Character\'s {category} is now {Character.origin}')
    if category == 'age':
        Character.age = selection
        print(f'Data saved. Character\'s {category} is now {Character.age}')
    if category == 'family':
        Character.family = selection
        print(f'Data saved. Character\'s {category} is now {Character.family}')
    else:
        Character.category = selection
        print(f'Character.category is {selection}')

def roll_race():
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
    race_result = str(random.choice(races))
    return race_result

def roll_homeland(race_result):
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
    match race_result:
        case 'Human' | 'Dwarf':
            char_home = str(random.choice(human_homes))
            return char_home

        case 'Elf' | 'Halfling' | 'Gnome':
            char_home = str(random.choice(fey_homes))
            return char_home
        
        case 'Dragonborn' | 'Orc' | 'Goblin' | 'Kobold' | 'Gnoll':
            char_home = str(random.choice(savage_homes))
            return char_home



def roll_origin(race_result, char_home):
    
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
    match race_result:
        case 'Human' | 'Dwarf':

            char_origin = str(random.choice(human_origins))
            print(char_origin)
            origin_flavor = str(random.choice(urban_flavor))
            print(origin_flavor)
            return char_origin

        case 'Elf' | 'Halfling' | 'Gnome':

            char_origin = str(random.choice(fey_origins))
            print(char_origin)
            origin_flavor = str(random.choice(wild_flavor))
            print(origin_flavor)
            return char_origin
        
        case 'Dragonborn' | 'Orc' | 'Goblin' | 'Kobold' | 'Gnoll':

            char_origin = str(random.choice(savage_origins))
            print(char_origin)
            origin_flavor = str(random.choice(savage_flavor))
            print(origin_flavor)
            return char_origin

def roll_family(race_result):
    family_status = [
        'Your family is alive and well.',
        'Something happened to your family.'
    ]
    char_family_status = str(random.choice(family_status))
    print(char_family_status)
    return char_family_status


    parents_status = [
        'Your parents are alive.',
        'Something happened to your parents.'
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
    

# def roll_life_events(race_result, char_age):






def ask_reroll(question_text, roll_result):
    choice_menu = {
        inquirer.List('menu',
                    message=f'{question_text} {roll_result}',
                    choices=['Accept', 'Reroll'], default=['Accept']
        )
    }
    answer = inquirer.prompt(choice_menu)

    if answer['menu'] == 'Reroll':
        print("Rerolling...")
        return True
    else:
        print("Moving on...")
        return False


def char_creation():
        






    # question 1
    retry = True
    while retry :
        question_text = 'Your character is a...'
        race_result = roll_race()
        retry = ask_reroll(question_text, race_result) 
    category = 'race'
    store_data(category, race_result)

    # question 2
    retry = True
    while retry :
        question_text = 'Your character is from...'
        char_home = roll_homeland(race_result)
        retry = ask_reroll(question_text, char_home) 
    category = 'home'
    store_data(category, char_home) 

    # question 3
    print('This RPG assumes a major noteworthy event happened to you every 5 years.')

    while True:
        try:
            char_age = input('How old is your character? (20 - 100)')
            if char_age.isdigit():
                char_age = int(char_age)
            else:
                raise ValueError()
            if 20 <= char_age <= 100:
                break
            raise ValueError()
        except ValueError:
            print('Please enter a number between 20 and 100.')


    age = 0
    life_milestones = []
    for age in range(0, char_age, 5):
        life_milestones.append(age)

    life_events_num = len(life_milestones)

    print(f'You are {char_age} years old. This means you had {life_events_num} big Life Path events.')
    print(f'You have had major life events at ages {life_milestones}')
    category = 'age'
    store_data(category, char_age)



    #  question 4
    retry = True
    while retry :
        question_text = 'Your childhood: '
        char_origin = roll_origin(race_result, char_home)
        retry = ask_reroll(question_text, char_origin) 
    category = 'origin'
    store_data(category, char_origin) 


    print('Total saved character data so far: ')

    if __name__ == '__main__':
        temp = vars(Character)
        for item in temp:
            if not item.startswith('__'):
                if not item.startswith('category'):
                    print(item , ' : ' , temp[item])




    # question 5
    retry = True
    while retry :
        question_text = 'Your family...'
        char_family = roll_family(race_result)
        retry = ask_reroll(question_text, char_family) 
    category = 'family'
    store_data(category, char_family) 











    # retry = True
    # while retry :

    #     print(f'You are a {race_result}.')



    #     match race_result:
    #         case 'Human' | 'Dwarf':
    #             print(f'Your family grew up in the human-centric areas of the world.')
    #             char_origin = str(random.choice(human_origins))
    #             return char_origin

    #         case 'Elf' | 'Halfling' | 'Gnome':
    #             print(f'You are one of the Fey races. Your family grew up in the natural world.')
    #             char_origin = str(random.choice(fey_origins))
    #             return char_origin
            
    #         case 'Dragonborn' | 'Orc' | 'Goblin' | 'Kobold' | 'Gnoll':
    #             print(f'You are one of the so-called \'savage\' races. Your family grew up in the wild, untamed realms of the world.')
    #             char_origin = str(random.choice(savage_origins))
    #             return char_origin
            
    #     retry = ask_reroll(question_text, char_origin) 
        
    #     char_origin = roll_origin(race_result)
    #     question_text = f'Your family status is: {family_status}'
    #     print(question_text)
            
    #     retry = ask_reroll(question_text, family_status) 
    # category = 'family'
    # store_data(category, char_origin) 






# ==================
# = CREATION START =
# ==================
char_creation()




# ================================================
#  Example of working "pause for user input" code
# ================================================

# player_answer = input("Do you want to roll dice? Y/N ")
# answer_stripped = str(player_answer.strip())
# print(f'You said: {answer_stripped}')

# if answer_stripped == "Y" or answer_stripped == "y": 
#     roll_results = []

#     print("Rolling 1d10...")
#     roll = random.randint(1,10)
#     roll_results.append(roll)

#     print(f'Result: {str(roll_results)}')

# else:
#     print("Dice roll cancelled.")
