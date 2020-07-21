
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views.generic import View
from django.core.serializers import serialize
import json
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


class SerializedDetailView(View):
    def get(self, request, *arg, **kwargs):
        obj = Update.objects.get(id=1)
        data = serialize("json", [obj, ], fields=('user', 'content'))

        json_data = data
        return HttpResponse(json_data, content_type="application/json")


class SerializedListView(View):
    def get(self, request, *arg, **kwargs):
        qs = Update.objects.all()
        data = serialize("json", qs, fields=('user', 'content'))
        print(data)
        # data = {
        #     "user": object.user.username,
        #     "content": object.content
        # }

        json_data = data
        return HttpResponse(json_data, content_type="application/json")
