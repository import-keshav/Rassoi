from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination
from rest_framework import generics, status, filters


from . import models as client_models
from . import serializers as client_serializer
from Shop import models as shop_models

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


class CreateShopFeedBack(generics.CreateAPIView):
    renderer_classes = [JSONRenderer]
    serializer_class = client_serializer.CreateShopFeedBackSerializer


class ListShopFeedBack(generics.ListAPIView):
    renderer_classes = [JSONRenderer]
    serializer_class = client_serializer.ListShopFeedBackSerializer

    def get_queryset(self):
        shop = shop_models.Shop.objects.filter(pk=self.kwargs['pk']).first()
        return client_models.ShopFeedBack.objects.filter(shop=shop)


class UpdateDeleteFeedBack(generics.RetrieveUpdateDestroyAPIView):
    renderer_classes = [JSONRenderer]
    serializer_class = client_serializer.ListShopFeedBackSerializer
    queryset = client_models.ShopFeedBack.objects.all()


class AddItemInClientFruitCart(generics.CreateAPIView):
    renderer_classes = [JSONRenderer]
    serializer_class = client_serializer.CreateClientFruitCartSerializer


class ListItemInClientFruitCart(generics.ListAPIView):
    renderer_classes = [JSONRenderer]
    serializer_class = client_serializer.ListClientFruitCartSerializer

    def get_queryset(self):
        client = client_models.Client.objects.filter(pk=self.kwargs['pk']).first()
        return client_models.ClientFruitCart.objects.filter(client=client)


class UpdateDeleteItemInClientFruitCart(generics.RetrieveUpdateDestroyAPIView):
    renderer_classes = [JSONRenderer]
    serializer_class = client_serializer.UpdateDeleteClientFruitCartSerializer
    queryset = client_models.ClientFruitCart.objects.all()