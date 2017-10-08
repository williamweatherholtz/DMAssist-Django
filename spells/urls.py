from django.conf.urls import url

from .views import IndexView, spell_list

app_name = 'spells'
urlpatterns = [
    #url(r'^$', IndexView.as_view(), name='index'),
    url(r'^$', spell_list, name='searcher'),
]
