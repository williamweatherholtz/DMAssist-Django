from django.core.management.base import BaseCommand
from items.models import MagicItemModel

class Command(BaseCommand):
    def handle(self, *args, **options):
        count = len(MagicItemModel.objects.all())
        MagicItemModel.objects.all().delete()
        print('{} MagicItemModel entries deleted'.format(count))
