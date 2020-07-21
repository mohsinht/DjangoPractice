from django.conf.urls import url, include

from .views import (
    UpdateModelDetailAPIView,
    UpdateModelListAPIView
)

urlpatterns = [
    # api/updates/ -> List/Create
    url(r'^$', UpdateModelListAPIView.as_view()),
    url(r'^(?P<id>\d+)/$', UpdateModelDetailAPIView.as_view()),
]
