from class_enums import WeightedEnum

class AllyMeeting(WeightedEnum):
    SAVED_THEM = ('You saved {} from something',10)
    SAVED_YOU = ('{} saved you from something',10)
    TAVERN = ('you met them in a tavern',10)
    ALLIES = ('You fought together against something',10)
    TRAPPED = ('You were trapped together somehow',10)
    TRAVELING = ('You met while traveling',10)
    HIRED_THEM = ('You hired them to do something',10)
    HIRED_YOU = ('They hired you to do something',10)
    ENEMIES = ('You fought against each other and came to mutual respect through combat',10)
    RELUCTANT_ALLY = ('You were forced to work together',10)
