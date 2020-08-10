from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination
from rest_framework import generics, status, filters

from . import models as promocode_models
from . import serializers as promocode_serializer


class CreateShopPromocode(generics.CreateAPIView):
    renderer_classes = [JSONRenderer]
    serializer_class = promocode_serializer.CreateShopPromocodeSerializer


class ListShopPromocode(generics.ListAPIView):
    renderer_classes = [JSONRenderer]
    serializer_class = promocode_serializer.ListShopPromocodeSerializer

    def get_queryset(self):
        return promocode_models.ShopPromocode.objects.filter(shop__pk=self.kwargs['pk'])


class UpdateDeleteShopPromocode(generics.RetrieveUpdateDestroyAPIView):
    renderer_classes = [JSONRenderer]
    serializer_class = promocode_serializer.ListShopPromocodeSerializer
    queryset = promocode_models.ShopPromocode.objects.all()


class ListPromocodeOfParticularCategory(generics.ListAPIView):
    renderer_classes = [JSONRenderer]
    serializer_class = promocode_serializer.ListShopPromocodeSerializer

    def get_queryset(self):
        return promocode_models.ShopPromocode.objects.filter(
        	shop__pk=self.kwargs['shop'], category=self.kwargs['category'])