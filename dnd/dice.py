


# Ask if player wants to roll dice
# if yes, roll dice
# if no, exit

# print(input("Do you want to roll dice? Y/N: "))


# def parse_input(input_string):


import random

player_answer = input("Do you want to roll dice? Y/N ")
answer_stripped = str(player_answer.strip())
print(f'You said: {answer_stripped}')

if answer_stripped == "Y" or answer_stripped == "y": 
    roll_results = []

    print("Rolling 1d10...")
    roll = random.randint(1,10)
    roll_results.append(roll)

    print(f'Result: {str(roll_results)}')

else:
    print("Dice roll cancelled.")




# def roll_dice(player_answer):
#     roll_result = []
#     for x in range (player_answer):
#         roll = random.randint(1,10)
#         roll_results.append(roll)
#     return roll_results


# def player_input(input_string):

#     else:
#         print("Dice roll cancelled.")