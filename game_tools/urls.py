from django.conf.urls import url
from django.urls import path
from django.views.generic import RedirectView

from .views import (
    gems_view, gems_result_view,
    jewelry_view, jewelry_result_view,
    t_types_view, t_types_result_view,
    travel_view, travel_result_view)

app_name = 'game_tools'
urlpatterns = [
    path('t_types/result', t_types_result_view, name='t_types_result'),
    #url(r'^t_types/result/$', t_types_result_view, name='t_types_result'),
    url(r'^t_types/$', t_types_view, name='t_types'),
    url(r'^jewelry/result/$', jewelry_result_view, name='jewelry_result'),
    url(r'^jewelry/$', jewelry_view, name='jewelry'),
    url(r'^gems/result/$', gems_result_view, name='gems_result'),
    url(r'^gems/$', gems_view, name='gems'),
    url(r'^travel_encounters/$', travel_view, name='travel'),
    url(r'^travel_encounters/result/$', travel_result_view, name='travel_result'),
    url(r'^$', RedirectView.as_view(pattern_name='game_tools:gems', permanent=False), name='index'),
]
