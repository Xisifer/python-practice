import random
class Character:

    def __init__(
            self, 
            charGender, 
            charRace, 
            charHome, 
            charOrigin, 
            charAge,
            charFamily
        ): 
        self.gender = charGender
        self.race = charRace
        self.home = charHome
        self.origin = charOrigin
        self.age = charAge
        self.family = charFamily

# leon = Character("Male", "Human", 'Spain')

# print("This character is a",Character.gender, Character.race)
# print(f'Leon is: {leon.gender}.')
# print(f'Leon is a: {leon.race}.')




# d = {
#  'a': [1, 3, 2],
#  'b': [6],
#  'c': [0, 0]
# }

# roll = random.choice([k for k in d for x in d[k]])

# print(roll)

# dict = {'deer':50,
#         'raccoon':40,
#         'UNICORN':10}

# diceroll = random.choices(list(dict.keys()), weights=dict.values(), k=1)

# print(diceroll)