from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    # figure out what the fuck this regex means!
    url(r'^(?P<room_name>[^/]+)/$', views.room, name='room'),
]