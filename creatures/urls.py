from django.conf.urls import url

from .views import DetailView, creature_list

app_name = 'creatures'
urlpatterns = [
    url(r'^$', creature_list, name='searcher'),
    url(r'^(?P<slug>[^\n]+)/$', DetailView.as_view(), name='detail'),
]
