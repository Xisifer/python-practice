from dnd.class_enums import WeightedEnum

class PlayerJob(WeightedEnum):
    BARBARIAN = ('Barbarian', 10)
    BARD = ('Bard', 10)
    CRAFTER = ('Artisan / Crafter', 10)
    CRIMINAL = ('Criminal / Rogue', 10)
    DOCTOR = ('Doctor / Healer', 10)
    DRUID = ('Druid', 10)
    MAGE = ('Mage / Wizard', 10)
    FIGHTER = ('Fighter / Warrior', 10)
    MERCHANT = ('Merchant', 10)
    NOBLE = ('Noble', 10)
    PRIEST = ('Priest / Cleric', 10)
    RANGER = ('Ranger', 10)

class NPCJob(WeightedEnum):
    PEASANT = ('Peasant', 10)
    MERCHANT = ('Merchant', 10)
    FARMER = ('Farmer', 10)
    FISHER = ('Fisher', 10)
    NOBLE = ('Noble', 10)
    HUNTER = ('Hunter', 10)
    SERVANT = ('Servant', 10)
    MINER = ('Miner', 10)
    CRAFTER = ('Craftsman',10)



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