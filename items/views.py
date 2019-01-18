from django.shortcuts import render
from django.views import generic

from .models import MagicItem
from .filters import ItemFilter

def item_list(request):
    items = MagicItem.objects.all()
    filter = ItemFilter(request.GET, queryset = items)
    
    return render(request, 'items/index.html', {'filter':filter})
    
class DetailView(generic.DetailView):
    model = MagicItem
    template_name = 'items/detail.html'
    context_object_name = 'item'
