from random import randint
import json

from django.db import models

from dma.dnd.roll import roll
from dma.dnd.creature_info import Intelligence, SourceBook

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
    #json representation of a list of strings
    alt_names = models.CharField(max_length=500, null=True)
    #int representing SourceBook IntEnum
    source = models.SmallIntegerField()
    
    parent_creature = models.CharField(max_length=100, null=True)
    #json list of creature names
    sub_creatures = models.CharField(max_length=500, null=True)
    
    min_appearing = models.PositiveSmallIntegerField()
    max_appearing = models.PositiveSmallIntegerField()
    lair_chance = models.DecimalField(max_digits=6, decimal_places=4, default = 0.0)
    treasure_types = models.CharField(max_length=100, null=True)
    
    ac = models.SmallIntegerField()
    
    #Most movement is given as integers, but some are fractional
    ground_speed = models.DecimalField(max_digits=5, decimal_places=2)
    air_speed = models.DecimalField(max_digits=5, decimal_places=2)
    water_speed = models.DecimalField(max_digits=5, decimal_places=2)
    burrow_speed = models.DecimalField(max_digits=5, decimal_places=2)
    climb_speed = models.DecimalField(max_digits=5, decimal_places=2)
    web_speed = models.DecimalField(max_digits=5, decimal_places=2)
    
    min_hd = models.PositiveSmallIntegerField()
    max_hd = models.PositiveSmallIntegerField()
    min_hp_mod = models.SmallIntegerField()
    max_hp_mod = models.SmallIntegerField()
    
    #a json representation of a list of attacks
    #each attack is a length 3 list: ([die_type],[num_rolled],[damage_added])
    attacks = models.CharField(max_length=300, null=True)
    magic_resist = models.DecimalField(max_digits=4, decimal_places=2)
    
    #Int representing Intelligence IntEnum
    iq_class = models.SmallIntegerField()
    #One of 'LG','NG','CG','LN','NN','CN','LE','NE','CE'
    alignment = models.CharField(max_length=2)
    #One of 'S','M','L'
    size_class = models.CharField(max_length=1)
    
    level = models.IntegerField(null=True)
    base_xp = models.IntegerField(default=0)
    xp_per_hp = models.IntegerField(default=0)

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
        
            
    def lair_percentage(self):
        return self.lair_chance * 100
        
    def aliases(self):
        if self.alt_names:
            return json.loads(self.alt_names)
        
        return None
    
    def num_attacks(self):
        if not self.attacks:
            return 0
        else:
            return len(json.loads(self.attacks))
    
    def attacks_str(self):
        if not self.attacks:
            return 'None'
            
        att_list = json.loads(self.attacks)

        attack_str = ''
        
        for att in att_list:
            min = att[1] + att[2]
            max = att[0] * att[1] + att[2]
            
            if min == max:
                attack_str += '{}/'.format(min)
            else:
                attack_str += '{}-{}/'.format(min,max)
        
        return attack_str[:-1]
    
    def m_resist_percentage(self):
        return self.magic_resist * 100
        
    def intelligence_str(self):
        return Intelligence(self.iq_class).name
        
    def alignment_str(self):
        return align_expand[self.alignment]
    
align_expand = {
    'LG': 'Lawful Good', 
    'NG': 'Neutral Good',
    'CG': 'Chaotic Good',
    'LN': 'Lawful Neutral',
    'NN': 'True Neutral',
    'CN': 'Chaotic Neutral',
    'LE': 'Lawful Evil',
    'NE': 'Neutral Evil',
    'CE': 'Chaotic Evil'
}
        
        
            
