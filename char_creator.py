from char_creation_menus import *
from char_creation_rollers import *
from general_functions import *





    
# question 1: Race
print(f'Question 1: \n')
race_result = char_question('Choose race:', roll_race, 'race', '')

# question 2: Homeland
print(f'Question 2: \n')
char_home = char_question('Your homeland:', roll_homeland, 'home', race_result)

# question 3: Origin
print(f'Question 3: \n')
# packing up Q1 & Q2 into a tuple
char_data = (race_result, char_home)
char_question('Your early background: \n', roll_origin, 'origin', char_data)

# question 4: Family status
print(f'Question 4: \n')
char_question('Your character\'s family:', roll_family_fate, 'family', race_result)

# question 5: Parents status
char_question('Your character\'s family:', roll_parents, 'parents', race_result)

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
for age in range(5, char_age, 5):
    life_milestones.append(age)

life_events_num = len(life_milestones)

print(f'You are {char_age} years old. This means you had {life_events_num} big Life Path events.')
print(f'You have had major life events at ages {life_milestones}')
category = 'age'
store_data(category, char_age)


# question 7

# char_question('Your character\'s family:', roll_parents, 'parents', race_result)

# Packing up into an expected tuple
life_event_data = (race_result, char_age, life_milestones)



for i in life_milestones:

    # event_roll = roll_life_events(race_result)

    print(f'Calling char_question and inserting roll_life_events function...')
    char_event_roll = char_question(f'At age {i}, something happened to you: ', roll_life_events, f'{i} year milestone', race_result)
    print(f'Outputted result of char_event_roll is: {char_event_roll}')
    char_event_roll_index = char_event_roll[1]

    print(f'char_event_roll_index is: {char_event_roll_index}')
    if char_event_roll_index == 0: 
        good_bad = roll_fortune()
        # char_question(f'Fortune or Misfortune?', roll_fortune, '', '')
        print(f'You chose: {good_bad}')



    elif char_event_roll_index == 1:
        char_question(f'You met someone! Were they an Ally or an Enemy?', roll_npc, 'npc', '')
        # print(f'They were: {npc_ally_enemy}')
        
    else:
        print(f'You rolled: {char_event_roll} at index {char_event_roll_index}')



category = 'life events'
store_data(category, 'life events') 




