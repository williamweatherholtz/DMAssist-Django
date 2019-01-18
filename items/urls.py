from django.conf.urls import url

from .views import DetailView, item_list

app_name = 'items'

urlpatterns = [
    url(r'^$', item_list, name='searcher'),
    url(r'^(?P<slug>[^\n]+)/$', DetailView.as_view(), name='detail'),
]