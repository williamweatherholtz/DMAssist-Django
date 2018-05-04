from enum import Enum

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class ClassRole(Enum):
    NONE = 0
    FIGHTER = 1
    RANGER = 2
    PALADIN = 3
    CLERIC = 4
    DRUID = 5
    MONK = 6
    MAGIC_USER = 7
    ILLUSIONIST = 8
    THIEF = 9
    ASSASSIN = 10
    ACROBAT = 11
    CAVALIER = 12
    BARBARIAN = 13
    BARD = 14
    LENGTH = 14

class CharacterInfo(models.Model):
    class Meta:
        unique_together = ('user', 'name')
    
    
    user = models.CharField(max_length=75)
    name = models.CharField(max_length=75)
    max_hp = models.PositiveSmallIntegerField()
    race = models.CharField(max_length=75)
    
    str = models.PositiveSmallIntegerField()
    dex = models.PositiveSmallIntegerField()
    con = models.PositiveSmallIntegerField()
    int = models.PositiveSmallIntegerField()
    wis = models.PositiveSmallIntegerField()
    chr = models.PositiveSmallIntegerField()
    com = models.PositiveSmallIntegerField()
    
    class_role = models.PositiveSmallIntegerField(
        validators=[
            MinValueValidator(ClassRole.NONE),
            MaxValueValidator(ClassRole.LENGTH)])
    class_level = models.PositiveSmallIntegerField()
    
    def __str__(self):
        return self.user + ' - ' + self.name
