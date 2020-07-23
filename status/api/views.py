from rest_framework import generics, mixins
from rest_framework.views import APIView
from rest_framework.response import Response

from status.models import Status as StatusModel
from .serializers import StatusSerializer


class StatusListSearchAPIView(APIView):
    permission_classes = []
    authentication_classes = []

    def get(self, request, format=None):
        qs = StatusModel.objects.all()
        serializer = StatusSerializer(qs, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        qs = StatusModel.objects.all()
        serializer = StatusSerializer(qs, many=True)
        return Response(serializer.data)


# CreateModelMixin is for creating data using POST.
# UpdateModelMixin is to update data using PUT.
# DestroyModelMixin is to delete data using DELETE.

class StatusAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    permission_classes = []
    authentication_classes = []
    serializer_class = StatusSerializer

    def get_queryset(self):
        qs = StatusModel.objects.all()
        query = self.request.GET.get('q')
        if query is not None:
            qs = qs.filter(content__icontains=query)
        return qs

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


# NOT NEEDED AS IT IS NOW IMPLEMENTED IN StatusAPIView.post()
# class StatusCreateAPIView(generics.CreateAPIView):
#     permission_classes = []
#     authentication_classes = []
#     queryset = StatusModel.objects.all()
#     serializer_class = StatusSerializer

#     # def perform_create(self, serialzer):
#     #     serializer.save(user=self.request.user)


class StatusDetailAPIView(mixins.DestroyModelMixin, mixins.UpdateModelMixin, generics.RetrieveAPIView):
    permission_classes = []
    authentication_classes = []
    queryset = StatusModel.objects.all()
    serializer_class = StatusSerializer
    lookup_field = 'id'

    def post(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    # def get_object(self, *args, **kwargs):
    #     kwargs = self.kwargs
    #     # the following is same as the one entered in URL 'id'
    #     kw_id = kwargs.get('id')
    #     return StatusModel.objects.get(id=kw_id)


# NOT NEEDED AS IT IS IMPLEMETED ABOVE IN StatusDetailAPIView.post()
# class StatusUpdateAPIView(generics.UpdateAPIView):
#     permission_classes = []
#     authentication_classes = []
#     queryset = StatusModel.objects.all()
#     serializer_class = StatusSerializer


# class StatusDeleteAPIView(generics.DestroyAPIView):
#     permission_classes = []
#     authentication_classes = []
#     queryset = StatusModel.objects.all()
#     serializer_class = StatusSerializer
