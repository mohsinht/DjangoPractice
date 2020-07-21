
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views.generic import View

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
    

class JsonResponseMixin(object):
    def render_to_json_response(self, context, **response_kwargs):
        return JsonResponse(self.get_data(context), **response_kwargs)

    def get_data(self, context):
        return context
