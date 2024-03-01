from dnd.class_enums import WeightedEnum

class ParentsStatus(WeightedEnum):
    ALIVE = ('Your parents are alive.',30)
    INCIDENT = ('Something happened to your parents.',70)