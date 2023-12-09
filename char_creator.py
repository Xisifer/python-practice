from char_creation_menus import *
from char_creation_rollers import *
from general_functions import *
from char_save_data import *
from char_properties import *



    
# question 1: Race
print(f'Question 1: \n')
race_result = char_question('Choose race:', roll, races)
question_result = race_result
category = 'race'
print(f'QUESTION 1 RESULT: {question_result}')
result_text = question_result[0]
print(f'result_text = {result_text}')
result_tuple = question_result[1]
print(f'result_tuple = {result_tuple}')
store_data(category, result_text)

race_result = race_result[0] # Changing the association of race_result so all the other functions relying on race_result's text doesn't break


# question 2: Homeland
print(f'Question 2: \n')
char_home = char_question('Your homeland:', roll_homeland, race_result)
question_result = char_home
category = 'home'
print(f'QUESTION 2 RESULT: {question_result}')
result_text = question_result[0]
print(f'result_text = {result_text}')
result_tuple = question_result[1]
print(f'result_tuple = {result_tuple}')
store_data(category, result_text)


# question 3: Origin
print(f'Question 3: \n')
# packing up Q1 & Q2 into a tuple
char_data = (race_result, char_home)
char_background = char_question('Your early background: \n', roll_origin, char_data)
question_result = char_background
category = 'origin'
print(f'QUESTION 3 RESULT: {question_result}')
result_text = question_result[0]
print(f'result_text = {result_text}')
result_tuple = question_result[1]
print(f'result_tuple = {result_tuple}')
store_data(category, result_text)



# question 4: Family status
print(f'Question 4: \n')
char_family = char_question('Your character\'s family:', roll_family_fate, race_result)
question_result = char_family
category = 'family'
print(f'QUESTION 4 RESULT: {question_result}')
result_text = question_result[0]
print(f'result_text = {result_text}')
result_tuple = question_result[1]
print(f'result_tuple = {result_tuple}')
store_data(category, question_result)

# question 5: Parents status
char_parents = char_question('Your character\'s parents:', roll_parents, race_result)
question_result = char_parents
category = 'parents'
print(f'QUESTION 5 RESULT: {question_result}')
result_text = question_result[0]
print(f'result_text = {result_text}')
result_tuple = question_result[1]
print(f'result_tuple = {result_tuple}')
store_data(category, question_result)

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
    char_event_roll = char_question(f'At age {i}, something happened to you: ', roll_life_events, race_result)
    print(f'Outputted result of char_event_roll is: {char_event_roll}')

    question_result = char_event_roll
    category = f'{i} year milestone'
    store_data(category, question_result)

    char_event_roll_index = char_event_roll[1]

    print(f'char_event_roll_index is: {char_event_roll_index}')
    if char_event_roll_index == 0: 
        # good_bad = roll_fortune()
        # char_question(f'Fortune or Misfortune?', roll_fortune, '', '')
        # print(f'You chose: {good_bad}')



        good_bad = char_question(f'Was it a Fortunate event? Or a Misfortune?\n', roll_fortune, race_result)
        print(f'Result: good_bad = {good_bad}')

        if good_bad[1] == 0: # Fortunate Event
            fortune_event = char_question(f'You rolled: ', roll, fortunes)
            print(f'fortune_event rolled: {fortune_event}')
        else: # Misfortune
            misfortune_event = char_question(f'You rolled: ', roll, misfortunes)
            print(f'misfortune_event rolled: {misfortune_event}')




    elif char_event_roll_index == 1:
        npc_ally_enemy = char_question(f'You met someone! Were they an Ally or an Enemy?', roll, allegiance)
        # print(f'They were: {npc_ally_enemy}')

        if npc_ally_enemy[1] == 0: # Ally
            ally_gender = roll(gender)
            complete_ally = roll_ally(ally_gender)
            # print(f'complete_ally is: {complete_ally}')
            # ally_summary = f'You met a {ally_gender[0]} {complete_ally[1]} {complete_ally[2]}, and {complete_ally[3]}. \nYou became {complete_ally[4]} for many years. \nEventually you parted ways in {complete_ally[5]}. \nToday, {complete_ally[6]}.'
            # complete_ally = [
            #     al_gender,
            #     al_position,
            #     al_meeting,
            #     al_relationship,
            #     al_location,
            #     al_fate
            # ]
            # print(ally_summary)

            npc_ally = char_question(f'They were an: {npc_ally_enemy}', roll_ally, ally_gender)
            print(f'npc_ally is: {npc_ally}')






        
    else:
        print(f'You rolled: {char_event_roll} at index {char_event_roll_index}')



category = 'life events'
store_data(category, 'life events') 




