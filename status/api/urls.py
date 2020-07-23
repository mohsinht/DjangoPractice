from django.conf.urls import url

from .views import StatusAPIView

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
    # url(r'^(?<id>.*)/$', StatusDetailAPIView.as_view()),
    # url(r'^(?<id>.*)/update/$', StatusUpdateAPIView.as_view()),
    # url(r'^(?<id>.*)/delete/$', StatusDeleteAPIView.as_view()),
]
