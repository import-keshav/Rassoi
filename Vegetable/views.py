from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination
from rest_framework import generics, status, filters


from . import models as vegetable_models
from . import serializers as vegetable_serializer
from Approval import models as approval_models


class ListVegetables(generics.ListAPIView):
    renderer_classes = [JSONRenderer]
    serializer_class = vegetable_serializer.ListVegetableSerializer

    def get_queryset(self):
        return vegetable_models.Vegetable.objects.filter(shop__pk=self.kwargs['pk'], is_approved=True)


class ListVegetablesOnClientSide(generics.ListAPIView):
    renderer_classes = [JSONRenderer]
    serializer_class = vegetable_serializer.ListVegetableOnClientSideSerializer

    def get_queryset(self):
        return vegetable_models.Vegetable.objects.filter(shop__pk=self.kwargs['shop'], is_approved=True)


class ListSpecificVegetable(generics.ListAPIView):
    renderer_classes = [JSONRenderer]
    serializer_class = vegetable_serializer.ListVegetableSerializer

    def get_queryset(self):
        return vegetable_models.Vegetable.objects.filter(pk=self.kwargs['pk'])


class CreateVegetable(APIView):
    def post(self, request):
        valid_keys = ['shop', 'name']
        for key in valid_keys:
            if key not in self.request.data:
                return Response('Include ' + key + ' in data', status=status.HTTP_400_BAD_REQUEST)
        serializer_obj = vegetable_serializer.CreateVegetableSerializer(data=self.request.data)
        if serializer_obj.is_valid():
            serializer_obj.save()
            self.add_obj_in_approval(serializer_obj)
            return Response({'message': 'Vegetable created succesfully', 'id':serializer_obj.data['id']}, status=status.HTTP_200_OK)
        return Response(serializer_obj.errors, status=status.HTTP_400_BAD_REQUEST)

    def add_obj_in_approval(self, serializer_obj):
        vegetable = vegetable_models.Vegetable.objects.filter(pk=serializer_obj.data['id']).first()
        vegetable.is_approved = False
        vegetable.save()
        approval_obj = approval_models.VegetableApproval(vegetable=vegetable, is_approved=False, action='Create')
        approval_obj.save()


class ChangeIsAvailibilityOfVegetable(APIView):
    def post(self, request, pk):
        vegetable = vegetable_models.Vegetable.objects.filter(pk=pk,).first()
        if not vegetable:
            return Response({'message': 'Invalid Vegetable ID'}, status=status.HTTP_400_BAD_REQUEST)
        vegetable.is_available = not vegetable.is_available
        vegetable.save()
        return Response({'message': 'Vegetable Availability Changes Succesfully'}, status=status.HTTP_200_OK)


class CreateVegetablePrice(generics.CreateAPIView):
    renderer_classes = [JSONRenderer]
    serializer_class = vegetable_serializer.GetVegetablePriceSerializer