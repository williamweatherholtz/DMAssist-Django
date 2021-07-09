from django.conf.urls import url
from django.urls import path

from .views import DetailView, spell_list

app_name = 'spells'
urlpatterns = [
    path('', spell_list, name='searcher'),
    path('<slug:slug>/', DetailView.as_view(), name="detail"),
]
