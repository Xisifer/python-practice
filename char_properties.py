
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

# # print("This character is a",Character.gender, Character.race)
# print(f'Leon is: {leon.gender}.')
# print(f'Leon is a: {leon.race}.')

