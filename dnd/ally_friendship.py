from class_enums import WeightedEnum

class AllyRelation(WeightedEnum):
    ACQUAINTANCE = ('Acquaintances',40)
    FRIEND = ('Friends',20)
    CLOSE_FRIEND = ('Close Friends',20)
    INSEPERABLE = ('Inseperable',10)
    SWORN = ('Sworn companions/partners',10)
