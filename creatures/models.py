from random import randint, random
import json

from django.db import models
from django.templatetags.static import static

from dma.dnd.roll import roll
from dma.dnd.creature_info import Intelligence, SourceBook
from dma.dnd.treasure import Treasure

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
    alt_names = models.CharField(max_length=500)
    #int representing SourceBook IntEnum
    source = models.SmallIntegerField()
    
    description = models.CharField(max_length=4000, default = '')
    
    parent_creature = models.CharField(max_length=100)
    #json list of creature names
    sub_creatures = models.CharField(max_length=500)
    is_abstract = models.BooleanField(default=False)
    
    min_appearing = models.PositiveSmallIntegerField()
    max_appearing = models.PositiveSmallIntegerField()
    lair_chance = models.DecimalField(max_digits=6, decimal_places=4, default = 0.0)
    treasure_types = models.CharField(max_length=100)
    
    ac = models.SmallIntegerField()
    
    #Most movement is given as integers, but some are fractional
    ground_speed = models.DecimalField(max_digits=5, decimal_places=2)
    air_speed = models.DecimalField(max_digits=5, decimal_places=2)
    flight_class = models.CharField(max_length=1)
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
    attacks = models.CharField(max_length=300)
    magic_resist = models.DecimalField(max_digits=5, decimal_places=2)
    
    psi_attack_min = models.PositiveSmallIntegerField(default=0)
    psi_attack_max = models.PositiveSmallIntegerField(default=0)
    psi_defense_min = models.PositiveSmallIntegerField(default=0)
    psi_defense_max = models.PositiveSmallIntegerField(default=0)
    psi_modes = models.CharField(max_length=10)
    
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
    
    def roll_in_lair(self):
        return (random() > self.lair_chance)
        
    def roll_treasure(self):
        t = Treasure()
        t.rollLoot(self.treasure_types)
        
        return str(t)
         
    @property
    def lair_percentage(self):
        return self.lair_chance * 100
        
    def aliases(self):
        if self.alt_names:
            return json.loads(self.alt_names)
        
        return None
    
    def sub_creature_list(self):
        if self.sub_creatures:
            return json.loads(self.sub_creatures)
        else:
            return None
    
    @property
    def num_attacks(self):
        if not self.attacks:
            return 0
        else:
            return len(json.loads(self.attacks))
    
    @property
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
   
    @property
    def intelligence_str(self):
        return Intelligence(self.iq_class).name
    
    @property
    def alignment_str(self):
        return align_expand[self.alignment]
        
    def img_path(self):
        return static('creatures/images/ + self.slug' + '.png')


    def stats_html(self):
        if not self.is_abstract:
            table_creatures = [self]
        else:
            table_creatures = []
            
        if self.sub_creature_list():
            for c_name in self.sub_creature_list():
                creature = CreatureInfo.objects.get(name = c_name)
                table_creatures.append(creature)

        #Create top row with creature name(s)
        html = '<table><tr><th></th>'
        for c in table_creatures:
            html += '<th>{}</th>'.format(c.name)
        html += '</tr>'
        
        #Num Appearing Row
        html += '<tr><th>Number Appearing</th>'
        for c in table_creatures:
            if c.min_appearing != c.max_appearing:
                html += '<td>{} - {}</td>'.format(c.min_appearing, c.max_appearing)
            else:
                html += '<td>{}</td>'.format(c.max_appearing) 
        html += '</tr>'
        
        #AC Row
        html += table_row('Armor Class', 'ac', table_creatures)
            
        #Move Speeds
        html += table_row('Move Speed', 'ground_speed', table_creatures,
            data_suffix = '"', make_int = True)

        html += table_row_if_present('Air Speed', 'air_speed',
            table_creatures, data_suffix = '"', make_int = True)
            
        html += table_row_if_present('Flight Class', 'flight_class',
            table_creatures)
       
        html += table_row_if_present('Water Speed', 'water_speed',
            table_creatures, data_suffix = '"', make_int = True)
            
        html += table_row_if_present('Climb Speed', 'climb_speed',
            table_creatures, data_suffix = '"', make_int = True)
            
        html += table_row_if_present('Burrow Speed', 'burrow_speed',
            table_creatures, data_suffix = '"', make_int = True)
            
        html += table_row_if_present('Web Speed', 'web_speed',
            table_creatures, data_suffix = '"', make_int = True)

        #HD/HP
        html +=  '<tr><th>Hit Dice</th>'
        for c in table_creatures:
            html += '<td>'
            if c.max_hd > 0:
                if c.min_hd != c.min_hd:
                    html += '{} - {} HD'.format(c.min_hd, c.max_hd)
                else:
                    html += '{} HD'.format(c.min_hd)
                
                if c.max_hp_mod > 0:
                    html += ' + '
                    
            if c.max_hp_mod > 0:
                if c.min_hp_mod != c.max_hp_mod:
                    html += '{} - {} HP'.format(c.min_hp_mod, c.max_hp_mod)
                else:
                    html += '{} HP'.format(c.min_hp_mod)
            html += '</td>'
        
        html += '<tr><th>% In Lair</th>'
        for c in table_creatures:
            if c.lair_chance >= 0.01 or c.lair_chance == 0.00:
                html += '<td>{:.0%}</td>'.format(c.lair_chance)
            else:
                html += '<td>{:.2%}</td>'.format(c.lair_chance)
        html += '</tr>'
        
        html += table_row('Treasure Type', 'treasure_types',
            table_creatures, show_none = True)
            
        html += table_row('Number of Attacks', 'num_attacks',
            table_creatures)
        
        html += table_row('Attack Damage', 'attacks_str',
            table_creatures)
            
        html += '<tr><th>Magic Resistance</th>'
        for c in table_creatures:
            html += '<td>{:%}</td>'.format(c.magic_resist)
        html += '</tr>'
        
        html += table_row('Intelligence', 'intelligence_str',
            table_creatures)
            
        html += table_row('Alignment', 'alignment_str',
            table_creatures)
            
        html += table_row('Size', 'size_class', table_creatures)
        
        html += table_row('Level', 'level', table_creatures)
        
        #XP
        html += '<tr><th>XP</th>'
        for c in table_creatures:
            html += '<td>{:,}'.format(c.base_xp)
            if c.xp_per_hp:
                html += ' + {}/HP'.format(c.xp_per_hp)
            html += '</td>'
        html += '</tr>'

        #Psionic Ability Points
        html += '<tr><th>Psionic Ability</th>'
        for c in table_creatures:
            if (not c.psi_attack_min) and (not c.psi_defense_min):
            #no psionics
                html += '<td>Nil</td>'
            else:
                psi_min = c.psi_attack_min + c.psi_defense_min
                psi_max = c.psi_attack_max + c.psi_defense_max
                html += '<td>{}'.format(psi_min)
                if (psi_min != psi_max):
                    html += '-{}'.format(psi_max)
                
                if not c.psi_defense_min:
                #only attack points
                    html += ' attack'
                if not c.psi_attack_min:
                #only defense points
                    html += ' defense'
                    
                html += '</td>'
        html += '</tr>'
        
        #Psionic Modes
        html += '<tr><th>Psionic Attack/Defense Modes</th>'
        for c in table_creatures:
            if not c.psi_modes:
                html += '<td>Nil</td>'
            elif c.psi_modes == '?':
                html += '<td>Varying</td>'
            else:
                html += '<td>'
                
                att_modes = ''.join(c for c in c.psi_modes if c in 'abcde')
                if not att_modes:
                    html += 'Nil'
                elif att_modes == 'abcde':
                    html += 'All'
                else:
                    html += att_modes.upper()
                    
                html += '/'
                
                def_modes = ''.join(c for c in c.psi_modes if c in 'fghij')
                if not def_modes:
                    html += 'Nil'
                elif def_modes == 'fghij':
                    html += 'All'
                else:
                    html += def_modes.upper()
                    
                html += '</td>'
        html += '</tr>'
                
        html += '</table>'
                
        return html
 
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

def table_row(title, field, creatures, data_suffix='',
    make_int = False, show_none=False):
    ret = '<tr><th>{}</th>'.format(title)
    for c in creatures:
        data = getattr(c,field)
        if make_int:
            data = int(data)
        
        if not show_none or data:                
            ret += '<td>{}{}</td>'.format(data, data_suffix)
        else: #Show None active, data is null
            ret += '<td>None</td>'
    ret += '</tr>'
    
    return ret

def table_row_if_present(title, field, creatures, data_suffix='', make_int = False):
    if any( getattr(x, field) for x in creatures):
        return table_row(title, field, creatures, data_suffix, make_int)  
    return ''
