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



#common time units, values relative to decisegments
#assumes 24hr days, 365 day years
class TimeUnit(Enum):
    decisegment = 1
    segment = 10
    round = 100
    turn = 1000
    hour = 6000
    day = 144000
    year = 525600
    variable = -1
    permanent = -2

#Take a integer value of decisegments
#Return the largest evenly divisible unit
def simplify(ds):
    val = ds
    for unit in list(TimeUnit)[-3::-1]:
        if val >= unit.value:
            if val % unit.value == 0:
                return TimePeriod(val//unit.value, unit)

    return TimePeriod(val, unit)

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

    @property
    def decisegments(self):
        if self.unit is TimeUnit.variable:
            return -1
        elif self.unit is TimeUnit.permanent:
            return -2
        else:
            return self.value * self.unit.value

if __name__ == '__main__':
    test_module()
