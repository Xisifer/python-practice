
from char_properties import *

def check_saved_data():
    print('Total saved character data so far: ')

    if __name__ == '__main__':
        temp = vars(Character)
        for item in temp:
            if not item.startswith('__'):
                if not item.startswith('category'):
                    print(item , ' : ' , temp[item])


def store_data(category, selection):
    # print(f'Saving {selection} into character {category}...')
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
