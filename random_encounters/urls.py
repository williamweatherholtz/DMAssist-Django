from django.conf.urls import url

from .views import index_view

app_name = 'random_encounters'
urlpatterns = [
    url(r'^$', index_view, name='index')
]