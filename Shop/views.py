from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination
from rest_framework import generics, status, filters


from . import models as shop_models
from . import serializers as shop_serializer
from Approval import models as approval_models

class ListGroceries(generics.ListAPIView):
    renderer_classes = [JSONRenderer]
    serializer_class = shop_serializer.ListGroceriesSerializer

    def get_queryset(self):
        shop = shop_models.Shop.objects.filter(pk=self.kwargs['pk']).first()
        return shop_models.Grocery.objects.filter(shop=shop, is_approved=True)


class CreateGrocery(APIView):
    def post(self, request):
        valid_keys = ['shop', 'name']
        for key in valid_keys:
            if key not in self.request.data:
                return Response('Include ' + key + ' in data', status=status.HTTP_400_BAD_REQUEST)
        self.request.data['is_approved'] = False
        serializer_obj = shop_serializer.CreateGrocerySerializer(data=self.request.data)
        if serializer_obj.is_valid():
            serializer_obj.save()
            self.add_obj_in_approval(serializer_obj)
            return Response({'message': 'Grocery created succesfully', 'id':serializer_obj.data['id']}, status=status.HTTP_200_OK)
        return Response(serializer_obj.errors, status=status.HTTP_400_BAD_REQUEST)

    def add_obj_in_approval(self, serializer_obj):
        grocery = shop_models.Grocery.objects.filter(pk=serializer_obj.data['id']).first()
        approval_obj = approval_models.GroceryApproval(grocery=grocery,is_approved=False, action='Create')
        approval_obj.save()


class CreateGroceryInKgQuantityPrice(generics.CreateAPIView):
    renderer_classes = [JSONRenderer]
    serializer_class = shop_serializer.GetGroceryInKgQuantityPriceSerializer


class CreateGroceryInNumOfItemsPrice(generics.CreateAPIView):
    renderer_classes = [JSONRenderer]
    serializer_class = shop_serializer.GetGroceryInNumOfItemsPriceSerializer


class CreateGroceryInLitresPrice(generics.CreateAPIView):
    renderer_classes = [JSONRenderer]
    serializer_class = shop_serializer.GetGroceryInLitresPriceSerializer# class DeleteGrocery(generics.DestroyAPIView)


class ListFruits(generics.ListAPIView):
    renderer_classes = [JSONRenderer]
    serializer_class = shop_serializer.ListFruitsSerializer

    def get_queryset(self):
        shop = shop_models.Shop.objects.filter(pk=self.kwargs['pk']).first()
        return shop_models.Fruit.objects.filter(shop=shop)


class CreateFruit(APIView):
    def post(self, request):
        valid_keys = ['shop', 'name', 'price_per_kg']
        for key in valid_keys:
            if key not in self.request.data:
                return Response('Include ' + key + ' in data', status=status.HTTP_400_BAD_REQUEST)
        self.request.data['is_approved'] = False
        serializer_obj = shop_serializer.CreateFruitsSerializer(data=self.request.data)
        if serializer_obj.is_valid():
            serializer_obj.save()
            self.add_obj_in_approval(serializer_obj)
            return Response({'message': 'Fruit created succesfully', 'id':serializer_obj.data['id']}, status=status.HTTP_200_OK)
        return Response(serializer_obj.errors, status=status.HTTP_400_BAD_REQUEST)

    def add_obj_in_approval(self, serializer_obj):
        fruit = shop_models.Fruit.objects.filter(pk=serializer_obj.data['id']).first()
        approval_obj = approval_models.FruitApproval(fruit=fruit, is_approved=False, action='Create')
        approval_obj.save()


class ListVegetables(generics.ListAPIView):
    renderer_classes = [JSONRenderer]
    serializer_class = shop_serializer.ListVegetableSerializer

    def get_queryset(self):
        shop = shop_models.Shop.objects.filter(pk=self.kwargs['pk']).first()
        return shop_models.Vegetable.objects.filter(shop=shop)


class CreateVegetable(APIView):
    def post(self, request):
        valid_keys = ['shop', 'name', 'price_per_kg']
        for key in valid_keys:
            if key not in self.request.data:
                return Response('Include ' + key + ' in data', status=status.HTTP_400_BAD_REQUEST)
        self.request.data['is_approved'] = False
        serializer_obj = shop_serializer.CreateVegetableSerializer(data=self.request.data)
        if serializer_obj.is_valid():
            serializer_obj.save()
            self.add_obj_in_approval(serializer_obj)
            return Response({'message': 'Vegetable created succesfully', 'id':serializer_obj.data['id']}, status=status.HTTP_200_OK)
        return Response(serializer_obj.errors, status=status.HTTP_400_BAD_REQUEST)

    def add_obj_in_approval(self, serializer_obj):
        vegetable = shop_models.Vegetable.objects.filter(pk=serializer_obj.data['id']).first()
        approval_obj = approval_models.VegetableApproval(vegetable=vegetable, is_approved=False, action='Create')
        approval_obj.save()


class ListSlots(generics.ListAPIView):
    renderer_classes = [JSONRenderer]
    serializer_class = shop_serializer.ListSlotsSerializer

    def get_queryset(self):
        shop = shop_models.Shop.objects.filter(pk=self.kwargs['pk']).first()
        return shop_models.Slots.objects.filter(shop=shop)
