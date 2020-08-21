from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination
from rest_framework import generics, status, filters

from . import models as grocery_models
from . import serializers as grocery_serializer
from Approval import models as approval_models


class ListGroceries(generics.ListAPIView):
    renderer_classes = [JSONRenderer]
    serializer_class = grocery_serializer.ListGroceriesSerializer

    def get_queryset(self):
        return grocery_models.Grocery.objects.filter(shop__pk=self.kwargs['pk'], is_approved=True)


class ListGroceriesOnClientSide(generics.ListAPIView):
    renderer_classes = [JSONRenderer]
    serializer_class = grocery_serializer.ListGroceriesOnClientSideSerializer

    def get_queryset(self):
        return grocery_models.Grocery.objects.filter(shop__pk=self.kwargs['shop'], is_approved=True)


class ListSpecificGrocery(generics.ListAPIView):
    renderer_classes = [JSONRenderer]
    serializer_class = grocery_serializer.ListGroceriesSerializer

    def get_queryset(self):
        return grocery_models.Grocery.objects.filter(pk=self.kwargs['pk'])


class CreateGrocery(APIView):
    def post(self, request):
        valid_keys = ['shop', 'name']
        for key in valid_keys:
            if key not in self.request.data:
                return Response('Include ' + key + ' in data', status=status.HTTP_400_BAD_REQUEST)
        self.request.data['is_approved'] = False
        serializer_obj = grocery_serializer.CreateGrocerySerializer(data=self.request.data)
        if serializer_obj.is_valid():
            serializer_obj.save()
            self.add_obj_in_approval(serializer_obj)
            return Response({'message': 'Grocery created succesfully', 'id':serializer_obj.data['id']}, status=status.HTTP_200_OK)
        return Response(serializer_obj.errors, status=status.HTTP_400_BAD_REQUEST)

    def add_obj_in_approval(self, serializer_obj):
        grocery = grocery_models.Grocery.objects.filter(pk=serializer_obj.data['id']).first()
        approval_obj = approval_models.GroceryApproval(grocery=grocery, is_approved=False, action='Create')
        approval_obj.save()


class ChangeIsAvailibilityOfGrocery(APIView):
    def post(self, request, pk):
        grocery = grocery_models.Grocery.objects.filter(pk=pk).first()
        if not grocery:
            return Response({'message': 'Invalid Grocery ID'}, status=status.HTTP_400_BAD_REQUEST)
        grocery.is_available = not grocery.is_available
        grocery.save()
        return Response({'message': 'Grocery Availability Changes Succesfully'}, status=status.HTTP_200_OK)


class CreateGroceryPrice(generics.CreateAPIView):
    renderer_classes = [JSONRenderer]
    serializer_class = grocery_serializer.GetGroceryPriceSerializer