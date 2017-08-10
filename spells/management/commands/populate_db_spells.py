
import sqlite3

from django.db.utils import IntegrityError
from django.core.management.base import BaseCommand
from django.template.defaultfilters import slugify

from spells.models import SpellInfo

from dma.dnd.spells import (
    cleric_spells, druid_spells, mu_spells, illusionist_spells)
    
class Command(BaseCommand):

    def _create_spells(self):
        spell_list = (cleric_spells +
            druid_spells + mu_spells + illusionist_spells)
    
        print(spell_list)
    
        for spell in spell_list:
            s = SpellInfo(
                slug = slugify(str(spell)),
                name = spell.name,
                level = spell.level,
                spell_class = spell.role
            )
            
            try:
                s.save()
            except IntegrityError:
                print('{} already in database'.format(spell))
            else:
                print('added {} to database'.format(spell))
                
    def handle(self, *args, **options):
        self._create_spells()
