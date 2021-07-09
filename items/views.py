from django.shortcuts import render
from django.views import generic

from .models import MagicItemModel
from .filters import ItemFilter

def item_list(request):
    items = MagicItemModel.objects.all()
    filter = ItemFilter(request.GET, queryset = items)
    
    return render(request, 'items/index.html', {'filter':filter})
    
class DetailView(generic.DetailView):
    model = MagicItemModel
    template_name = 'items/detail.html'
    context_object_name = 'item'
