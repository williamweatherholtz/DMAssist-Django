from django.conf.urls import url

from .views import index_view

app_name = 'spells'
urlpatterns = [
    url(r'^$', index_view, name='view')
]