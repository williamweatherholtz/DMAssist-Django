""" Contains minimal information on creatures to determine their
    starting HP and their XP values
"""
from decimal import Decimal, getcontext

class BasicCreatureInfo():
    def __init__(self, name, hd, hp, num = (1,1), lair=0.0,
                 base_xp = 0, lvl=None):
        
        getcontext().prec = 4
        
        self.name = name
        self.hit_dice = hd
        self.hit_point_mod = hp
        self.num_appearing = num
        self.lair_chance = Decimal(lair).normalize()
        self.base_xp = base_xp
        self.level = lvl

