import django_filters
from django import forms

from items.models import MagicItemModel

class ItemFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(
        lookup_expr='icontains'
    )
    
    class Meta:
        model = MagicItemModel
        
        fields = [
            'name'
        ]
