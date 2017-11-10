from .currency import Wealth
from .roll import roll
from .gem import Gem
from .jewelry import Jewelry

from .treasure_map import Map
from .magic_item import (generateMagicItem, generatePotion,
    generateScroll,generateRing, generateRod, generateArmorShield,
    generateMiscMagic,generateRodStaffWand)
from .magic_weapon import generateSword, generateMiscWeapon

from random import random, randint
from sys import stderr



def __main__():
    while True:
        inp = input('Enter gem count:')
        g_num = int(inp)
        inp = input('Enter jewelry count:')
        j_num = int(inp)

        t = Treasure(gems=g_num,jewelry=j_num)
        print(t)

class Treasure():
    def __init__(self, wealth=None,maps=[],items=[],gems=0,jewelry=0):
        if wealth: self.wealth=wealth
        else: self.wealth = Wealth(0,0,0,0,0)

        self.maps = []
        self.maps.extend(maps)
        self.items = []
        self.items.extend(items)

        self.gem_count=gems #why was I delaying this?
        self.jewelry_count=jewelry #why was I delaying this?
        self.gem_list = []
        self.jewelry_list = []
        self.convertGemsJewelry()

    def clear(self):
        self.wealth = Wealth(0,0,0,0,0)
        del self.maps[:]
        del self.items[:]
        self.gem_count = 0
        self.jewelry_count = 0
        del self.gem_list[:]
        del self.jewelry_list[:]

    def addGems(self, count):
        self.gem_count += count
        self.convertGemsJewelry()

    def addJewelry(self, count):
        self.jewelry_count += count
        self.convertGemsJewelry()

    def addItem(self,item):
        self.items.extend(item)

    def addTreasure(self, t):
        if t.wealth: self.wealth.addWealth(t.wealth)
        self.maps.extend(t.maps)
        self.items.extend(t.items)
        self.gem_count += t.gem_count
        self.jewelry_count += t.jewelry_count

        self.convertGemsJewelry()

    def __bool__(self):
        if (self.wealth or self.items or self.gem_list
                or self.jewelry_list or self.maps):
            return True
        else:
            return False

    def __str__(self):
        if not(self):
            return 'No treasure'

        output = ''

        if self.wealth:
            output = 'COINS:\n------\n{}\n'.format(self.wealth)

        self.convertGemsJewelry()



        if len(self.gem_list):
            val = gemsValue(self.gem_list)
            string = '\n{} GEMS WORTH TOTAL OF {}\n'.format(len(self.gem_list),val)
            string += '-'*(len(string)-3)
            output += string

            for gem in self.gem_list:
                output += '\n'+str(gem)

        if len(self.jewelry_list):
            val = jewelryValue(self.jewelry_list)
            string = '\n\n{} PIECES OF JEWELRY WORTH TOTAL OF {}\n'.format(len(self.jewelry_list),val)
            string += '-'*(len(string)-4)
            output += string
            for jewelry in self.jewelry_list:
                output += '\n'+str(jewelry)

        if len(self.items):
            output += '\n\nITEMS:\n------'
            for item in self.items:
                output += '\n'+str(item)

        if len(self.maps):
            output += '\n\nMAPS:\n-----'
            for map in self.maps:
                output += '\n'+str(map)

        return output

    def convertGemsJewelry(self):
        if self.jewelry_count:
            for i in range(self.jewelry_count):
                self.jewelry_list.append(Jewelry())
            self.jewelry_list = sorted(self.jewelry_list, reverse=True)
            self.jewelry_count = 0

        if self.gem_count:
            for i in range(self.gem_count):
                g = Gem()

                self.gem_list.append(g)
            self.gem_list = sorted(self.gem_list, reverse=True)
            self.gem_count = 0


    def rollLoot(self, t_types, num_enemies=1):
        self.clear()
        loot = generateLootFromString(t_types)

        self.addTreasure(loot)

        return loot

def gemsValue(gem_list):
    value = Wealth(0,0,0,0,0)
    for gem in gem_list:
        value.addCoins(gem.value)
    return value

def jewelryValue(jewelry_list):
    value = Wealth(0,0,0,0,0)
    for jewelry in jewelry_list:
        value.addCoins(jewelry.base_value)
    return value


