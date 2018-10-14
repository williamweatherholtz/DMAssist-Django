"""
Adds existing creature list from Kivy project to database
"""

import sqlite3
import json

from django.db.utils import IntegrityError
from django.core.management.base import BaseCommand
from django.template.defaultfilters import slugify

from creatures.models import CreatureInfo

from dma.dnd.creature_info_definitions import creature_list

class Command(BaseCommand):

    def _create_creatures(self):
        num_added = 0
        num_modified = 0

        for creature in creature_list:
            if len(creature.attacks):
                _attacks = json.dumps(creature.attacks)
            else: _attacks = ''

            if creature.parent_creature:
                _parent_creature = creature.parent_creature
            else: _parent_creature = ''

            if len(creature.sub_creatures):
                _sub_creatures = json.dumps(creature.sub_creatures)
            else: _sub_creatures = ''

            if len(creature.alternate_names):
                _alt_names = json.dumps(creature.alternate_names)
            else: _alt_names = ''

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
                level = creature.level,

                treasure_types = creature.treasure,
                iq_class = creature.iq.value,
                ground_speed = creature.speed,
                air_speed = creature.fly_speed,
                flight_class = creature.flight_class,
                water_speed = creature.swim_speed,
                burrow_speed = creature.burrow_speed,
                climb_speed = creature.climb_speed,
                web_speed = creature.web_speed,
                ac = creature.ac,
                attacks = _attacks,
                psi_attack_min = creature.psi_str[0][0],
                psi_attack_max = creature.psi_str[0][1],
                psi_defense_min = creature.psi_str[1][0],
                psi_defense_max = creature.psi_str[1][1],
                psi_modes = creature.psi_modes,
                magic_resist = creature.magic_resist,
                alignment = creature.alignment,
                size_class = creature.size_class,

                source = creature.source.value,
                is_abstract = creature.is_abstract,
                parent_creature = _parent_creature,
                sub_creatures = _sub_creatures,
                alt_names = _alt_names,

                description = creature.description
            )

            try:
                c.save()
            except IntegrityError:
                fields_changed = 0
                conflict = CreatureInfo.objects.get(name=creature.name)

                if conflict != c:
                    fields = {key: val for key, val in vars(c).items() if key not in ['_state', 'id']}

                    for field in fields.keys():
                        new_val = getattr(c, field)
                        existing_val = getattr(conflict, field)
                        if new_val != existing_val:
                            print('conflict in {}, {} set to {} from {}'.format(
                                c.name, field, new_val, existing_val))
                            fields_changed += 1
                            setattr(conflict, field, new_val)

                if fields_changed:
                    num_modified += 1
                    conflict.save()

            else:
                num_added += 1
                print('added {} to database'.format(creature.name))

        print('{} creature entries added, {} modified'.format(num_added, num_modified))

    def handle(self, *args, **options):
        self._create_creatures()
