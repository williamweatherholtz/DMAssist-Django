from django.conf.urls import url

from .views import IndexView, creator_view, importer_view

app_name = 'characters'
urlpatterns = [
    url(r'^$', importer_view, name="index")
]
