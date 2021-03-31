from django.urls import path

from . import views


app_name = 'wedding_app'
urlpatterns = [
    path('', views.index, name='index'),
    path('validatecode', views.get_events, name='validatecode'),
    path('write_rsvp_data', views.write_rsvp_data, name='write_rsvp_data')
]