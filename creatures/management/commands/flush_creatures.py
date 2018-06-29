from django.core.management.base import BaseCommand
from creatures.models import CreatureInfo

class Command(BaseCommand):
    def handle(self, *args, **options):
        count = len(CreatureInfo.objects.all())
        CreatureInfo.objects.all().delete()
        print('{} CreatureInfo entries deleted'.format(count))
