"""
Creature class represents an individual creature
"""
from random import randint

from .roll import roll

class Creature():
    def __init__(self, c_type, hp, xp, name=None):
        self.creature_name = c_type
        self.hp = hp
        self.xp = xp
        self.name = name

def roll_standard_encounter(c_type):
    creatures = []
    n = randint(c_type.num_appearing[0], c_type.num_appearing[1])

    for c in n:
        hd = randint(c_type.hit_dice[0], c_type.hit_dice[1])
        hp = roll(8, hd) + randint(c_type.hit_point_mod[0], hit_point_mod[1])
        xp = c_type.base_xp + (hp * c_type.xp_per_hp)

        creatures.append(Creature(c_type.name, hp, xp))

    return creatures
