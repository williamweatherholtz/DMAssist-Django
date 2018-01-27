import django_filters
from django import forms

from creatures.models import CreatureInfo

class CreatureFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    
    class Meta:
        model = CreatureInfo
        fields = [
            'name',
            'level',
            'base_xp'
        ]
