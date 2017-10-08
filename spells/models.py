from django.db import models

class SpellInfo(models.Model):
    slug = models.SlugField(max_length=75, unique=True)
    name = models.CharField(max_length=75)
    spell_class = models.CharField(max_length=1)
    level = models.SmallIntegerField()
    cast_time = models.DecimalField(max_digits=15, decimal_places=5)
    duration = models.DecimalField(max_digits=20, decimal_places=5)
    duration_per_level = models.DecimalField(max_digits=15, decimal_places=5)
    source = models.CharField(max_length=50)

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
