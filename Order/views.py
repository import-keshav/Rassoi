from django import forms
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination
from rest_framework import generics, status, filters

from . import models as order_models
from . import serializers as order_serializer


class CreateOrder(APIView):
    def post(self, request):
        if not 'order' in self.request.data:
            raise forms.ValidationError('Include order in data')
        if not 'items' in self.request.data:
            raise forms.ValidationError('Include items in data')

        order_dict = self.request.data['order']
        order_serializer_obj = order_serializer.CreateOrderSerializer(data=order_dict)
        if order_serializer_obj.is_valid():
            order_serializer_obj.save()
            self.request.data['items']['order'] = order_serializer_obj.data['id']
        else:
            return Response(order_serializer_obj.errors)

        if order_dict['order_type'] == 'Grocery':
            order_item_obj = order_serializer.CreateOrderGrocerySerializer(data=self.request.data['items'])
        elif order_dict['order_type'] == 'Fruit':
            order_item_obj = order_serializer.CreateOrderFruitSerializer(data=self.request.data['items'])
        elif order_dict['order_type'] == 'Vegetable':
            order_item_obj = order_serializer.CreateOrderVegetableSerializer(data=self.request.data['items'])
        elif order_dict['order_type'] == 'Food':
            order_item_obj = order_serializer.CreateOrderFoodMealSerializer(data=self.request.data['items'])

        if order_item_obj.is_valid():
            order_item_obj.save()
        else:
            return Response(order_item_obj.errors)
        return Response({'message': 'Orders Created Successfully', 'id': order_serializer_obj.data['id']})
