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
        return client_models.ClientNotification.objects.filter(client__pk=self.kwargs['pk'])


class CreateShopFeedBack(generics.CreateAPIView):
    renderer_classes = [JSONRenderer]
    serializer_class = client_serializer.CreateShopFeedBackSerializer


class ListShopFeedBack(generics.ListAPIView):
    renderer_classes = [JSONRenderer]
    serializer_class = client_serializer.ListShopFeedBackSerializer

    def get_queryset(self):
        return client_models.ShopFeedBack.objects.filter(shop__pk=self.kwargs['pk'])


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
        return client_models.ClientFruitCart.objects.filter(client__pk=self.kwargs['pk'])


class UpdateDeleteItemInClientFruitCart(generics.RetrieveUpdateDestroyAPIView):
    renderer_classes = [JSONRenderer]
    serializer_class = client_serializer.UpdateDeleteClientFruitCartSerializer
    queryset = client_models.ClientFruitCart.objects.all()


class AddItemInClientVegetableCart(generics.CreateAPIView):
    renderer_classes = [JSONRenderer]
    serializer_class = client_serializer.CreateClientVegetableCartSerializer


class ListItemInClientVegetableCart(generics.ListAPIView):
    renderer_classes = [JSONRenderer]
    serializer_class = client_serializer.ListClientVegetableCartSerializer

    def get_queryset(self):
        return client_models.ClientVegetableCart.objects.filter(client__pk=self.kwargs['pk'])


class UpdateDeleteItemInClientVegetableCart(generics.RetrieveUpdateDestroyAPIView):
    renderer_classes = [JSONRenderer]
    serializer_class = client_serializer.UpdateDeleteClientVegetableCartSerializer
    queryset = client_models.ClientFruitCart.objects.all()


class AddItemInClientGroceryCart(generics.CreateAPIView):
    renderer_classes = [JSONRenderer]
    serializer_class = client_serializer.CreateClientGroceryCartSerializer


class ListItemInClientGroceryCart(generics.ListAPIView):
    renderer_classes = [JSONRenderer]
    serializer_class = client_serializer.ListClientGroceryCartSerializer

    def get_queryset(self):
        return client_models.ClientGroceryCart.objects.filter(client__pk=self.kwargs['pk'])


class UpdateDeleteItemInClientGroceryCart(generics.RetrieveUpdateDestroyAPIView):
    renderer_classes = [JSONRenderer]
    serializer_class = client_serializer.UpdateDeleteClientGroceryCartSerializer
    queryset = client_models.ClientFruitCart.objects.all()