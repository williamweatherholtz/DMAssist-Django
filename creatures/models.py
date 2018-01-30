from django.db import models

# Create your models here.
class CreatureInfo(models.Model):
    slug = models.SlugField(max_length=75)
    name = models.CharField(max_length=75, unique=True)
    min_hd = models.PositiveSmallIntegerField()
    max_hd = models.PositiveSmallIntegerField()
    min_hp_mod = models.SmallIntegerField()
    max_hp_mod = models.SmallIntegerField()
    min_appearing = models.PositiveSmallIntegerField()
    max_appearing = models.PositiveSmallIntegerField()
    lair_chance = models.DecimalField(max_digits=6, decimal_places=4, default = 0.0)
    base_xp = models.IntegerField(default=0)
    xp_per_hp = models.IntegerField(default=0)
    level = models.IntegerField(null=True)
    
    def __str__(self):
        return self.name
    
    def __eq__(self, other):
        my_vars = vars(self)
        their_vars = vars(other)
        
        my_fields = {key: val for key, val in my_vars.items() if key not in ['_state', 'id']}
        their_fields = {key: val for key, val in their_vars.items() if key not in ['_state', 'id']}
        
        return my_fields == their_fields
