import sys

from django.shortcuts import render, redirect
from django.views.generic.edit import FormView

from .forms import ItemCountForm, TreasureTypeForm

from .models import GemResults, JewelryResults, TreasureTypeResults

#base for gems and jewelry views
def item_count_view(request, url, redirect_pattern, items_name):
    form_label = 'Number of ' + items_name
    if request.method == 'POST':
        form = ItemCountForm(request.POST)
        if form.is_valid():
            request.session['item_count'] = form.cleaned_data['item_count']
            return redirect(redirect_pattern)
    else:
        form = ItemCountForm()
        form.fields["item_count"].label = form_label

    return render(request, url, {'form': form})
    
def gems_view(request):
    return item_count_view(request, 'game_tools/gems.html', '/game_tools/gems/result', 'Gems')
   
def jewelry_view(request):
    return item_count_view(request, 'game_tools/jewelry.html', '/game_tools/jewelry/result', 'Jewelry')

def gems_result_view(request):
    gem_count = request.session['item_count']
    gem_list = GemResults(gem_count).gem_list
    return render(
        request, 'game_tools/gems_result.html',
        {'gem_count': gem_count, 'gem_list' : gem_list}
    )

def jewelry_result_view(request):
    jewelry_count = request.session['item_count']
    jewelry_list = JewelryResults(jewelry_count).jewelry_list
    
    return render(
        request, 'game_tools/jewelry_result.html',
        {'jewelry_count': jewelry_count, 'jewelry_list': jewelry_list}
    )
  
def t_types_view(request):
    if request.method == 'POST':
        form = TreasureTypeForm(request.POST)
        if form.is_valid():
            request.session['t_types_str'] = form.cleaned_data['types_str']
            return redirect('/game_tools/t_types/result')
    else:
        form = TreasureTypeForm()
        
    return render(request, 'game_tools/t_types.html', {'form': form})
    
def t_types_result_view(request):
    t_types = request.session['t_types_str']
    treasure = TreasureTypeResults(t_types).treasure
    
    
    return render(request, 'game_tools/t_types_result.html', {'treasure': treasure})

