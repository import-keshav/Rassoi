from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination
from rest_framework import generics, status, filters


from . import models as driver_models
from . import serializers as driver_serializer
from Shop import models as shop_models


class ListDrivers(generics.ListAPIView):
    renderer_classes = [JSONRenderer]
    serializer_class = driver_serializer.ListDriverSerializer

    def get_queryset(self):
        shop = shop_models.Shop.objects.filter(pk=self.kwargs['pk']).first()
        return driver_models.Driver.objects.filter(shop_assigned=shop)
