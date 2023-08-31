import inquirer
import random


# Define arrays of choices

def __init__(self, value):

    genders = [
        'Male',
        'Female'
    ]
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




def choice_roller(question_text, choice_table, menu_option):

    table_result = str(random.choice(choice_table))
    choice_menu = {
        inquirer.List('menu',
                    message=f'Result: {table_result}',
                    choices=['Accept', 'Reroll'], default=['Accept']

        )
    }
    # def get_choices(answers): return list(str())
    # get_choices(races)

    while menu_option == 'Reroll':
        table_result = str(random.choice(choice_table))
        choice_menu = {
            inquirer.List('menu',
                        message=f'Result: {table_result}',
                        choices=['Accept', 'Reroll'], default=['Accept']

            )
        }

        answer = inquirer.prompt(choice_menu)

        if answer['menu'] == 'Reroll':
            print("Rerolling...")
        else:
            print(f"table_result is: {table_result}")
            print("Moving on...")
            return table_result
            # break

# print(f"Character race: \n ")
choice_roller('What is your race?', races, 'Reroll')







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




# class Character:
#     name =  char_name
#     age = char_age






# print("Hello, " + Character.name)





# char_age = int(input("What is your age? "))

# # if (char_age >=20 and <=29):
# if 20 <= char_age <= 29:
#     print("You are in your 20s")





    # Show character text: "Your [homeland] is: [Texas]"
    # Prompt player to Accept or Reroll
    # If Accept: Store answer in part of the Character class
    # If Reroll: Reroll

    # What about nested tables? 
        # Show character text: "Your [homeland] is: [Texas]"
        # Prompt player to Accept or Reroll
        # If Accept: show second prompt
            # Second prompt: roll from list of options
            # Prompt player to Accept or Reroll

        # If Reroll: Reroll




