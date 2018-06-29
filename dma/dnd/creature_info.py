""" Contains full information on creatures
"""
from decimal import Decimal, getcontext
from enum import IntEnum

class Intelligence(IntEnum):
    NON = 0
    ANIMAL = 1
    SEMI = 2
    LOW = 3
    AVERAGE = 4
    VERY = 5
    HIGH = 6
    EXCEPTIONAL = 7
    GENIUS = 8
    SUPRA = 9
    GODLIKE = 10
    VARIABLE = 11
    LENGTH = 12
    
class SourceBook(IntEnum):
    UNKNOWN = 0
    MONSTER_MANUAL = 1
    FIEND_FOLIO = 2
    MONSTER_MANUAL_2 = 3
    
class CreatureInfo():
    def __init__(
        self, name, iq,
        ac, attacks,
        align, size,
        description="",
        hd=(0,0), hp=(0,0),
        speed=0, fly=0, swim=0, web=0, burrow=0, climb=0,
        m_resist=0,
        num = (1,1), lair=0.0, treasure='',
        base_xp = 0, lvl=None, xp_hp = 0,
        parent_creature=None,
        sub_creatures=[],
        aliases = [],
        source = SourceBook.UNKNOWN
     ):
        
        getcontext().prec = 4
        
        self.name = name
        self.hit_dice = hd
        self.hit_point_mod = hp
        self.num_appearing = num
        self.lair_chance = Decimal(lair).normalize()
        self.base_xp = base_xp
        self.xp_per_hp = xp_hp
        self.level = lvl

        self.parent_creature = parent_creature
        self.sub_creatures = sub_creatures
        self.treasure = treasure
        self.source = source
        self.iq = iq
        self.speed = speed
        self.fly_speed = fly
        self.swim_speed = swim
        self.web_speed = web
        self.burrow_speed = burrow
        self.climb_speed = climb
        self.ac = ac
        self.attacks = attacks
        self.magic_resist = Decimal(m_resist).normalize()
        self.alignment = align
        self.size_class = size
        self.description = description
        self.alternate_names = aliases
        
    def __str__(self):
        return self.name
