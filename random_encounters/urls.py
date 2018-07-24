from django.conf.urls import url

from .views import travel_view, result_view

app_name = 'random_encounters'
urlpatterns = [
    url(r'^$', travel_view, name='travel'),
    url(r'^result/$', result_view, name='result')
]
