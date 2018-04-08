from django.conf.urls import url

from .views import IndexView, creator_view

app_name = 'characters'
urlpatterns = [
    url(r'^$', creator_view, name="index")
]
