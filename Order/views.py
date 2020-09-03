from django import forms
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination
from rest_framework import generics, status, filters

from . import models as order_models
from . import serializers as order_serializer
from Cart import models as cart_models

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
        else:
            return Response(
                order_serializer_obj.errors,
                status=status.HTTP_400_BAD_REQUEST)

        order_items = self.request.data['items']


###############       Pre Validation of Order Items          ###############
        for order_item in order_items:
            order_item['order'] = order_serializer_obj.data['id']
            if order_dict['order_type'] == 'Grocery':
                order_item_obj = order_serializer.CreateOrderGrocerySerializer(data=order_item)
            elif order_dict['order_type'] == 'Fruit':
                order_item_obj = order_serializer.CreateOrderFruitSerializer(data=order_item)
            elif order_dict['order_type'] == 'Vegetable':
                order_item_obj = order_serializer.CreateOrderVegetableSerializer(data=order_item)
            elif order_dict['order_type'] == 'Food':
                order_item_obj = order_serializer.CreateOrderFoodMealSerializer(data=order_item)

            if order_item_obj.is_valid():
                continue
            else:
                return Response(order_item_obj.errors, status=status.HTTP_400_BAD_REQUEST)
###########################################################################


        for order_item in order_items:
            if order_dict['order_type'] == 'Grocery':
                order_item_obj = order_serializer.CreateOrderGrocerySerializer(data=order_item)
            elif order_dict['order_type'] == 'Fruit':
                order_item_obj = order_serializer.CreateOrderFruitSerializer(data=order_item)
            elif order_dict['order_type'] == 'Vegetable':
                order_item_obj = order_serializer.CreateOrderVegetableSerializer(data=order_item)
            elif order_dict['order_type'] == 'Food':
                order_item_obj = order_serializer.CreateOrderFoodMealSerializer(data=order_item)

            if order_item_obj.is_valid():
                order_item_obj.save()
            else:
                return Response(order_item_obj.errors, status=status.HTTP_400_BAD_REQUEST)

        order = order_models.Order.objects.filter(pk=order_serializer_obj.data['id']).first()
        ongoing_order = order_models.OnGoingOrders(order=order, shop=order.shop)
        ongoing_order.save()

        if order_dict['order_type'] == 'Grocery':
            cart_models.ClientGroceryCart.objects.filter(client__pk=self.request.data['order']['client']).delete()
        elif order_dict['order_type'] == 'Fruit':
            cart_models.ClientFruitCart.objects.filter(client__pk=self.request.data['order']['client']).delete()
        elif order_dict['order_type'] == 'Vegetable':
            cart_models.ClientVegetableCart.objects.filter(client__pk=self.request.data['order']['client']).delete()
        elif order_dict['order_type'] == 'Food':
            cart_models.ClientFoodMealCart.objects.filter(client__pk=self.request.data['order']['client']).delete()

        return Response({'message': 'Orders Created Successfully', 'id': order_serializer_obj.data['id']})


class ListOngoingShopOrder(generics.ListAPIView):
    renderer_classes = [JSONRenderer]
    serializer_class = order_serializer.ListOngoingShopOrderSerializer

    def get_queryset(self):
        ongoing_orders = order_models.OnGoingOrders.objects.filter(order__shop__pk=self.kwargs['pk'])
        return [ongoing_order.order for ongoing_order in ongoing_orders]


class ListShopPastOrder(generics.ListAPIView):
    renderer_classes = [JSONRenderer]
    serializer_class = order_serializer.ListOngoingShopOrderSerializer

    def get_queryset(self):
        return order_models.Order.objects.filter(shop__pk=self.kwargs['pk']).order_by('-created')


class ListSpecificOngoingShopOrder(generics.ListAPIView):
    renderer_classes = [JSONRenderer]
    serializer_class = order_serializer.ListOngoingShopOrderSerializer

    def get_queryset(self):
        ongoing_orders = order_models.OnGoingOrders.objects.filter(pk=self.kwargs['pk'])
        return [ongoing_order.order for ongoing_order in ongoing_orders]


class ListClientOngoingOrder(generics.ListAPIView):
    renderer_classes = [JSONRenderer]
    serializer_class = order_serializer.ListOngoingShopOrderSerializer

    def get_queryset(self):
        ongoing_orders = order_models.OnGoingOrders.objects.filter(order__client__pk=self.kwargs['pk'])
        return [ongoing_order.order for ongoing_order in ongoing_orders]


class ListSpecificShopOrder(generics.ListAPIView):
    renderer_classes = [JSONRenderer]
    serializer_class = order_serializer.ListOngoingShopOrderSerializer

    def get_queryset(self):
        return order_models.Order.objects.filter(pk=self.kwargs['pk'])


class ListClientPastOrder(generics.ListAPIView):
    renderer_classes = [JSONRenderer]
    serializer_class = order_serializer.ListOngoingShopOrderSerializer

    def get_queryset(self):
        return order_models.Order.objects.filter(client__pk=self.kwargs['pk']).order_by('-created')


class UpdateOrder(generics.UpdateAPIView):
    renderer_classes = [JSONRenderer]
    serializer_class = order_serializer.UpdateOrderSerializer
    queryset = order_models.Order.objects.all()


class OrderCompleted(APIView):
    def post(self, request):
        if 'order' not in self.request.data:
            return Response({'message': 'Include Order in Data'}, status=status.HTTP_400_BAD_REQUEST)

        order = order_models.Order.objects.filter(pk=self.request.data['order']).first()
        if not order:
            return Response({'message': 'Invalid Order ID'}, status=status.HTTP_400_BAD_REQUEST)

        obj = order_models.OnGoingOrders.objects.filter(order=order).first()
        if obj:
            obj.delete()
        order.is_delivered = True
        order.save()
        return Response({'message': 'Order Completed Successfully'}, status=status.HTTP_200_OK)
