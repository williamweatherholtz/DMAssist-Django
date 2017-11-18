import django_filters
from django import forms

from spells.models import SpellInfo, CLASS_CHOICES
from spells.forms import SpellForm

def spell_class_query(request):
    if request is None:
        return SpellInfo.objects.none()
        
    return SpellInfo.objects.all()

class SpellFilter(django_filters.FilterSet):
    spell_class = django_filters.ChoiceFilter(
        choices = CLASS_CHOICES,
        empty_label = None,
        widget = forms.Select
    )
    
    level = django_filters.RangeFilter()

    class Meta:
        model = SpellInfo
        fields = {
            'name': ['contains'],
            'description': ['contains'],
        }
        form = SpellForm
