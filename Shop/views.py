from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination
from rest_framework import generics, status, filters


from . import models as shop_models
from . import serializers as shop_serializer

class ListGroceries(generics.ListAPIView):
    renderer_classes = [JSONRenderer]
    serializer_class = shop_serializer.ListGroceriesSerializer

    def get_queryset(self):
        shop = shop_models.Shop.objects.filter(pk=self.kwargs['pk']).first()
        return shop_models.Grocery.objects.filter(shop=shop)


# class DeleteGrocery(generics.DestroyAPIView)
#     renderer_classes = [JSONRenderer]
#     serializer_class = restaurant_serializers.RestaurantPostSerializer
#     queryset = shop_models.Grocery.objects.all()


class ListFruits(generics.ListAPIView):
    renderer_classes = [JSONRenderer]
    serializer_class = shop_serializer.ListFruitsSerializer

    def get_queryset(self):
        shop = shop_models.Shop.objects.filter(pk=self.kwargs['pk']).first()
        return shop_models.Fruit.objects.filter(shop=shop)


class ListVegetables(generics.ListAPIView):
    renderer_classes = [JSONRenderer]
    serializer_class = shop_serializer.ListVegetableSerializer

    def get_queryset(self):
        shop = shop_models.Shop.objects.filter(pk=self.kwargs['pk']).first()
        return shop_models.Vegetable.objects.filter(shop=shop)


class ListSlots(generics.ListAPIView):
    renderer_classes = [JSONRenderer]
    serializer_class = shop_serializer.ListSlotsSerializer

    def get_queryset(self):
        shop = shop_models.Shop.objects.filter(pk=self.kwargs['pk']).first()
        return shop_models.Slots.objects.filter(shop=shop)
