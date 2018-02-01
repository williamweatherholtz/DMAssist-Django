from django.shortcuts import get_object_or_404, render, redirect
from django.views import generic

from .models import CreatureInfo
from .filters import CreatureFilter
from .forms import StandardEncounterForm

from dma.dnd.creature import roll_standard_encounter 

def creature_list(request):
    template = 'creatures/index.html'
    
    creatures = CreatureInfo.objects.all()
    filter = CreatureFilter(request.GET, queryset = creatures)
    context = {'filter':filter}
    
    return render(request, template, context)

def creature_detail(request, slug):
    template = 'creatures/detail.html'
    
    creature = get_object_or_404(CreatureInfo, slug=slug)
    context = {'creature':creature}
    
    if request.method == 'POST':
        redirect_pattern = 'encounter/'
        form = StandardEncounterForm(request.POST)
        if form.is_valid():
            return redirect(redirect_pattern)
    else:
        form = StandardEncounterForm()
        
    return render(request, template, context)
    
def creature_encounter(request, slug):
    template = 'creatures/encounter.html'
    #TODO: pass this in instead of doing another DB lookup
    creature_info = get_object_or_404(CreatureInfo, slug=slug)
    creature_list = sorted(creature_info.roll_standard_encounter(), reverse=True)
    xp_total = 0
    for c in creature_list:
        xp_total += c.xp
    context = {
        'creature_info':creature_info,
        'creatures':creature_list,
        'xp_total':xp_total,
        'creature_count':len(creature_list)
    }

    return render(request, template, context)
