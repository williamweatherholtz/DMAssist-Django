from dnd.currency import Coin

class MeleeWeapon():
    def __init__(
        self,name, weight, damage, damage_lg,
        space,speed,value,ac_adjust,
        recieve_bonus=False,L_recieve_bonus=False,
        mount_charge_bonus=False):
        
        self.name = name
        self.value = value
        self.weight = weight
        self.die = damage[0]
        self.num = damage[1]
        self.mod = damage[2]
        self.die_lg = damage_lg[0]
        self.num_lg = damage_lg[1]
        self.mod_lg = damage_lg[2]
        self.space = space
        self.speed = speed
        self.ac_adjust = ac_adjustments
    
    def __str__(self):
        return self.name
melee_weapons = [
MeleeWeapon('Battle Axe',
    weight = 75,
    damage = (8,1,0),
    damage_lg = (8,1,0),
    space = 4,
    speed = 7,
    value = Coin(5,'g'),
    ac_adjust = [-3,-2,-1,-1,0,0,1,1,2]
),
MeleeWeapon('Hand Axe',
    weight = 50,
    damage = (6,1,0),
    damage_lg = (4,1,0),
    space = 1,
    speed = 4,
    value = Coin(1,'g'),
    ac_adjust = [-3,-2,-2,-1,0,0,1,1,1]
)
MeleeWeapon('Bardiche',
    weight = 125,
    damage = (4,2,0),
    damage_lg = (4,3,0),
    space = 5,
    speed = 9,
    value = Coin(7,'g'),
    ac_adjust = [-2,-1,0,0,1,1,2,2,3]
)
MeleeWeapon('Bec de Corbin',
    weight = 100,
    damage = (8,1,0),
    damage_lg = (6,1,0),
    space = 6,
    speed = 9,
    value = Coin(6,'g'),
    ac_adjust = [2,2,2,0,0,0,0,0,-1]
)
MeleeWeapon('Bill-Guisarme',
    weight = 150,
    damage = (4,2,0),
    damage_lg = (10,1,0),
    space = 2,
    speed = 10,
    value = Coin(6,'g'),
    ac_adjust = [0,0,0,0,0,0,1,0,0]
)
MeleeWeapon('Bo Stick',
    weight = 15,
    damage = (6,1,0),
    damage_lg = (3,1,0),
    space = 3,
    speed = 3,
    value = Coin(50,'s'),
    ac_adjust = [-9,-7,-5,-3,-1,0,1,0,3]
)
MeleeWeapon('Club',
    weight = 30,
    damage = (6,1,0),
    damage_lg = (3,1,0),
    space = 2,
    speed = 4,
    value = Coin(50,'s'),
    ac_adjust = [-5,-4,-3,-2,-1,-1,0,0,1]
)
MeleeWeapon('Dagger',
    weight = 10,
    damage = (4,1,0),
    damage_lg = (3,1,0),
    space = 1,
    speed = 2,
    value = Coin(2,'g'),
    ac_adjust = [-3,-3,-2,-2,0,0,1,1,3]
)
MeleeWeapon('Fauchard',
    weight = 60,
    damage = (6,1,0),
    damage_lg = (8,1,0),
    space = 2,
    speed = 8,
    value = Coin(3,'g'),
    ac_adjust = [-2,-2,-1,-1,0,0,0,-1,-1]
)
MeleeWeapon('Fauchard-Fork',
    weight = 80,
    damage = (8,1,0),
    damage_lg = (10,1,0),
    space = 2,
    speed = 8,
    value = Coin(8,'g'),
    ac_adjust = [-1,-1,-1,0,0,0,1,0,1]
)
MeleeWeapon('Footman\'s Flail',
    weight = 150,
    damage = (6,1,1),
    damage_lg = (4,2,0),
    space = 6,
    speed = 7,
    value = Coin(3,'g'),
    ac_adjust = [2,2,1,2,1,1,1,1,-1]
)
MeleeWeapon('Horseman\'s Flail',
    weight = 35,
    damage = (4,1,1),
    damage_lg = (4,1,1),
    space = 4,
    speed = 6,
    value = Coin(8,'g'),
    ac_adjust = [0,0,0,0,0,1,1,1,0]
)
MeleeWeapon('Military Fork',
    weight = 75,
    damage = (8,1,0),
    damage_lg = (4,2,0),
    space = 1,
    speed = 7,
    value = Coin(4,'g'),
    ac_adjust = [-2,-2,-1,0,0,1,1,0,1]
)
MeleeWeapon('Glaive',
    weight = 75,
    damage = (6,1,0),
    damage_lg = (10,1,0),
    space = 1,
    speed = 8,
    value = Coin(6,'g'),
    ac_adjust = [-1,-1,0,0,0,0,0,0,0]
)
MeleeWeapon('Glaive-Guisarme',
    weight = 100,
    damage = (4,2,0),
    damage_lg = (6,2,0),
    space = 1,
    speed = 9,
    value = Coin(10,'g'),
    ac_adjust = [-1,-1,0,0,0,0,0,0,0]
)
MeleeWeapon('Guisarme',
    weight = 80,
    damage = (4,2,0),
    damage_lg = (8,1,0),
    space = 2,
    speed = 8,
    value = Coin(5,'g'),
    ac_adjust = [-2,-2,-1,-1,0,0,0,-1,-1]
)
MeleeWeapon('Guisarme-Voulge',
    weight = 150,
    damage = (4,2,0),
    damage_lg = (4,2,0),
    space = 2,
    speed = 10,
    value = Coin(7,'g'),
    ac_adjust = [-1,-1,0,1,1,1,0,0,0]
)  
MeleeWeapon('Halberd',
    weight = 175,
    damage = (10,1,0),
    damage_lg = (6,2,0),
    space = 5,
    speed = 9,
    value = Coin(9,'g'),
    ac_adjust = [1,1,1,2,2,2,1,1,0]
)
MeleeWeapon('Lucerne Hammer',
    weight = 150,
    damage = (4,2,0),
    damage_lg = (6,1,0),
    space = 5,
    speed = 9,
    value = Coin(7,'g'),
    ac_adjust = [1,1,2,2,2,1,1,0,0]
)
MeleeWeapon('Hammer',
    weight = 50,
    damage = (4,1,1),
    damage_lg = (4,1,0),
    space = 2,
    speed = 4,
    value = Coin(1,'g'),
    ac_adjust = [0,1,0,1,0,0,0,0,0]
)
MeleeWeapon('Jo Stick',
    weight = 40,
    damage = (6,1,0),
    damage_lg = (4,1,0),
    space = 2,
    speed = 2,
    value = Coin(50,'s'),
    ac_adjust = [-8,-6,-4,-2,-1,0,1,0,2]
)
MeleeWeapon('Lance (Light Horse)',
    weight = 50,
    damage = (6,1,0),
    damage_lg = (8,1,0),
    space = 1,
    speed = 6,
    value = Coin(6,'g'),
    ac_adjust = [-2,-2,-1,0,0,0,0,0,0]
)
MeleeWeapon('Lance (Medium Horse)',
    weight = 100,
    damage = (6,1,1),
    damage_lg = (6,2,0),
    space = 1,
    speed = 7,
    value = Coin(6,'g'),
    ac_adjust = [0,1,1,1,1,0,0,0,0]
)
MeleeWeapon('Lance (Heavy Horse)',
    weight = 150,
    damage = (4,2,1),
    damage_lg = (6,3,0),
    space = 1,
    speed = 8,
    value = Coin(6,'g'),
    ac_adjust = [3,3,2,2,2,1,1,0,0]
)
MeleeWeapon('Footman\'s Mace',
    weight = 100,
    damage = (6,1,1),
    damage_lg = (6,1,0),
    space = 4,
    speed = 7,
    value = Coin(8,'g'),
    ac_adjust = [1,1,0,0,0,0,0,1,-1]
)
MeleeWeapon('Horseman\'s Mace',
    weight = 50,
    damage = (6,1,0),
    damage_lg = (4,1,0),
    space = 2,
    speed = 6,
    value = Coin(4,'g'),
    ac_adjust = [1,1,0,0,0,0,0,0,0]
)
MeleeWeapon('Morning Star',
    weight = 125,
    damage = (4,2,0),
    damage_lg = (6,1,1),
    space = 5,
    speed = 7,
    value = Coin(5,'g'),
    ac_adjust = [0,1,1,1,1,1,1,2,2]
)
MeleeWeapon('Partisan',
    weight = 80,
    damage = (6,1,0),
    damage_lg = (6,1,1),
    space = 3,
    speed = 9,
    value = Coin(10,'g'),
    ac_adjust = [0,0,0,0,0,0,0,0,0]
)
MeleeWeapon('Footman\'s Military Pick',
    weight = 60,
    damage = (6,1,1),
    damage_lg = (4,2,0),
    space = 4,
    speed = 7,
    value = Coin(8,'g'),
    ac_adjust = [2,2,1,1,0,-1,-1,-1,-2]
)
MeleeWeapon('Horseman\'s Military Pick',
    weight = 40,
    damage = (4,1,1),
    damage_lg = (4,1,0),
    space = 2,
    speed = 5,
    value = Coin(5,'g'),
    ac_adjust = [1,1,1,1,0,0,-1,-1,-1]
)
MeleeWeapon('Awl Pike',
    weight = 80,
    damage = (6,1,0),
    damage_lg = (12,1,0),
    space = 1,
    speed = 13,
    value = Coin(3,'g'),
    ac_adjust = [-1,0,0,0,0,0,0,-1,-2]
)
MeleeWeapon('Ranseur',
    weight = 50,
    damage = (4,2,0),
    damage_lg = (4,2,0),
    space = 1,
    speed = 8,
    value = Coin(4,'g'),
    ac_adjust = [-2,-1,-1,0,0,0,0,0,1]
)
MeleeWeapon('Scimitar',
    weight = 40,
    damage = (8,1,0),
    damage_lg = (8,1,0),
    space = 2,
    speed = 4,
    value = Coin(15,'g'),
    ac_adjust = [-3,-2,-2,-1,0,0,1,1,3]
)
MeleeWeapon('Spear',
    weight = 50,
    damage = (6,1,0),
    damage_lg = (8,1,0),
    space = 1,
    speed = 7,
    value = Coin(1,'g'),
    ac_adjust = [-2,-1,-1,-1,0,0,0,0,0]
)
MeleeWeapon('Spetum',
    weight = 50,
    damage = (6,1,1),
    damage_lg = (6,2,0),
    space = 1,
    speed = 8,
    value = Coin(3,'g'),
    ac_adjust = [-2,-1,0,0,0,0,0,1,2]
)
MeleeWeapon('Quarter Staff',
    weight = 50,
    damage = (6,1,0),
    damage_lg = (6,1,0),
    space = 3,
    speed = 4,
    value = Coin(50,'s'),
    ac_adjust = [-7,-5,-3,-1,0,0,1,1,1]
)
MeleeWeapon('Bastard Sword',
    weight = 100,
    damage = (4,2,0),
    damage_lg = (8,2,0),
    space = 4,
    speed = 6,
    value = Coin(25,'g'),
    ac_adjust = [0,0,1,1,1,1,1,1,0]
)
MeleeWeapon('Broad Sword',
    weight = 75,
    damage = (4,2,0),
    damage_lg = (6,1,1),
    space = 4,
    speed= 5,
    value = Coin(10,'g'),
    ac_adjust = [-3,-2,-1,0,0,1,1,1,2]
)
MeleeWeapon('Long Sword',
    weight = 60,
    damage = (8,1,0),
    damage_lg = (12,1,0),
    space = 3,
    speed = 5,
    value = Coin(15,'g'),
    ac_adjust = [-2,-1,0,0,0,0,0,1,2]
)
MeleeWeapon('Short Sword',
    weight = 35,
    damage = (6,1,0),
    damage_lg = (8,1,0),
    space = 1,
    speed = 3,
    value = Coin(8,'g'),
    ac_adjust = [-3,-2,-1,0,0,0,1,0,2]
)
MeleeWeapon('Two-Handed Sword',
    weight = 250,
    damage = (10,1,0),
    damage_lg = (6,3,0),
    space = 6,
    speed = 10,
    value = Coin(30,'g'),
    ac_adjust = [2,2,2,2,3,3,3,1,0]
)
MeleeWeapon('Trident',
    weight = 50,
    damage = (6,1,1),
    damage_lg = (4,3,0),
    space = 1,
    speed = 7,
    value = Coin(4,'g'),
    ac_adjust = [-3,-2,-1,-1,0,0,1,0,1]
)
MeleeWeapon('Voulge',
    weight = 125,
    damage = (4,2,0),
    damage_lg = (4,2,0),
    space = 2,
    speed = 10,
    value = Coin(2,'g'),
    ac_adjust = [-1,-1,0,1,1,1,0,0,0]
)
]

