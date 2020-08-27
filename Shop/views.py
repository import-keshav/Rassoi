import hashlib, binascii, os, random
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination
from rest_framework import generics, status, filters


from . import models as shop_models
from . import serializers as shop_serializer
from Approval import models as approval_models


class ListSlots(generics.ListAPIView):
    renderer_classes = [JSONRenderer]
    serializer_class = shop_serializer.ListSlotsSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category']

    def get_queryset(self):
        shop = shop_models.Shop.objects.filter(pk=self.kwargs['pk']).first()
        return shop_models.Slots.objects.filter(shop=shop)


class CreateSlot(generics.CreateAPIView):
    renderer_classes = [JSONRenderer]
    serializer_class = shop_serializer.CreateSlotSerializer


class UpdateDeleteSlot(generics.RetrieveUpdateDestroyAPIView):
    renderer_classes = [JSONRenderer]
    serializer_class = shop_serializer.UpdateDeleteSlotsSerializer
    queryset = shop_models.Slots.objects.all()


class ListSpecificShop(generics.ListAPIView):
    renderer_classes = [JSONRenderer]
    serializer_class = shop_serializer.ListShop

    def get_queryset(self):
        return shop_models.Shop.objects.filter(pk=self.kwargs['pk'])


class ShopLogin(APIView):
    def post(self, request):
        try:
            shop = shop_models.Shop.objects.filter(
                unique_id=self.request.data['unique_id']).first()
            if not shop:
                return Response({"message": "Invalid Shop unique Id",}, status=status.HTTP_400_BAD_REQUEST)
            if self.verify_password(shop.password, self.request.data['password']):
                shop_obj = shop_serializer.ListShop(shop)
                return Response({'message': 'Login Succesfully', "shop": shop_obj.data}, status=status.HTTP_200_OK)
            return Response({'message': 'Invalid password'}, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({"message": "unique_id is missing"}, status=status.HTTP_400_BAD_REQUEST)

    def verify_password(self, stored_password, provided_password):
        """Verify a stored password against one provided by user"""
        salt = stored_password[:64]
        stored_password = stored_password[64:]
        pwdhash = hashlib.pbkdf2_hmac('sha512', 
                                      provided_password.encode('utf-8'), 
                                      salt.encode('ascii'), 
                                      100000)
        pwdhash = binascii.hexlify(pwdhash).decode('ascii')
        return pwdhash == stored_password
