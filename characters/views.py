from django.views import generic
from django.shortcuts import render, redirect, render_to_response
from django.db import IntegrityError
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from .forms import ImportForm, CreateForm
from .models import CharacterInfo

@login_required
def importer_view(request):
    if request.method == 'POST':
        form = ImportForm(request.POST)
        
        print('form POST')
        if form.is_valid():
            char_entry = CharacterInfo()
            char_entry.user = request.user.get_username()
            char_entry.name = form.cleaned_data['name']
            char_entry.str = form.cleaned_data['str']
            char_entry.dex = form.cleaned_data['dex']
            char_entry.con = form.cleaned_data['con']
            char_entry.int = form.cleaned_data['int']
            char_entry.wis = form.cleaned_data['wis']
            char_entry.chr = form.cleaned_data['chr']
            char_entry.com = form.cleaned_data['com']
            char_entry.class_role = form.cleaned_data['class_role']
            char_entry.class_level = form.cleaned_data['level']
            char_entry.max_hp = form.cleaned_data['hp']
            
            try:
                char_entry.save()
            except IntegrityError as e:
                print(e.__cause__)
                
            return HttpResponseRedirect('/characters')
            
    else:
        form = ImportForm()

    return render(
        request, 'characters/import.html',
        {'form':form}
    )

@login_required
def creator_view(request):
    if request.method == 'POST':
        form = CreateForm(request.POST)
         
    else:
        form = CreateForm()
    
    return render(
        request, 'characters/create.html',
        {'form':form}
    )

class IndexView(generic.ListView):
    model = CharacterInfo
    template_name = 'characters/index.html'
    
    def get_queryset(self):
        try:
            queryset = CharacterInfo.objects.filter(user=self.request.user)
        except CharacterInfo.DoesNotExist:
            queryset = None
        return queryset

