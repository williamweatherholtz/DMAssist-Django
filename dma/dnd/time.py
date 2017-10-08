from enum import Enum
from decimal import Decimal, getcontext

def test_module():
    #getcontext().prec = 4
    print('GameTime testing...')

    #Example defintion
    period = TimePeriod(Decimal(100), TimeUnit.segment)
    print(period)

    #Conversion testing
    print('{} rounds'.format(period.in_rounds()))

#common time units, values relative to rounds
#assumes 24hr days, 365 day years
class TimeUnit(Enum):
    decisegment = Decimal(.01)
    segment = Decimal(.1)
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

    def in_rounds(self):
        if self.unit is TimeUnit.variable:
            return Decimal(-2)
        elif self.unit is TimeUnit.permanent:
            return Decimal(-1)
        else:
            return self.value * self.unit.value

if __name__ == '__main__':
    test_module()
