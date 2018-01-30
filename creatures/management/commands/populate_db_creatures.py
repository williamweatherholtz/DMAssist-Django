"""
Adds existing creature list from Kivy project to database
"""

import sqlite3

from django.db.utils import IntegrityError
from django.core.management.base import BaseCommand
from django.template.defaultfilters import slugify

from creatures.models import CreatureInfo

from dma.dnd.basic_creature_info_definitions import creature_list

class Command(BaseCommand):

    def _create_creatures(self):
        num_added = 0
        num_modified = 0

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
                xp_per_hp = creature.xp_per_hp,
                level = creature.level
            )

            try:
                c.save()
            except IntegrityError:
                conflict = CreatureInfo.objects.get(name=creature.name)

                if conflict != c:
                    fields = {key: val for key, val in vars(c).items() if key not in ['_state', 'id']}

                    print(fields)
                    print()
                    print(vars(conflict))

                    for field in fields.keys():
                        new_val = getattr(c, field)
                        if new_val != getattr(conflict, field):
                            setattr(conflict, field, new_val)

                    conflict.save()

                    num_modified += 1

            else:
                num_added += 1
                print('added {} to database'.format(creature.name))

        print('{} creature entries added, {} modified'.format(num_added, num_modified))

    def handle(self, *args, **options):
        self._create_creatures()
