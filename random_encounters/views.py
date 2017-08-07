from sys import stderr

from django.shortcuts import render, redirect

from .forms import TravelForm
from .models import TravelResult

def index_view(request):
    if request.method == 'POST':
        form = TravelForm(request.POST)
        if form.is_valid():
            request.session['days'] = form.cleaned_data['days']
            request.session['temperature'] = form.cleaned_data['temperature']
            request.session['population'] = form.cleaned_data['population']
            request.session['terrain'] = form.cleaned_data['terrain']
            return redirect('/random_encounters/result')
    else:
        form = TravelForm()
        
    return render(
        request, 'random_encounters/index.html',
        {'form': form}
    )
        
def result_view(request):
    encounters = TravelResult(
        request.session['days'],
        request.session['temperature'],
        request.session['population'],
        request.session['terrain']).encounters
    
    return render(request, 'random_encounters/result.html', {'encounters': encounters})
