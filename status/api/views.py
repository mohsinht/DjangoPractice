from rest_framework import generics
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


class StatusAPIView(generics.ListAPIView):
    permission_classes = []
    authentication_classes = []
    serializer_class = StatusSerializer

    def get_queryset(self):
        qs = StatusModel.objects.all()
        query = self.request.GET.get('q')
        if query is not None:
            qs = qs.filter(content__icontains=query)
        return qs


class StatusCreateAPIView(generics.CreateAPIView):
    permission_classes = []
    authentication_classes = []
    queryset = StatusModel.objects.all()
    serializer_class = StatusSerializer

    # def perform_create(self, serialzer):
    #     serializer.save(user=self.request.user)


class StatusDetailAPIView(generics.RetrieveAPIView):
    permission_classes = []
    authentication_classes = []
    queryset = StatusModel.objects.all()
    serializer_class = StatusSerializer
    lookup_field = 'id'

    # def get_object(self, *args, **kwargs):
    #     kwargs = self.kwargs
    #     # the following is same as the one entered in URL 'id'
    #     kw_id = kwargs.get('id')
    #     return StatusModel.objects.get(id=kw_id)


class StatusUpdateAPIView(generics.UpdateAPIView):
    permission_classes = []
    authentication_classes = []
    queryset = StatusModel.objects.all()
    serializer_class = StatusSerializer


class StatusDeleteAPIView(generics.DestroyAPIView):
    permission_classes = []
    authentication_classes = []
    queryset = StatusModel.objects.all()
    serializer_class = StatusSerializer
