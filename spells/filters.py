import django_filters
from django import forms

from spells.models import SpellInfo, CLASS_CHOICES, SOURCE_CHOICES

class SpellFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(
        lookup_expr='icontains'
    )
    
    description = django_filters.CharFilter(
        lookup_expr='icontains'
    )

    spell_class = django_filters.MultipleChoiceFilter(
        choices = CLASS_CHOICES,
        #empty_label = None,
        widget = forms.CheckboxSelectMultiple
    )
    
    source = django_filters.ChoiceFilter(
        choices = SOURCE_CHOICES,
        empty_label = None,
        widget = forms.Select
    )
    
    level = django_filters.RangeFilter()

    class Meta:
        model = SpellInfo
        
        #form ordering
        fields = [
            'name',
            'spell_class',
            'level',
            'description',
            'source'
        ]
