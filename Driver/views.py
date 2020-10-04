from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination
from rest_framework import generics, status, filters


from . import models as driver_models
from . import serializers as driver_serializer
from Shop import models as shop_models
from Order import models as order_models
from Order import serializers as order_serializer


class ListDrivers(generics.ListAPIView):
    renderer_classes = [JSONRenderer]
    serializer_class = driver_serializer.ListDriverSerializer

    def get_queryset(self):
        return driver_models.Driver.objects.filter(shop_assigned__pk=self.kwargs['pk'])


class GetTodaysOrders(generics.ListAPIView):
    renderer_classes = [JSONRenderer]
    serializer_class = order_serializer.ListOngoingShopOrderSerializer

    def get_queryset(self):
        driver = driver_models.Driver.objects.get(pk=self.kwargs['pk'])
        driver_slots = self.get_driver_slots(driver)
        ongoing_orders = order_models.OnGoingOrders.objects.none()
        for slot in driver_slots:
            ongoing_orders|= order_models.OnGoingOrders.objects.filter(shop=driver.shop_assigned, order__slot=slot)
        return [order.order for order in ongoing_orders]

    def get_driver_slots(self, driver):
        driver_slots = driver_models.DriverSlotsAssigned.objects.filter(driver=driver)
        return [slot.slot for slot in driver_slots]


class GetTodaysFoodPackageOrders(generics.ListAPIView):
    renderer_classes = [JSONRenderer]
    serializer_class = order_serializer.GetFoodPackageEachMealOrderSerializer

    def get_queryset(self):
        driver_slots = self.get_driver_slots(self.kwargs['pk'])
        driver = driver_models.Driver.objects.get(pk=self.kwargs['pk'])
        return order_models.FoodPackageEachMealOrder.objects.filter(order__shop=driver.shop_assigned, order__slot=driver_slots)

    def get_driver_slots(self, driver_id):
        slots = shop_models.Slots.objects.none()
        driver_slots = driver_models.DriverSlotsAssigned.objects.filter(driver__pk=driver_id)
        for slot in driver_slots:
            slots |= slot.slot
        return slots


class DeliveredNormalOrder(APIView):
    def post(self, request, order_id):
        order = order_models.Order.objects.filter(pk=order_id).first()
        if not order:
            return Response({
                "message": "No order Exist with this Id"
            }, status=status.HTTP_400_BAD_REQUEST)

        ongoing_order = order_models.OnGoingOrders.objects.filter(order=order).first()
        if not ongoing_order:
            return Response({
                "message": "Order Already Delivered"
            }, status=status.HTTP_400_BAD_REQUEST)

        ongoing_order.delete()
        order.status = "delivered"
        order.is_delivered = True
        order.save()

        return Response({
            "message": "Order Delivered Successfully"
        }, status=status.HTTP_200_OK)


class DeliveredFoodPackageMealOrder(APIView):
    def post(self, request, order_id):
        order = order_models.FoodPackageEachMealOrder.objects.filter(pk=order_id).first()
        if not order:
            return Response({
                "message": "No order Exist with this Id"
            }, status=status.HTTP_400_BAD_REQUEST)

        order.status = "delivered"
        order.is_delivered = True
        order.save()

        return Response({
            "message": "Order Delivered Successfully"
        }, status=status.HTTP_200_OK)

