
from enum import Enum
import random

class WeightedEnum(Enum):
    def __init__(self, str, weight=1):
        self.str = str
        self.weight = weight

    def __str__(self):
        return self.str

    @classmethod
    def random(cls):
        all = list(cls)
        weights = [x.weight for x in all]
        return random.choices(all, weights)[0]











