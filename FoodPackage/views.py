from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination
from rest_framework import generics, status, filters

from . import models as food_package_models
from . import serializers as food_package_serializer


class ListClientFoodPackage(generics.ListAPIView):
    renderer_classes = [JSONRenderer]
    serializer_class = food_package_serializer.ListFoodPackageSerializer

    def get_queryset(self):
        return food_package_models.FoodPackage.objects.filter(client__pk=self.kwargs['pk'])


class ListShopFoodPackage(generics.ListAPIView):
    renderer_classes = [JSONRenderer]
    serializer_class = food_package_serializer.ListFoodPackageSerializer

    def get_queryset(self):
        return food_package_models.FoodPackage.objects.filter(shop__pk=self.kwargs['pk'])


class UpdateDeleteFoodPackage(generics.RetrieveUpdateDestroyAPIView):
    renderer_classes = [JSONRenderer]
    serializer_class = food_package_serializer.UpdateDeleteFoodPackageSerializer
    queryset = food_package_models.FoodPackage.objects.all()


class UpdateDeleteFoodPackageMeal(generics.RetrieveUpdateDestroyAPIView):
    renderer_classes = [JSONRenderer]
    serializer_class = food_package_serializer.UpdateDeleteFoodPackageMealSerializer
    queryset = food_package_models.FoodPackageMeal.objects.all()


class CreateFoodPackage(generics.CreateAPIView):
    renderer_classes = [JSONRenderer]
    serializer_class = food_package_serializer.CreateFoodPackageSerializer


class CreateFoodPackageMeal(generics.CreateAPIView):
    renderer_classes = [JSONRenderer]
    serializer_class = food_package_serializer.CreateFoodPackageMealSerializer