from django.shortcuts import get_object_or_404, render
from django.views import generic

from .models import CreatureInfo


class IndexView(generic.ListView):
    template_name = 'creatures/index.html'
    context_object_name = 'creature_list'
    
    def get_queryset(self):
        return CreatureInfo.objects.order_by('name')

class DetailView(generic.DetailView):
    model = CreatureInfo
    template_name = 'creatures/detail.html'
    context_object_name = 'creature'
