from django.db import models

from dma.dnd.random_encounters import rollMultipleDays 

class TravelResult():
    def __init__(self, days, temp, pop, terrain):
        if pop == 'Wilderness':
            self.encounters = rollMultipleDays(days, '{} Wilderness {}'.format(temp, terrain), 'Wilderness')
        elif pop == 'Rural':
            self.encounters = rollMultipleDays(days, '{} Civilized {}'.format(temp, terrain), 'Sparse')
        else:
            self.encounters = rollMultipleDays(days, '{} Civilized {}'.format(temp, terrain), 'Dense')
