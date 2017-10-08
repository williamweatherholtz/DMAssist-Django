from django.core.management.base import BaseCommand
from spells.models import SpellInfo

class Command(BaseCommand):
    def handle(self, *args, **options):
        count = len(SpellInfo.objects.all())
        SpellInfo.objects.all().delete()
        print('{} SpellInfo entries deleted'.format(count))
