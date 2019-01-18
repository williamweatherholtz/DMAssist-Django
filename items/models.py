from django.db import models

class MagicItem(models.Model):
    slug = models.SlugField(max_length = 75)
    name = models.CharField(max_length = 75, unique=True)
    
    #int representation for MagicItemCategory Enum
    category = models.SmallIntegerField()
    
    #int representation for SourceBook IntEnum
    source = models.SmallIntegerField()
    
    min_xp = models.IntegerField(default=0)
    max_xp = models.IntegerField(default=0)
    
    min_gold = models.IntegerField(default=0)
    max_gold = models.IntegerField(default=0)
    
    #int representation of decisegments
    activation_time = models.IntegerField()
    
    description = models.CharField(max_length=4000, default='')

    def __str__(self):
        return self.name

    def __eq__(self, other):
        my_vars = vars(self)
        their_vars = vars(other)
        
        my_fields = {key: val for key, val in my_vars.items() if key not in ['_state', 'id']}
        their_fields = {key: val for key, val in their_vars.items() if key not in ['_state', 'id']}
        
        return my_fields == their_fields
