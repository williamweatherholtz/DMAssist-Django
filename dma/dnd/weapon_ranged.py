from dnd.currency import Coin

class RangedWeapon():
    def __init__(self
        name,damage,damage_lg,fire_rate,ranges,ac_adjust):
        
        self.name = name
        self.die = damage[0]
        self.num = damage[1]
        self.mod = damage[2]
        self.die_lg = damage_lg[0]
        self.num_lg = damage_lg[1]
        self.mod_lg = damage_lg[2]
        self.fire_rate = fire_rate
        self.ranges = ranges
        self.ac_adjust = ac_adjust

ranged_weapons = [
RangedWeapon('Hand Axe',
    damage = (6,1,0),
    damage_lg = (4,1,0),
    fire_rate = 1,
    ranges = [1,2,3],
    ac_adjust = [-4,-3,-2,-1,-1,0,0,0,1]
),
RangedWeapon('Composite Long Bow',
    damage = (6,1,0),
    damage_lg = (6,1,0),
    fire_rate = 2,
    ranges = [6,12,21],
    ac_adjust = [-2,-1,0,0,1,2,2,3,3]
),
RangedWeapon('Composite Short Bow',
    damage = (6,1,0),
    damage_lg = (6,1,0),
    fire_rate = 2,
    ranges = [5,10,18],
    ac_adjust = [-3,-3,-1,0,1,2,2,2,3]
),
RangedWeapon('Long Bow',
    damage = (6,1,0),
    damage_lg = (6,1,0),
    fire_rate = 2,
    ranges = [7,14,21],
    ac_adjust = [-1,0,0,1,2,3,3,3,3]
),
RangedWeapon('Short Bow',
    damage = (6,1,0),
    damage_lg = (,,),
    fire_rate = 2,
    ranges = [5,10,15],
    ac_adjust = [-5,-4,-1,0,0,1,2,2,2]
),
RangedWeapon('Club',
    damage = (6,1,0),
    damage_lg = (3,1,0),
    fire_rate = 1,
    ranges = [1,2,3],
    ac_adjust = [-7,-5,-3,-2,-1,-1,-1,0,0]
),
RangedWeapon('Heavy Crossbow',
    damage = (4,1,1),
    damage_lg = (6,1,1),
    fire_rate = 0.5,
    ranges = [8,16,24],
    ac_adjust = [-1,0,1,2,3,3,4,4,4]
),
RangedWeapon('Light Crossbow',
    damage = (4,1,0),
    damage_lg = (4,1,0),
    fire_rate = 1,
    ranges = [6,12,18],
    ac_adjust = [-2,-1,0,0,1,2,3,3,3]
),
RangedWeapon('Dagger',
    damage = (4,1,0),
    damage_lg = (3,1,0),
    fire_rate = 2,
    ranges = [1,2,3],
    ac_adjust = [-5,-4,-3,-2,-1,-1,0,0,1]
),
RangedWeapon('Dart',
    damage = (3,1,0),
    damage_lg = (2,1,0),
    fire_rate = 3,
    ranges = [1.5,3,4.5],
    ac_adjust = [-5,-4,-3,-2,-1,0,1,0,1]
),
RangedWeapon('Hammer',
    damage = (4,1,1),
    damage_lg = (4,1,0),
    fire_rate = 1,
    ranges = [1,2,3],
    ac_adjust = [-2,-1,0,0,0,0,0,0,1]
),
RangedWeapon('Javelin',
    damage = (6,1,0),
    damage_lg = (6,1,0),
    fire_rate = 1,
    ranges = [2,4,6],
    ac_adjust = [-5,-4,-3,-2,-1,0,1,0,1]
),
RangedWeapon('Bullet Sling',
    damage = (4,1,1),
    damage_lg = (6,1,1),
    fire_rate = 1,
    ranges = [5,10,20],
    ac_adjust = [-2,-2,-1,0,0,0,2,1,3]
),
RangedWeapon('Stone Sling',
    damage = (4,1,0),
    damage_lg = (4,1,0),
    fire_rate = 1,
    ranges = [4,8,16],
    ac_adjust = [-5,-4,-2,-1,0,0,2,1,3]
),
RangedWeapon('Spear',
    damage = (6,1,0),
    damage_lg = (8,1,0),
    fire_rate = 1,
    ranges = [1,2,3],
    ac_adjust = [-3,-3,-2,-2,-1,0,0,0,0]
)
]
