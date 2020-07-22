from django.views.generic import View
from django.http import HttpResponse
from updates.models import Update as UpdateModel


class UpdateModelDetailAPIView(View):
    # Retrieve:
    def get(self, request, id, *args, **kwargs):
        try:
            obj = UpdateModel.objects.get(id=id)
            json_data = obj.serialize()
        except:
            json_data = {"no_update": True}
        return HttpResponse(json_data, content_type="application/json")

    # Create:
    def post(self, request, *args, **kwargs):
        json_data = {}
        return HttpResponse(json_data, content_type="application/json")  # json

    # Update:
    def put(self, request, *args, **kwargs):
        json_data = {}
        return HttpResponse(json_data, content_type="application/json")  # json

    # Remove:
    def delete(self, request, *args, **kwargs):
        json_data = {}
        return HttpResponse(json_data, content_type="application/json")  # json


class UpdateModelListAPIView(View):
    # Retrieve:
    def get(self, request, *args, **kwargs):
        qs = UpdateModel.objects.all()
        json_data = qs.serialize()
        return HttpResponse(json_data, content_type="application/json")  # json

    # Create:
    def post(self, request, *args, **kwargs):
        json_data = {}
        return HttpResponse(json_data, content_type="application/json")  # json
