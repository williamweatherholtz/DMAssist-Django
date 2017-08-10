from django.db import models

class SpellInfo(models.Model):
    slug = models.SlugField(max_length=75, unique=True)
    name = models.CharField(max_length=75)
    spell_class = models.CharField(max_length=1)
    level = models.SmallIntegerField()
    
    def __str__(self):
        return self.slug
