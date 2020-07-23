from django.conf.urls import url
from django.urls import path, re_path

from .views import (StatusAPIView,
                    StatusDetailAPIView, )

'''
Endpoints for the Status API.

    List -> /api/status/
    Create -> /api/status/create/
    Detail -> /api/status/1/
    Update -> /api/status/1/update/
    Delete -> /api/status/1/delete/

But better way is to create a single API for all of these operations:

    CRUD List -> /api/status/
    CRUD Detail -> /api/status/1/ 

And even better:

    CRUD on List/Detail -> /api/status/

'''

urlpatterns = [
    url(r'^$', StatusAPIView.as_view()),
    # url(r'^create/$', StatusCreateAPIView.as_view()),
    url(r'^(?P<id>\d+)/$', StatusDetailAPIView.as_view()),
    # re_path(r'^articles/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/$', views.month_archive),
    # url(r'^(?P<pk>\d+)/update/$', StatusUpdateAPIView.as_view()),
    # #url(r'^(?P<pk>.*)/update/$', StatusUpdateAPIView.as_view()),
    # url(r'^(?P<pk>\d+)/delete/$', StatusDeleteAPIView.as_view()),
]
