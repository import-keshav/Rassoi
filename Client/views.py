from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination
from rest_framework import generics, status, filters


from . import models as client_models
from . import serializers as client_serializer
from Shop import models as shop_models

class GetClientInfo(generics.ListAPIView):
    renderer_classes = [JSONRenderer]
    serializer_class = client_serializer.GetClientInfoSerializer
    def get_queryset(self):
        return client_models.Client.objects.filter(pk=self.kwargs['pk'])


class ListClientNotification(generics.ListAPIView):
    renderer_classes = [JSONRenderer]
    serializer_class = client_serializer.GetClientNotificationSerializer
    def get_queryset(self):
        return client_models.ClientNotification.objects.filter(client__pk=self.kwargs['pk'])


class CreateShopFeedBack(generics.CreateAPIView):
    renderer_classes = [JSONRenderer]
    serializer_class = client_serializer.CreateShopFeedBackSerializer


class ListShopFeedBack(generics.ListAPIView):
    renderer_classes = [JSONRenderer]
    serializer_class = client_serializer.ListShopFeedBackSerializer

    def get_queryset(self):
        return client_models.ShopFeedBack.objects.filter(shop__pk=self.kwargs['pk'])


class UpdateDeleteFeedBack(generics.RetrieveUpdateDestroyAPIView):
    renderer_classes = [JSONRenderer]
    serializer_class = client_serializer.ListShopFeedBackSerializer
    queryset = client_models.ShopFeedBack.objects.all()


class AddItemInClientFruitCart(generics.CreateAPIView):
    renderer_classes = [JSONRenderer]
    serializer_class = client_serializer.CreateClientFruitCartSerializer


class ListItemInClientFruitCart(generics.ListAPIView):
    renderer_classes = [JSONRenderer]
    serializer_class = client_serializer.ListClientFruitCartSerializer

    def get_queryset(self):
        return client_models.ClientFruitCart.objects.filter(client__pk=self.kwargs['pk'])


class UpdateDeleteItemInClientFruitCart(generics.RetrieveUpdateDestroyAPIView):
    renderer_classes = [JSONRenderer]
    serializer_class = client_serializer.UpdateDeleteClientFruitCartSerializer
    queryset = client_models.ClientFruitCart.objects.all()


class GetPriceOfFruitCartItem(APIView):
    def get(self, request, pk):
        cart_item =  client_models.ClientFruitCart.objects.filter(pk=pk).first()
        if cart_item.fruit.price_per_dozen:
            price = cart_item.fruit.price_per_dozen * cart_item.num_of_items
        else:
            price = cart_item.fruit.price_per_kg * cart_item.num_of_items
        cart_item.price = price
        cart_item.save()
        return Response({'price': price}, status=status.HTTP_200_OK)


class GetClientFruitCartTotalPrice(APIView):
    def get(self, request, pk):
        cart_items =  client_models.ClientFruitCart.objects.filter(client__pk=pk)
        total_price = 0
        for cart_item in cart_items:
            if cart_item.fruit.price_per_dozen:
                price = cart_item.fruit.price_per_dozen * cart_item.num_of_items
            else:
                price = cart_item.fruit.price_per_kg * cart_item.num_of_items
            total_price +=price        
            cart_item.price = price
            cart_item.save()
        return Response({'total_price': total_price}, status=status.HTTP_200_OK)


class AddItemInClientVegetableCart(generics.CreateAPIView):
    renderer_classes = [JSONRenderer]
    serializer_class = client_serializer.CreateClientVegetableCartSerializer


class ListItemInClientVegetableCart(generics.ListAPIView):
    renderer_classes = [JSONRenderer]
    serializer_class = client_serializer.ListClientVegetableCartSerializer

    def get_queryset(self):
        return client_models.ClientVegetableCart.objects.filter(client__pk=self.kwargs['pk'])


class UpdateDeleteItemInClientVegetableCart(generics.RetrieveUpdateDestroyAPIView):
    renderer_classes = [JSONRenderer]
    serializer_class = client_serializer.UpdateDeleteClientVegetableCartSerializer
    queryset = client_models.ClientFruitCart.objects.all()


