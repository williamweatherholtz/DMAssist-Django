from django.shortcuts import render
from django.views import generic

from .models import SpellInfo

class IndexView(generic.ListView):
    template_name = 'spells/index.html'
    context_object_name = 'spell_list'

    def get_queryset(self):
        return SpellInfo.objects.order_by('name')
