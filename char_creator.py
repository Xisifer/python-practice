import inquirer
import random
from char_properties import Character
from math import floor
from char_creation_menus import *


# def bare_text(string):
#     print(f'bare string is {string}')
#     strip1 = string.strip('[]') # remove [dictionary brackets]
#     strip2 = strip1.strip('\"') # remove "double quotes"
#     stripped_text = strip2.strip("\'") # remove 'single quotes'
#     return stripped_text

def roll(dictionary):
    
    rolled = random.choices(list(dictionary.keys()), weights=dictionary.values(), k=1)
    rolled_string = rolled[0]
    print(f'rolled_string is: {rolled_string}')

    dict_items = list(dictionary.items())
    rolled_index = [id for id, key in enumerate(dict_items) if key[0] == rolled_string]
    print(f'rolled_index[0] is: {rolled_index[0]}')

    # pack both string and index into a tuple for export



    return (rolled_string, rolled_index[0])



def name_input():
    char_name = input("Do you want to roll dice? Y/N ")
    name_stripped = str(char_name.strip())
    print(f'You said: {name_stripped}')


def store_data(category, selection):
    print(f'Saving {selection} into character {category}...')
    Character.category = selection


    match category:
        case 'race': 
            Character.race = selection
            print(f'Data saved. Character\'s {category} is now {Character.race}')        
        case 'home': 
            Character.home = selection
            print(f'Data saved. Character\'s {category} is now {Character.home}')       
        case 'origin':
            Character.origin = selection
            print(f'Data saved. Character\'s {category} is now {Character.origin}')
        case 'age':
            Character.age = selection
            print(f'Data saved. Character\'s {category} is now {Character.age}')
        case 'family':
            Character.family = selection
            print(f'Data saved. Character\'s {category} is now {Character.family}')       
        case 'parents':
            Character.family = selection
            print(f'Data saved. Character\'s {category} is now {Character.family}')
        case _: 
            Character.category = selection
            print(f'Character.category is {selection}')


def roll_race():

    race_result = roll(races)
    return race_result

def roll_homeland(race_result):
   
    match race_result:
        case 'Human' | 'Dwarf':
            char_home = roll(human_homes)
            print(f'returning:  {char_home}')
            return char_home

        case 'Elf' | 'Halfling' | 'Gnome':
            char_home = roll(fey_homes)
            print(f'returning:  {char_home}')
            return char_home
        
        case 'Dragonborn' | 'Orc' | 'Goblin' | 'Kobold' | 'Gnoll':
            char_home = roll(savage_homes)
            print(f'returning:  {char_home}')
            return char_home
        case _:
            print('ERROR: Race not valid!')



def roll_origin(race_result, char_home):
    

    match race_result:
        case 'Human' | 'Dwarf':

            char_origin = roll(human_origins)
            print(char_origin)
            origin_flavor = roll(urban_flavor)
            print(origin_flavor)
            return char_origin

        case 'Elf' | 'Halfling' | 'Gnome':

            char_origin = roll(fey_origins)
            print(char_origin)
            origin_flavor = roll(wild_flavor)
            print(origin_flavor)
            return char_origin
        
        case 'Dragonborn' | 'Orc' | 'Goblin' | 'Kobold' | 'Gnoll':

            char_origin = roll(savage_origins)
            print(char_origin)
            origin_flavor = roll(savage_flavor)
            return char_origin

def roll_family_fate(race_result):


    char_family_status = roll(family_status)
    char_family_status_id = char_family_status[1]
    if char_family_status_id == 0:
        print('Your family is alive and well.')
        return char_family_status
    else:
        print('Something happened to your family.')
        
        match race_result:
            case 'Human' | 'Dwarf':

                char_family_fate = roll(family_fate_human)
                print(char_family_fate)

                return char_family_fate

            case 'Elf' | 'Halfling' | 'Gnome':

                char_family_fate = roll(family_fate_fey)
                print(char_family_fate)
                return char_family_fate
            
            case 'Dragonborn' | 'Orc' | 'Goblin' | 'Kobold' | 'Gnoll':

                char_family_fate = roll(family_fate_savage)
                print(char_family_fate)
                return char_family_fate

def roll_parents():

    char_parents_status = roll(parents_status)
    char_parents_status_id = char_parents_status[1]

    if char_parents_status_id == 0:
        return char_parents_status
    else:
        char_parents_fate = roll(parents_fate)
        print(char_parents_fate)
        char_parents_fate_id = char_parents_fate[1]
        if char_parents_fate_id == 0:
            char_father_fate = roll(father_fate)
            print(char_father_fate)
            return char_father_fate
        else:
            char_mother_fate = roll(mother_fate)
            print(char_mother_fate)
            return char_mother_fate

# def roll_family_events():
    

def roll_life_events(race_result, char_age):



    event_category = roll(life_event)
    event_category_id = event_category[1]
    print(f'You rolled: {event_category} with ID {event_category_id}')
    if event_category_id == 0: # Fortune or Misfortune
        print('Fortune or Misfortune...')

        print(f'1d10 x 100 gold = {gold}')

    elif event_category_id == 1: # Allies and Enemies
        print('Allies and Enemies')
    else: #Romance
        print('Romance')




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
        
    # question 1: Race
    retry = True
    while retry :
        question_text = 'Your character is a...'
        race_result_tuple = roll_race()
        race_result = race_result_tuple[0]
        retry = ask_reroll(question_text, race_result) 
    category = 'race'
    store_data(category, race_result)

    # question 2: Homeland
    retry = True
    while retry :
        question_text = 'Your character is from...'
        char_home_tuple = roll_homeland(race_result)
        char_home = char_home_tuple[0]
        retry = ask_reroll(question_text, char_home) 
    category = 'home'
    Character.origin = char_home
    store_data(category, char_home) 



    #  question 3: Origin
    retry = True
    while retry :
        question_text = 'Your childhood: '
        char_origin_tuple = roll_origin(race_result, char_home)
        char_origin = char_origin_tuple[0]
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




    # question 4: Family status
    retry = True
    while retry :
        question_text = 'Your family...'
        char_family_tuple = roll_family_fate(race_result)
        char_family = char_family_tuple[0]
        retry = ask_reroll(question_text, char_family) 
    category = 'family'
    store_data(category, char_family) 

    # question 5: Parents status
    retry = True
    while retry :
        question_text = 'Your parents...'
        char_parents_tuple = roll_parents()
        char_parents = char_parents_tuple[0]
        retry = ask_reroll(question_text, char_parents) 
    category = 'parents'
    store_data(category, char_parents) 

    # question 6: Life Path
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


    # question 7

    retry = True
    while retry :
        question_text = 'Major Life Events'
        char_life_events = roll_life_events(race_result, char_age)
        retry = ask_reroll(question_text, char_life_events) 
    category = 'life events'
    store_data(category, char_life_events) 





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
