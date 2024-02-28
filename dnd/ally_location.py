from class_enums import WeightedEnum

class AllyLocation(WeightedEnum):
    TOWN = ('a nearby town',30)
    CAPITOL = ('the country\'s grand capitol',30)
    VILLAGE = ('a peaceful village',20)
    HUT = ('a small hut in the middle of nowhere',10)
