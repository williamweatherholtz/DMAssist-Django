from django.conf.urls import url

from .views import index_view, result_view

app_name = 'random_encounters'
urlpatterns = [
    url(r'^$', index_view, name='index'),
    url(r'^result/$', result_view, name='result')
]
