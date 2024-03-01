from dnd.class_enums import WeightedEnum

class HumanOrigins(WeightedEnum):
    CITY = ('one of the massive cities throughout the realm, such as a national capitol or a large coastal trading port.', 50)
    COUNTRY = ('the idyllic countryside. You may have worked on a family farm, helped a family trade, or stalked game in the forest.', 50)
    

class HumanFlavor(WeightedEnum):
    POOR = ('The city was cramped, dirty, poor and vicious.', 70)
    RICH = ('The city was rich and opulent. You lived like nobility.',30)

class HumanHomes(WeightedEnum):
    WATERDEEP = ("Waterdeep, the City of Splendors", 40)
    BALDUR = ("Baldur's Gate", 20)
    VARISIA = ("Varisia, the Lands of Adventure", 30)
    MWANGI = ("the Mwangi Expanse, the dense jungle heartland", 10)