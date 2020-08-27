from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination
from rest_framework import generics, status, filters
from django_filters.rest_framework import DjangoFilterBackend

from . import models as food_models
from . import serializers as food_serializer
from Approval import models as approval_models


class ListFoodMeal(generics.ListAPIView):
    renderer_classes = [JSONRenderer]
    serializer_class = food_serializer.ListFoodMealSerializer

    def get_queryset(self):
        return food_models.FoodMeal.objects.filter(shop__pk=self.kwargs['pk'], is_approved=True)


class ListFoodMealOnClientSide(generics.ListAPIView):
    renderer_classes = [JSONRenderer]
    serializer_class = food_serializer.ListFoodDishesOnClientSideSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['food_type']

    def get_queryset(self):
        return food_models.FoodMeal.objects.filter(shop__pk=self.kwargs['shop'], is_approved=True)


class CreateFoodMeal(APIView):
    def post(self, request):
        valid_keys = ['shop', 'name', 'food_type', 'day']
        for key in valid_keys:
            if key not in self.request.data:
                return Response('Include ' + key + ' in data', status=status.HTTP_400_BAD_REQUEST)
        serializer_obj = food_serializer.CreateFoodMealSerializer(data=self.request.data)
        if serializer_obj.is_valid():
            serializer_obj.save()
            self.add_obj_in_approval(serializer_obj)
            return Response({'message': 'Food Meal created succesfully', 'id':serializer_obj.data['id']}, status=status.HTTP_200_OK)
        return Response(serializer_obj.errors, status=status.HTTP_400_BAD_REQUEST)

    def add_obj_in_approval(self, serializer_obj):
        meal = food_models.FoodMeal.objects.filter(pk=serializer_obj.data['id']).first()
        meal.is_approved = False
        meal.save()
        approval_obj = approval_models.FoodMealApproval(meal=meal, is_approved=False, action='Create')
        approval_obj.save()


class ChangeIsAvailibilityOfFoodMeal(APIView):
    def post(self, request, pk):
        food_meal = food_models.FoodMeal.objects.filter(pk=pk).first()
        if not food_meal:
            return Response({'message': 'Invalid FoodMeal ID'}, status=status.HTTP_400_BAD_REQUEST)
        food_meal.is_available = not food_meal.is_available
        food_meal.save()
        return Response({'message': 'FoodMeal Availability Changes Succesfully'}, status=status.HTTP_200_OK)


class CreateFoodDish(generics.CreateAPIView):
    renderer_classes = [JSONRenderer]
    serializer_class = food_serializer.CreateFoodDishesSerializer
