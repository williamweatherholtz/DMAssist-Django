
import sqlite3

from django.db.utils import IntegrityError
from django.core.management.base import BaseCommand
from django.template.defaultfilters import slugify

from items.models import MagicItem

from dma.dnd.magic_item_definitions import all_items

class Command(BaseCommand):
    
    def _create_items(self):
        num_added = 0
        num_modified = 0
        num_copies = 0
        
        for item in all_items:
            
            m = MagicItem(
                slug = slugify(item.name),
                name = item.name,
                category = item.category.value,
                source = item.source.value,
                min_xp = item.xp_value[0],
                max_xp = item.xp_value[1],
                min_gold = item.gold_value[0],
                max_gold = item.gold_value[1],
                activation_time = item.activation_time.decisegments,
                description = item.description
            )
            
            try:
                m.save()
            except IntegrityError:
                fields_changed = 0
                conflict = MagicItem.objects.get(name=item.name)
                
                if conflict != m:
                    fields = {key: val for key, val in vars(m).items() if key not in ['_state', 'id']}
                    
                    for field in fields.keys():
                        new_val = getattr(m, field)
                        existing_val = getattr(conflict, field)
                        if new_val != existing_val:
                            print('conflict in {}, {} set to {} from {}'.format(
                                m.name, field, new_val, existing_val))
                            fields_changed += 1
                            setattr(conflict, field, new_val)                           
                
                if fields_changed:
                    print('Modified {}'.format(item.name))
                    num_modified += 1
                    conflict.save()
                else:
                    num_copies += 1
            
            else:
                num_added += 1
                print('added {} to database'.format(item.name))
        print('{} item entries added, {} modified, {} identical entries'.format(num_added, num_modified, num_copies))
                    
    def handle(self, *args, **options):
        self._create_items()
