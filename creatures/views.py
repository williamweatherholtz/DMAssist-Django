from sys import stderr
from random import randint

from django.shortcuts import get_object_or_404, render, redirect
from django.views import generic

from .models import CreatureInfo
from .filters import CreatureFilter
from .forms import StandardEncounterForm, QuantityEncounterForm

from dma.dnd.creature import roll_standard_encounter

def creature_list(request):
    template = 'creatures/index.html'
    
    creatures = CreatureInfo.objects.all().filter(parent_creature__exact='')
    filter = CreatureFilter(request.GET, queryset = creatures)
    context = {'filter':filter}
    
    return render(request, template, context)

def creature_detail(request, slug):
    template = 'creatures/detail.html'
    
    creature = get_object_or_404(CreatureInfo, slug=slug)
    context = {
        'creature':creature,
        'standard_form':None,
        'quantity_form':None,
    }
    
    if request.method == 'POST':
        redirect_pattern = 'encounter/'
        
        quantity_form = QuantityEncounterForm(request.POST)
        if quantity_form.is_valid():
            quantity = quantity_form.cleaned_data['quantity']
            request.session['quantity'] = quantity
            return redirect(redirect_pattern)
        
        standard_form = StandardEncounterForm(request.POST)
        if standard_form.is_valid():
            request.session['quantity'] = None
            return redirect(redirect_pattern)
            
    else:
        standard_form = StandardEncounterForm()
        quantity_form = QuantityEncounterForm()
        
        context['standard_form'] = standard_form
        context['quantity_form'] = quantity_form
        
    return render(request, template, context)
    
def creature_encounter(request, slug):
    template = 'creatures/encounter.html'
    #TODO: pass this in instead of doing another DB lookup
    creature_info = get_object_or_404(CreatureInfo, slug=slug)
    
    num_creatures = request.session['quantity']
    if not num_creatures:
        num_creatures = randint(creature_info.min_appearing, creature_info.max_appearing)
    
    creature_list = sorted(creature_info.roll_quantity(num_creatures), reverse=True)
    
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
