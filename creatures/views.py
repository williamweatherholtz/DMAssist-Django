from django.shortcuts import get_object_or_404, render
from django.views import generic

from .models import CreatureInfo
from .filters import CreatureFilter

def creature_list(request):
    creatures = CreatureInfo.objects.all()
    filter = CreatureFilter(request.GET, queryset = creatures)
    
    return render(request, 'creatures/index.html', {'filter':filter})

class DetailView(generic.DetailView):
    model = CreatureInfo
    template_name = 'creatures/detail.html'
    context_object_name = 'creature'
