from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination
from rest_framework import generics, status, filters

from . import models as feedback_models
from . import serializers as feedback_serializer


class CreateShopFeedBack(generics.CreateAPIView):
    renderer_classes = [JSONRenderer]
    serializer_class = feedback_serializer.CreateShopFeedBackSerializer


class ListShopFeedBack(generics.ListAPIView):
    renderer_classes = [JSONRenderer]
    serializer_class = feedback_serializer.ListShopFeedBackSerializer

    def get_queryset(self):
        return feedback_models.ShopFeedBack.objects.filter(shop__pk=self.kwargs['pk'])


class UpdateDeleteFeedBack(generics.RetrieveUpdateDestroyAPIView):
    renderer_classes = [JSONRenderer]
    serializer_class = feedback_serializer.ListShopFeedBackSerializer
    queryset = feedback_models.ShopFeedBack.objects.all()


class ListClientFeedBack(generics.ListAPIView):
    renderer_classes = [JSONRenderer]
    serializer_class = feedback_serializer.ListShopFeedBackSerializer

    def get_queryset(self):
        return feedback_models.ShopFeedBack.objects.filter(client__pk=self.kwargs['pk'])
