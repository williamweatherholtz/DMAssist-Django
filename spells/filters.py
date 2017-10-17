import django_filters

from spells.models import SpellInfo

class SpellFilter(django_filters.FilterSet):
    class Meta:
        model = SpellInfo
        fields = {
            'slug': ['contains'],
            'description': ['contains']
        }
