from django.views import generic
from django.shortcuts import render, redirect

from .forms import ImportForm, CreateForm, AttributesForm

def creator_view(request):
    if request.method == 'POST':
        form = CreateForm(request.POST)
    else:
        form = CreateForm()
    
    attr_form = AttributesForm()
    return render(
        request, 'characters/create.html',
        {'form':form,
         'attr_form':attr_form,}
    )
    
def importor_view(request):
    if request.method == 'POST':
        form = ImportForm(request.POST)
    else:
        form = ImportForm()
    
    return render(
        request, 'characters/import.html',
        {'form':form}
    )

class IndexView(generic.TemplateView):
    template_name = 'characters/index.html'
