
import sqlite3

from django.db.utils import IntegrityError
from django.core.management.base import BaseCommand
from django.template.defaultfilters import slugify

from spells.models import SpellInfo

from dma.dnd.spells import (
    cleric_spells, druid_spells, mu_spells, illusionist_spells)

class Command(BaseCommand):

    def _create_spells(self):
        num_added = 0
        num_modified = 0
        num_copies = 0

        spell_list = (cleric_spells +
            druid_spells + mu_spells + illusionist_spells)

        for spell in spell_list:
            s = SpellInfo(
                slug = slugify(str(spell)),
                name = spell.name,
                level = spell.level,
                spell_class = spell.role,
                cast_time = spell.cast_time.in_rounds(),
                duration = spell.duration.in_rounds(),
                duration_per_level = spell.duration_per_level.in_rounds(),
                source = spell.sourcebook.value
            )

            try:
                s.save()
            except IntegrityError:
                conflict = SpellInfo.objects.get(slug=slugify(str(spell)))
                if conflict != s:
                    fields = {key: val for key, val in vars(s).items() if key not in ['_state', 'id']}

                    """
                    print(fields)
                    print()
                    print()
                    print(vars(conflict))
                    """
                    any_change = False
                    for field in fields.keys():
                        new_val = getattr(s, field)
                        if new_val != getattr(conflict, field):
                            print('s: {}'.format(new_val))
                            print('conf: {}'.format(getattr(conflict, field)))

                            any_change = True
                            setattr(conflict, field, new_val)

                    if any_change:
                        print('Modified {}...'.format(slugify(str(spell))))
                        conflict.full_clean()
                        conflict.save()
                        num_modified += 1
                    else:
                        num_copies += 1
            else:
                num_added += 1
                print('added {} to database'.format(spell))
        print('{} spell entries added, {} modified, {} identical entries'.format(num_added, num_modified, num_copies))

    def handle(self, *args, **options):
        self._create_spells()
