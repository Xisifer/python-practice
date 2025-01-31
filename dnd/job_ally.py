from class_enums import WeightedEnum


class AllyJob(WeightedEnum):
    BH = ('Bounty Hunter',10)
    MAGE = ('Mage',10)
    TEACHER = ('Mentor or Teacher',10)
    FRIEND = ('Childhood Friend',10)
    MERCHANT = ('Craftsman or Merchant',10)
    ENEMY = ('Former Enemy',10)
    NOBLE = ('Noble',10)
    PEASANT = ('Peasant',10)
    SOLDIER = ('Soldier',10)
    BARD = ('Bard',10)