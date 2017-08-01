"""
Adds existing creature list from Kivy project to database
"""

from django.core.management.base import BaseCommand
from django.template.defaultfilters import slugify

from creatures.models import CreatureInfo

from .basic_creature_info_definitions import creature_list

class Command(BaseCommand):
    
    def _create_creatures(self):
        for creature in creature_list:
            c = CreatureInfo(
                slug = slugify(creature.name),
                name = creature.name,
                min_hd = creature.hit_dice[0],
                max_hd = creature.hit_dice[1],
                min_hp_mod = creature.hit_point_mod[0],
                max_hp_mod = creature.hit_point_mod[1],
                min_appearing = creature.num_appearing[0],
                max_appearing = creature.num_appearing[1],
                lair_chance = creature.lair_chance,
                base_xp = creature.base_xp,
                level = creature.level
            )
            
            c.save()
            
            print('added {} to database'.format(creature.name))
        
    def handle(self, *args, **options):
        self._create_creatures()