def avg_dmg(die,num,mod):
    avg_die = die/2 + 0.5
    
    return ((avg_die * num) + mod)
    
def avg_weapon_dmg(weapon):
    vs_reg = avg_dmg(weapon.die, weapon.num, weapon.mod)
    vs_lg = avg_dmg(weapon.die_lg, weapon.num_lg, weapon.mod_lg)
    
    return [vs_reg, vs_lg]
    
def dmg_sorted(weapon_list=None):
    if weapon_list:
        weapons = weapon_list
    else:
        weapons = all_melee
        
    s = sorted(weapons, key=lambda weapon: avg_weapon_dmg(weapon)[0], reverse=True)
    for w in s:
        print(str(avg_weapon_dmg(w)[0]) + ' ' + str(w))
        
    return s

def dmg_lg_sorted(weapon_list=None):
    if weapon_list:
        weapons = weapon_list
    else:
        weapons = all_melee
        
    s = sorted(weapons, key=lambda weapon: avg_weapon_dmg(weapon)[1], reverse=True)
    for w in s:
        print(str(avg_weapon_dmg(w)[1]) + ' ' + str(w))
    
def speed_sorted(weapon_list=None):
    if weapon_list:
        weapons = weapon_list
    else:
        weapons = all_melee
        
    s = sorted(weapons, key=lambda weapon: weapon.speed)
    for w in s:
        print(str(w.speed) + ' ' + str(w))
        
    return s