class GetPriceOfVegetableCartItem(APIView):
    def get(self, request, pk):
        cart_item =  client_models.ClientVegetableCart.objects.filter(pk=pk).first()
        price = cart_item.vegetable.price_per_kg * cart_item.num_of_items
        cart_item.price = price
        cart_item.save()
        return Response({'price': price}, status=status.HTTP_200_OK)


class GetClientVegetableCartTotalPrice(APIView):
    def get(self, request, pk):
        cart_items =  client_models.ClientVegetableCart.objects.filter(client__pk=pk)
        total_price = 0
        for cart_item in cart_items:
            price = cart_item.vegetable.price_per_kg * cart_item.num_of_items
            total_price +=price        
            cart_item.price = price
            cart_item.save()
        return Response({'total_price': total_price}, status=status.HTTP_200_OK)


class AddItemInClientGroceryCart(generics.CreateAPIView):
    renderer_classes = [JSONRenderer]
    serializer_class = client_serializer.CreateClientGroceryCartSerializer


class ListItemInClientGroceryCart(generics.ListAPIView):
    renderer_classes = [JSONRenderer]
    serializer_class = client_serializer.ListClientGroceryCartSerializer

    def get_queryset(self):
        return client_models.ClientGroceryCart.objects.filter(client__pk=self.kwargs['pk'])


class UpdateDeleteItemInClientGroceryCart(generics.RetrieveUpdateDestroyAPIView):
    renderer_classes = [JSONRenderer]
    serializer_class = client_serializer.UpdateDeleteClientGroceryCartSerializer
    queryset = client_models.ClientFruitCart.objects.all()


class GetPriceOfGroceryCartItem(APIView):
    def get(self, request, pk):
        cart_item =  client_models.ClientGroceryCart.objects.filter(pk=pk).first()
        price = cart_item.grocery_price.price * cart_item.num_of_items
        cart_item.price = price
        cart_item.save()
        return Response({'price': price}, status=status.HTTP_200_OK)


class GetClientGroceryCartTotalPrice(APIView):
    def get(self, request, pk):
        cart_items =  client_models.ClientGroceryCart.objects.filter(client__pk=pk)
        total_price = 0
        for cart_item in cart_items:
            price = cart_item.grocery_price.price * cart_item.num_of_items
            total_price +=price        
            cart_item.price = price
            cart_item.save()
        return Response({'total_price': total_price}, status=status.HTTP_200_OK)


class AddItemInClientFoodMealCart(generics.CreateAPIView):
    renderer_classes = [JSONRenderer]
    serializer_class = client_serializer.CreateClientFoodMealCartSerializer


class ListItemInClientClientFoodMealCartCart(generics.ListAPIView):
    renderer_classes = [JSONRenderer]
    serializer_class = client_serializer.ListClientFoodMealCartSerializer

    def get_queryset(self):
        return client_models.ClientFoodMealCart.objects.filter(client__pk=self.kwargs['pk'])


class UpdateDeleteItemInClientFoodMealCart(generics.RetrieveUpdateDestroyAPIView):
    renderer_classes = [JSONRenderer]
    serializer_class = client_serializer.UpdateDeleteClientFoodMealCartSerializer
    queryset = client_models.ClientFoodMealCart.objects.all()


class GetPriceOfFoodMealCartItem(APIView):
    def get(self, request, pk):
        cart_item =  client_models.ClientFoodMealCart.objects.filter(pk=pk).first()
        price = cart_item.food_meal.price * cart_item.num_of_items
        cart_item.price = price
        cart_item.save()
        return Response({'price': price}, status=status.HTTP_200_OK)


class GetClientFoodMealCartTotalPrice(APIView):
    def get(self, request, pk):
        cart_items =  client_models.ClientFoodMealCart.objects.filter(client__pk=pk)
        total_price = 0
        for cart_item in cart_items:
            price = cart_item.food_meal.price * cart_item.num_of_items
            total_price +=price        
            cart_item.price = price
            cart_item.save()
        return Response({'total_price': total_price}, status=status.HTTP_200_OK)
