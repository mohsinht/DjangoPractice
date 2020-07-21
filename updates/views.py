
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views.generic import View

from cfeapi.mixins import JsonResponseMixin
from .models import Update


def json_example_view(request):
    data = {
        "count": 100,
        "content": "Some New Content"
    }
    return JsonResponse(data)


class JsonCBV(View):
    def get(self, request, *args, **kwargs):
        data = {
            "count": 100,
            "content": "Some New Content"
        }
        return JsonResponse(data)


class JsonCBV2(JsonResponseMixin, View):
    def get(self, request, *arg, **kwargs):
        data = {
            "count": 100,
            "content": "Some New Content"
        }
        return self.render_to_json_response(data)
