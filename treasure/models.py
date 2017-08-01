from sys import stderr

from django.db import models

from dma.dnd.gem import Gem
from dma.dnd.jewelry import Jewelry

from dma.dnd.treasure import Treasure
  
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