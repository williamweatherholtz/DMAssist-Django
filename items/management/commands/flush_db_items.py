from django.core.management.base import BaseCommand
from items.models import MagicItem

class Command(BaseCommand):
    def handle(self, *args, **options):
        count = len(MagicItem.objects.all())
        MagicItem.objects.all().delete()
        print('{} MagicItem entries deleted'.format(count))
