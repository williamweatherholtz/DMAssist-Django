from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from .views import IndexView, DetailView, creator_view, importer_view

app_name = 'characters'
urlpatterns = [
    url(r'^$', login_required(IndexView.as_view()), name="index"),
    url(r'^import/$', importer_view, name="import"),
    url(r'^create/$', creator_view, name="create"),
    url(r'^(?P<slug>[^\n]+)/$', DetailView.as_view(), name='detail'),
]
