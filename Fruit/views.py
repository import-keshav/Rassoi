from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination
from rest_framework import generics, status, filters


from . import models as fruit_models
from . import serializers as fruit_serializer
from Approval import models as approval_models


class ListFruits(generics.ListAPIView):
    renderer_classes = [JSONRenderer]
    serializer_class = fruit_serializer.ListFruitsSerializer

    def get_queryset(self):
        return fruit_models.Fruit.objects.filter(shop__pk=self.kwargs['pk'], is_approved=True)


class ListSpecificFruit(generics.ListAPIView):
    renderer_classes = [JSONRenderer]
    serializer_class = fruit_serializer.ListFruitsSerializer

    def get_queryset(self):
        return fruit_models.Fruit.objects.filter(pk=self.kwargs['pk'])


class CreateFruit(APIView):
    def post(self, request):
        valid_keys = ['shop', 'name']
        for key in valid_keys:
            if key not in self.request.data:
                return Response('Include ' + key + ' in data', status=status.HTTP_400_BAD_REQUEST)
        serializer_obj = fruit_serializer.CreateFruitsSerializer(data=self.request.data)
        if serializer_obj.is_valid():
            serializer_obj.save()
            self.add_obj_in_approval(serializer_obj)
            return Response({'message': 'Fruit created succesfully', 'id':serializer_obj.data['id']}, status=status.HTTP_200_OK)
        return Response(serializer_obj.errors, status=status.HTTP_400_BAD_REQUEST)

    def add_obj_in_approval(self, serializer_obj):
        fruit = fruit_models.Fruit.objects.filter(pk=serializer_obj.data['id']).first()
        fruit.is_approved = False
        fruit.save()
        approval_obj = approval_models.FruitApproval(fruit=fruit, is_approved=False, action='Create')
        approval_obj.save()


class ChangeIsAvailibilityOfFruit(APIView):
    def post(self, request, pk):
        fruit = fruit_models.Fruit.objects.filter(pk=pk).first()
        if not fruit:
            return Response({'message': 'Invalid Fruit ID'}, status=status.HTTP_400_BAD_REQUEST)
        fruit.is_available = not fruit.is_available 
        fruit.save()
        return Response({'message': 'Fruit Availability Changes Succesfully'}, status=status.HTTP_200_OK)


class CreateFruitPrice(generics.CreateAPIView):
    renderer_classes = [JSONRenderer]
    serializer_class = fruit_serializer.GetFruitPriceSerializer