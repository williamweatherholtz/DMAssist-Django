from django.conf.urls import url

from .views import creature_detail, creature_list, creature_encounter

app_name = 'creatures'
urlpatterns = [
    url(r'^$', creature_list, name='searcher'),
    url(r'^(?P<slug>[^\n]+)/encounter/$', creature_encounter, name='encounter'),
    url(r'^(?P<slug>[^\n]+)/$', creature_detail, name='detail'),  
]