#takes a str of treasure types (a-z), rolling loot for each
def generateLootFromString(types_str, num_enemies=1):
    t = Treasure()

    for char in types_str:
        t.addTreasure( generateLoot(char, num_enemies))

    return t

#The treasure tables apply to treasure found in outdoor lairs
#Dungeon treasure are meant to be handpicked by the DM
def generateLoot(t_type, num_enemies=1):
    t_type = t_type.upper()
    cp=0; sp=0; ep=0; gp=0; pp=0
    maps = []
    items = []
    gems = 0
    jewelry = 0

    if t_type == 'A':
        if random() < 0.25: cp = 1000 * roll(6)
        if random() < 0.3: sp = 1000 * roll(6)
        if random() < 0.35: ep = 1000 * roll(6)
        if random() < 0.4: gp = 1000 * roll(10)
        if random() < 0.25: pp = 100 * roll(4)

        if random() < 0.6: gems = roll(4,10)
        if random() < 0.5: jewelry = roll(3,10)

        if random() < 0.3:
            for i in range(3):
                if roll(100) < 11: maps.append(Map())
                else: items.append(generateMagicItem())
    elif t_type == 'B':
        if random() < 0.5: cp = 1000 * roll(8)
        if random() < 0.25: sp = 1000 * roll(6)
        if random() < 0.25: ep = 1000 * roll(4)
        if random() < 0.25: gp = 1000 * roll(3)

        if random() < 0.3: gems = roll(8)
        if random() < 0.2: jewelry = roll(4)

        if random() < 0.1:
            r = roll(3)
            if r == 1: items.append(generateSword())
            elif r == 2: items.append(generateArmorShield())
            else: items.append(generateMiscWeapon())
    elif t_type == 'C':
        if random() < 0.2: cp = 1000 * roll(12)
        if random() < 0.3: sp = 1000 * roll(6)
        if random() < 0.1: ep = 1000 * roll(4)

        if random() < 0.25: gems = roll(6)
        if random() < 0.2: jewelry = roll(3)

        if random() < 0.1:
            for i in range(2):
                if roll(100) < 11: maps.append(Map())
                else: items.append(generateMagicItem())
    elif t_type == 'D':
        if random() < 0.1: cp = 1000 * roll(8)
        if random() < 0.15: sp = 1000 * roll(12)
        if random() < 0.15: ep = 1000 * roll(8)
        if random() < 0.5: gp = 1000 * roll(6)

        if random() < 0.3: gems = roll(10)
        if random() < 0.25: jewelry = roll(6)

        if random() < 0.15:
            items.append(generatePotion())
            for i in range(2):
                if roll(100) < 11: maps.append(Map())
                else: items.append(generateMagicItem())
    elif t_type == 'E':
        if random() < 0.5: cp = 1000 * roll(10)
        if random() < 0.25: sp = 1000 * roll(12)
        if random() < 0.25: ep = 1000 * roll(6)
        if random() < 0.25: gp = 1000 * roll(8)

        if random() < 0.15: gems = roll(12)
        if random() < 0.1: jewelry = roll(8)

        if random() < 0.25:
            items.append(generateScroll())
            for i in range(3):
                if roll(100) < 11: maps.append(Map())
                else: items.append(generateMagicItem())
    elif t_type == 'F':
        if random() < 0.10: sp = 1000 * roll(20)
        if random() < 0.15: ep = 1000 * roll(12)
        if random() < 0.40: gp = 1000 * roll(10)
        if random() < 0.35: pp = 100 * roll(8)

        if random() < 0.2: gems = roll(10,3)
        if random() < 0.1: jewelry = roll(10)

        if random() < 0.3:
            items.append(generatePotion())
            items.append(generateScroll())
            for i in range(3):
                if roll(100) < 11: maps.append(Map())
                else: items.append(generateMagicItem(restrict_weapons=True))
    elif t_type == 'G':
        if random() < 0.5: gp = 1000 * roll(4,10)
        if random() < 0.5: pp = 100 * roll(20)

        if random() < 0.3: gems = roll(4,5)
        if random() < 0.25: jewelry = roll(10)

        if random() < 0.35:
            items.append(generateScroll())
            for i in range(4):
                if roll(100) < 11: maps.append(Map())
                else: items.append(generateMagicItem())
    elif t_type == 'H':
        if random() < 0.25: cp = 1000 * roll(6,5)
        if random() < 0.4: sp = 1000 * roll(100)
        if random() < 0.4: ep = 1000 * roll(10,4)
        if random() < 0.55: gp = 1000 * roll(10,6)
        if random() < 0.25: pp = 100 * roll(10,5)

        if random() < 0.5: gems = roll(100)
        if random() < 0.5: jewelry = roll(4,10)

        if random() < 0.15:
            items.append(generatePotion())
            items.append(generateScroll())
            for i in range(4):
                if roll(100) < 11: maps.append(Map())
                else: items.append(generateMagicItem())
    elif t_type == 'I':
        if random() < 0.3: pp = 100 * roll(6,3)

        if random() < 0.55: gems = roll(10,2)
        if random() < 0.5: jewelry = roll(12)

        if random() < 0.15:
            if roll(100) < 11: maps.append(Map())
            else: items.append(generateMagicItem())
    elif t_type == 'J':
        for i in range(num_enemies):
            cp += roll(8,3)
    elif t_type == 'K':
        for i in range(num_enemies):
            sp += roll(6,3)
    elif t_type == 'L':
        for i in range(num_enemies):
            ep += roll(6,2)
    elif t_type == 'M':
        for i in range(num_enemies):
            gp += roll(4,2)
    elif t_type == 'N':
        for i in range(num_enemies):
            pp += roll(6)
    elif t_type == 'O':
        if random() < 0.25: cp = 1000 * roll(4)
        if random() < 0.2: sp = 1000 * roll(3)
    elif t_type == 'P':
        if random() < 0.3: sp = 1000 * roll(6)
        if random() < 0.25: ep = 1000 * roll(2)
    elif t_type == 'Q':
        if random() < 0.5: gems = roll(4)
    elif t_type == 'R':
        if random() < 0.4: gp = 1000 * roll(4,2)
        if random() < 0.5: pp = 100 * roll(10,6)

        if random() < 0.55: gems = roll(8,4)
        if random() < 0.45: jewelry = roll(12)
    elif t_type == 'S':
        if random() < 0.4:
            for i in range(roll(4,2)):
                items.append(generatePotion())
    elif t_type == 'T':
        if random() < 0.5:
            for i in range(roll(4)):
                items.append(generateScroll())
    elif t_type == 'U':
        if random() < 0.9: gems = roll(8,10)
        if random() < 0.8: jewelry = roll(6,5)

        if random() < 0.7:
            items.append(generateRing())
            items.append(generateRodStaffWand())
            items.append(generateMiscMagic())
            items.append(generateArmorShield())
            items.append(generateSword())
            items.append(generateMiscWeapon())
    elif t_type == 'V':
        if random() < 0.85:
            for i in range(2):
                items.append(generateRing())
                items.append(generateRodStaffWand())
                items.append(generateMiscMagic())
                items.append(generateArmorShield())
                items.append(generateSword())
                items.append(generateMiscWeapon())
    elif t_type == 'W':
        if random() < 0.6: gp = 1000 * roll(6,5)
        if random() < 0.15: pp = 100 * roll(8)

        if random() < 0.6: gems = roll(8,10)
        if random() < 0.5: jewelry = roll(8,5)

        if random() < 0.55:
            maps.append(Map())
    elif t_type == 'X':
        if random() < 0.6:
            items.append(generatePotion())
            items.append(generateMiscMagic())
    elif t_type == 'Y':
        if random() < 0.7: gp = 1000 * roll(6,2)
    elif t_type == 'Z':
        if random() < 0.2: cp = 1000 * roll(3)
        if random() < 0.25: sp = 1000 * roll(4)
        if random() < 0.25: ep = 1000 * roll(4)
        if random() < 0.3: gp = 1000 * roll(4)
        if random() < 0.3: pp = 100 * roll(6)

        if random() < 0.55: gems = roll(6,10)
        if random() < 0.5: jewelry = roll(6,5)

        if random() < 0.5:
            for i in range(3):
                items.append(generateMagicItem())

    wealth =  Wealth(cp,sp,ep,gp,pp)

    return Treasure(wealth,maps,items,gems,jewelry)


if __name__ == '__main__':
    __main__()




