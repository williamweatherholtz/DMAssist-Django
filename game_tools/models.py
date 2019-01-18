from sys import stderr

from django.db import models

from dma.dnd.gem import Gem
from dma.dnd.jewelry import Jewelry

from dma.dnd.treasure import Treasure, gemsValue

from dma.dnd.random_encounters import rollMultipleDays

class GemResults():
    def __init__(self, count):
        treasure = Treasure(gems=count)
        self.gem_list = treasure.gem_list

class JewelryResults():
    def __init__(self, count):
        treasure = Treasure(jewelry=count)
        self.jewelry_list = treasure.jewelry_list

class TreasureTypeResults():
    def __init__(self, t_str):
        treasure = Treasure()
        treasure.rollLoot(t_str)

        self.treasure = str(treasure)
        print('TR {}'.format(self.treasure), stderr)

class TravelResult():
    def __init__(self, days, temp, pop, terrain):
        self.travel_time = days

        if pop == 'Wilderness':
            self.region = '{} Wilderness {}'.format(temp, terrain)
            self.encounters = rollMultipleDays(days, self.region, 'Wilderness')
        elif pop == 'Sparse':
            self.region = '{} Civilized {}'.format(temp, terrain)
            self.encounters = rollMultipleDays(days, self.region, 'Sparse')
        else:
            self.region = '{} Civilized {}'.format(temp, terrain)
            self.encounters = rollMultipleDays(days, self.region, 'Dense')

    def num_days_with_encounters(self):
        return len(self.encounters)

    def num_encounters(self):
        count = 0
        for day in self.encounters:
            count += len(day[1])

        return count
