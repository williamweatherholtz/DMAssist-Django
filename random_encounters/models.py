from django.db import models

from dma.dnd.random_encounters import rollMultipleDays 

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
