from random import randint

from django.db import models

from dma.dnd.roll import roll

"""
Creature class represents an individual creature
"""        
class Creature(models.Model):
    def __init__(self, type_name, hp, xp, combat_hd, name=None):
        self.creature_name = type_name
        self.hp = hp
        self.xp = xp
        self.combat_hd = combat_hd
        self.name = name
        
    def __eq__(self, other):
        return self.xp == other.xp

    def __gt__(self, other):
        return self.xp > other.xp

"""
CreatureInfo represents attributes for a type of creature
"""
class CreatureInfo(models.Model):
    slug = models.SlugField(max_length=75)
    name = models.CharField(max_length=75, unique=True)
    min_hd = models.PositiveSmallIntegerField()
    max_hd = models.PositiveSmallIntegerField()
    min_hp_mod = models.SmallIntegerField()
    max_hp_mod = models.SmallIntegerField()
    min_appearing = models.PositiveSmallIntegerField()
    max_appearing = models.PositiveSmallIntegerField()
    lair_chance = models.DecimalField(max_digits=6, decimal_places=4, default = 0.0)
    base_xp = models.IntegerField(default=0)
    xp_per_hp = models.IntegerField(default=0)
    level = models.IntegerField(null=True)
    
    def __str__(self):
        return self.name
    
    def __eq__(self, other):
        my_vars = vars(self)
        their_vars = vars(other)
        
        my_fields = {key: val for key, val in my_vars.items() if key not in ['_state', 'id']}
        their_fields = {key: val for key, val in their_vars.items() if key not in ['_state', 'id']}
        
        return my_fields == their_fields

    def roll_standard_encounter(self):
        creatures = []
        n = randint(self.min_appearing, self.max_appearing)
        
        return self.roll_quantity(n)

        
    def roll_quantity(self, n):
        creatures = []
        
        for i in range(n):
            hd = randint(self.min_hd, self.max_hd)
            hp_mod = randint(self.min_hp_mod, self.max_hp_mod)
            hp = roll(8, hd) + hp_mod
            xp = self.base_xp + (hp * self.xp_per_hp)
            
            #adjust effective hd for combat if creature has over +3 extra
            #each full +8 hp mod is counted as another hit die
            if (hp_mod > 3):
                combat_hd = hd + ((hp_mod -3) // 8) + 1
            else:
                combat_hd = hd
            
            creatures.append(Creature(self.name, hp, xp, combat_hd))
        
        return creatures
