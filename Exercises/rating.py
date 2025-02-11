from enum import Enum

class Rating(Enum):
    G = 0
    PG13 = 13
    R = 17

    def __str__(self):
        return self.name
