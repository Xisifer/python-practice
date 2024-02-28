import inquirer
import random
# from char_properties import Character

# from char_save_data import *


    



# def char_question(q_text=None, roll_choice=None, insert_data=None): 

#     retry = True
#     while retry :
#         question_text = q_text
#         question_result_tuple = roll_choice(insert_data)
#         print(f'question_result_tuple is: {question_result_tuple}')
#         question_result = question_result_tuple[0]
#         print(f'question_result_tuple[0] is: {question_result_tuple[0]}')
#         retry = ask_reroll(question_text, question_result)
#         print(f'Returning full tuple of roll result: {question_result_tuple}')
    
#     return question_result_tuple




def flip():
    if random.randint(0,1):
        return 0
    else:
        return 1



def name_input():
    char_name = input("Do you want to roll dice? Y/N ")
    name_stripped = str(char_name.strip())
    print(f'You said: {name_stripped}')

# def bare_text(string):
#     print(f'bare string is {string}')
#     strip1 = string.strip('[]') # remove [dictionary brackets]
#     strip2 = strip1.strip('\"') # remove "double quotes"
#     stripped_text = strip2.strip("\'") # remove 'single quotes'
#     return stripped_text



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



# ==============================================
# Other general useful code I don't want to get rid of yet until I'm sure I don't need it

# ===============
# TUPLE CHECKER
# ===============
# is_tuple = type(insert_data) is tuple

# if is_tuple:
#     print(f'The tuple is {len(insert_data)} items long.')
#     i=0
#     while i < len(insert_data):
#         print(insert_data[i])
#         i=i+1
#     print(f'first data of tuple {insert_data} is {insert_data[0]}.')
#     insert_data = insert_data[0]
# else:
#     insert_data = insert_data









# 
# ===============
# TUPLE CHECKER
# ===============

    # print(f'Is {insert_data} a tuple?')
    # if type(insert_data) is tuple:
    #     print('Yes!')
    #     print(f'The tuple is {len(insert_data)} items long.')
    #     # i=0
    #     # while i < len(insert_data):
    #     #     print(insert_data[i])
    #     #     i=i+1
    #     print(f'first data of tuple {insert_data} is {insert_data[0]}.')
    #     print(f'second data of tuple {insert_data} is {insert_data[1]}.')
    #     insert_data = insert_data[0]
    #     print(f'insert_data is now: {insert_data}')
    # else:
    #     print('No.')
    #     insert_data = insert_data

    # print(f'Is {roll_choice} a tuple?')

    # if type(roll_choice) is tuple:
    #     print('Yes!')
    #     print(f'The tuple is {len(roll_choice)} items long.')
    #     i=0
    #     while i < len(roll_choice):
    #         print(roll_choice[i])
    #         i=i+1
    #     print(f'first data of tuple {roll_choice} is {roll_choice[0]}.')
    #     roll_choice = roll_choice[0]
    # else:
    #     print('No.')
    #     roll_choice = roll_choice