from enum import Enum
from decimal import Decimal

def test_module():
    print('GameTime testing...')

    #Example defintion
    period = TimePeriod(5, TimeUnit.round)
    print(period)

#common time units, values relative to rounds
#assumes 24hr days, 365 day years
class TimeUnit(Enum):
    segment = Decimal(0.1)
    round = Decimal(1)
    turn = Decimal(10)
    hour = Decimal(60)
    day = Decimal(1440)
    year = Decimal(525600)
    variable = Decimal('NaN')
    permanent = Decimal('Infinity')

class TimePeriod():
    def __init__(self, val=1, unit=TimeUnit.round):
        self.value = val
        self.unit = unit

    def __str__(self):
        str = '{} {}'.format(self.value, self.unit.name)
        if self.value == 1:
            return str
        else:
            #pluralize
            return str + 's'

if __name__ == '__main__':
    test_module()
