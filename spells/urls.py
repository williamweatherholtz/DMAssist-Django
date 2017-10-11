from django.conf.urls import url

from .views import DetailView, spell_list

app_name = 'spells'
urlpatterns = [
    url(r'^$', spell_list, name='searcher'),
    url(r'^(?P<slug>[^\n]+)/$', DetailView.as_view(), name='detail'),
]
