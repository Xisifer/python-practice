from dnd.class_enums import WeightedEnum

class FeyOrigins(WeightedEnum):
    FOREST = ('You are from Sherwood Forest, and were raised under the cruel thumb of the King\'s tax collectors.',50)
    LOTHLORIEN = ('You are from Lothlorien, the final bastion of your dying people.',50)

class FeyFlavor(WeightedEnum):
    HARMONY = ('You lived in harmony with nature. The animals were your childhood friends.', 70)
    ALONE = ('Growing up in the wild taught you to be tough and self-sufficient.', 30)

class FeyHomes(WeightedEnum):
    FOREST = ('Forest',55)
    MOUNTAIN = ('Mountains',15)
    OCEAN = ('Ocean', 20)
    JUNGLE = ('Jungle',10)