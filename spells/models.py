from django.db import models

class SpellInfo(models.Model):
    slug = models.SlugField(max_length=75, unique=True)
    name = models.CharField(max_length=75)
    spell_class = models.CharField(max_length=1)
    level = models.SmallIntegerField()
    
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
