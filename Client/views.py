from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination
from rest_framework import generics, status, filters


from . import models as client_models
from . import serializers as client_serializer

class GetClientInfo(generics.ListAPIView):
    renderer_classes = [JSONRenderer]
    serializer_class = client_serializer.GetClientInfoSerializer
    def get_queryset(self):
        return client_models.Client.objects.filter(pk=self.kwargs['pk'])


class ListClientNotification(generics.ListAPIView):
    renderer_classes = [JSONRenderer]
    serializer_class = client_serializer.GetClientNotificationSerializer
    def get_queryset(self):
        client = client_models.Client.objects.filter(pk=self.kwargs['pk']).first()
        return client_models.ClientNotification.objects.filter(client=client)
