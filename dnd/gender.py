from class_enums import WeightedEnum

class Gender(WeightedEnum):
    MALE = ("Male", 45)
    FEMALE = ("Female", 45)
    NB = ("Nonbinary", 10)