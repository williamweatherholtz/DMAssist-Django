from django.db import models
from dma.dnd.time import simplify

class SpellInfo(models.Model):
    slug = models.SlugField(max_length=75, unique=True)
    name = models.CharField(max_length=75)
    spell_class = models.CharField(max_length=1)
    level = models.SmallIntegerField()
    cast_time = models.IntegerField()
    duration = models.IntegerField()
    duration_per_level = models.IntegerField()
    source = models.CharField(max_length=50)
    description = models.TextField(default="Missing description")

    def __str__(self):
        role = 'Unknown'
        if self.spell_class == 'C':
            role = 'Cleric'
        elif self.spell_class == 'M':
            role = 'Magic User'
        elif self.spell_class == 'D':
            role = 'Druid'
        elif self.spell_class == 'I':
            role = 'Illusionist'

        return '{} -  {} Level {} '.format(self.name, role, self.level)

    @property
    def cast_str(self):
        return simplify(self.cast_time)

    @property
    def duration_str(self):
        fixed_dur = None
        lvl_dur = None

        if (self.duration > 0):
            fixed_dur = simplify(self.duration)
        elif self.duration == -1:
            fixed_dur = 'Variable'
        elif self.duration == -2:
            fixed_dur = 'Permanent'

        if (self.duration_per_level > 0):
            lvl_dur = simplify(self.duration_per_level)

        if fixed_dur:
            if lvl_dur:
                return '{} + {}/level'.format(fixed_dur, lvl_dur)
            else:
                return str(fixed_dur)
        elif lvl_dur:
                return '{}/level'.format(str(lvl_dur))

        return 'N/A'
