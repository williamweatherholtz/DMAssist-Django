from enum import IntEnum

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class CharClassType(IntEnum):
    SINGLE = 0
    DUAL = 1
    MULTI = 2

class ClassRole(IntEnum):
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
    
    @property
    def pretty_name(self):
        return classCodeToStr(self.value)

#Enum for player character races. Double underscore represents a dash (-).
class Race(IntEnum):
    NONE = 0
    GRAY_DWARF = 1
    HILL_DWARF = 2
    MOUNTAIN_DWARF = 3
    DARK_ELF = 4
    GRAY_ELF = 5
    VALLEY_ELF = 6
    WILD_ELF = 7
    WOOD_ELF = 8
    DEEP_GNOME = 9
    SURFACE_GNOME = 10
    HALF__ELF = 11
    HALFLING = 12
    HALF__ORC = 13
    HUMAN = 14
    LENGTH = 14
    
    @property
    def pretty_name(self):
        return raceCodeToStr(self.value)
    
#convert a class code number to a capitalized string
def classCodeToStr(code):
    name = ClassRole(code).name
    return name.title().replace('_', ' ')

#converts the enum name to a formatted string
def raceCodeToStr(code):
    name = Race(code).name.title()
    name = name.replace('__', '-')
    return name.replace('_', ' ')

class CharacterInfo(models.Model):
    #DEFAULT_AUTO_FIELD = models.BigAutoField()
    slug = models.CharField(max_length=151)
    user = models.CharField(max_length=75)
    name = models.CharField(max_length=75)
    max_hp = models.PositiveSmallIntegerField()
    race = models.PositiveSmallIntegerField(
        validators=[MaxValueValidator(ClassRole.LENGTH)])
    str = models.PositiveSmallIntegerField()
    dex = models.PositiveSmallIntegerField()
    con = models.PositiveSmallIntegerField()
    int = models.PositiveSmallIntegerField()
    wis = models.PositiveSmallIntegerField()
    chr = models.PositiveSmallIntegerField()
    com = models.PositiveSmallIntegerField()
    
    class_type = models.PositiveSmallIntegerField(
        validators = [MaxValueValidator(CharClassType.MULTI)],
        default = CharClassType.SINGLE
    )
    
    class_role = models.PositiveSmallIntegerField(
        validators=[MaxValueValidator(ClassRole.LENGTH)])
    class_level = models.PositiveSmallIntegerField()

    class2 = models.PositiveSmallIntegerField(
        validators=[MaxValueValidator(ClassRole.LENGTH)],
        null=True,
        blank=True)
    class2_level = models.PositiveSmallIntegerField(
        null=True,
        blank=True)

    class3 = models.PositiveSmallIntegerField(
        validators=[MaxValueValidator(ClassRole.LENGTH)],
        null=True,
        blank=True)
    class3_level = models.PositiveSmallIntegerField(
        null=True,
        blank=True)
    
    def __str__(self):
        return self.name + ': ' + classCodeToStr(self.class_role)
