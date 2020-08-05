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

class ListGroceries(generics.ListAPIView):
    renderer_classes = [JSONRenderer]
    serializer_class = shop_serializer.ListGroceriesSerializer

    def get_queryset(self):
        shop = shop_models.Shop.objects.filter(pk=self.kwargs['pk']).first()
        return shop_models.Grocery.objects.filter(shop=shop, is_approved=True)

class ListSpecificGrocery(generics.ListAPIView):
    renderer_classes = [JSONRenderer]
    serializer_class = shop_serializer.ListGroceriesSerializer

    def get_queryset(self):
        return shop_models.Grocery.objects.filter(pk=self.kwargs['pk'])


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


class ChangeIsAvailibilityOfGrocery(APIView):
    def post(self, request):
        valid_keys = ['grocery', 'is_available']
        for key in valid_keys:
            if key not in self.request.data:
                return Response('Include ' + key + ' in data', status=status.HTTP_400_BAD_REQUEST)

        grocery = shop_models.Grocery.objects.filter(pk=self.request.data['grocery'],).first()
        if not grocery:
            return Response({'message': 'Invalid Grocery ID'}, status=status.HTTP_400_BAD_REQUEST)
        grocery.is_available = self.request.data['is_available']
        grocery.save()
        return Response({'message': 'Grocery Availability Changes Succesfully'}, status=status.HTTP_400_BAD_REQUEST)


class CreateGroceryPrice(generics.CreateAPIView):
    renderer_classes = [JSONRenderer]
    serializer_class = shop_serializer.GetGroceryPriceSerializer


class ListFruits(generics.ListAPIView):
    renderer_classes = [JSONRenderer]
    serializer_class = shop_serializer.ListFruitsSerializer

    def get_queryset(self):
        shop = shop_models.Shop.objects.filter(pk=self.kwargs['pk']).first()
        return shop_models.Fruit.objects.filter(shop=shop, is_approved=True)


class ListSpecificFruit(generics.ListAPIView):
    renderer_classes = [JSONRenderer]
    serializer_class = shop_serializer.ListFruitsSerializer

    def get_queryset(self):
        return shop_models.Fruit.objects.filter(pk=self.kwargs['pk'])


class CreateFruit(APIView):
    def post(self, request):
        valid_keys = ['shop', 'name']
        for key in valid_keys:
            if key not in self.request.data:
                return Response('Include ' + key + ' in data', status=status.HTTP_400_BAD_REQUEST)
        serializer_obj = shop_serializer.CreateFruitsSerializer(data=self.request.data)
        if serializer_obj.is_valid():
            serializer_obj.save()
            self.add_obj_in_approval(serializer_obj)
            return Response({'message': 'Fruit created succesfully', 'id':serializer_obj.data['id']}, status=status.HTTP_200_OK)
        return Response(serializer_obj.errors, status=status.HTTP_400_BAD_REQUEST)

    def add_obj_in_approval(self, serializer_obj):
        fruit = shop_models.Fruit.objects.filter(pk=serializer_obj.data['id']).first()
        fruit.is_approved = False
        fruit.save()
        approval_obj = approval_models.FruitApproval(fruit=fruit, is_approved=False, action='Create')
        approval_obj.save()


class ChangeIsAvailibilityOfFruit(APIView):
    def post(self, request):
        valid_keys = ['fruit', 'is_available']
        for key in valid_keys:
            if key not in self.request.data:
                return Response('Include ' + key + ' in data', status=status.HTTP_400_BAD_REQUEST)

        fruit = shop_models.Fruit.objects.filter(pk=self.request.data['fruit'],).first()
        if not fruit:
            return Response({'message': 'Invalid Fruit ID'}, status=status.HTTP_400_BAD_REQUEST)
        fruit.is_available = self.request.data['is_available']
        fruit.save()
        return Response({'message': 'Fruit Availability Changes Succesfully'}, status=status.HTTP_400_BAD_REQUEST)


class ListVegetables(generics.ListAPIView):
    renderer_classes = [JSONRenderer]
    serializer_class = shop_serializer.ListVegetableSerializer

    def get_queryset(self):
        shop = shop_models.Shop.objects.filter(pk=self.kwargs['pk']).first()
        return shop_models.Vegetable.objects.filter(shop=shop, is_approved=True)


class ListSpecificVegetable(generics.ListAPIView):
    renderer_classes = [JSONRenderer]
    serializer_class = shop_serializer.ListVegetableSerializer

    def get_queryset(self):
        return shop_models.Vegetable.objects.filter(pk=self.kwargs['pk'])


class CreateVegetable(APIView):
    def post(self, request):
        valid_keys = ['shop', 'name']
        for key in valid_keys:
            if key not in self.request.data:
                return Response('Include ' + key + ' in data', status=status.HTTP_400_BAD_REQUEST)
        serializer_obj = shop_serializer.CreateVegetableSerializer(data=self.request.data)
        if serializer_obj.is_valid():
            serializer_obj.save()
            self.add_obj_in_approval(serializer_obj)
            return Response({'message': 'Vegetable created succesfully', 'id':serializer_obj.data['id']}, status=status.HTTP_200_OK)
        return Response(serializer_obj.errors, status=status.HTTP_400_BAD_REQUEST)

    def add_obj_in_approval(self, serializer_obj):
        vegetable = shop_models.Vegetable.objects.filter(pk=serializer_obj.data['id']).first()
        vegetable.is_approved = False
        vegetable.save()
        approval_obj = approval_models.VegetableApproval(vegetable=vegetable, is_approved=False, action='Create')
        approval_obj.save()


class ChangeIsAvailibilityOfVegetable(APIView):
    def post(self, request):
        valid_keys = ['vegetable', 'is_available']
        for key in valid_keys:
            if key not in self.request.data:
                return Response('Include ' + key + ' in data', status=status.HTTP_400_BAD_REQUEST)

        vegetable = shop_models.Vegetable.objects.filter(pk=self.request.data['vegetable'],).first()
        if not vegetable:
            return Response({'message': 'Invalid Vegetable ID'}, status=status.HTTP_400_BAD_REQUEST)
        vegetable.is_available = self.request.data['is_available']
        vegetable.save()
        return Response({'message': 'Vegetable Availability Changes Succesfully'}, status=status.HTTP_400_BAD_REQUEST)


class ListSlots(generics.ListAPIView):
    renderer_classes = [JSONRenderer]
    serializer_class = shop_serializer.ListSlotsSerializer

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


class ListFoodPackages(generics.ListAPIView):
    renderer_classes = [JSONRenderer]
    serializer_class = shop_serializer.GetFoodPackageSerializer

    def get_queryset(self):
        shop = shop_models.Shop.objects.filter(pk=self.kwargs['pk']).first()
        return shop_models.FoodPackage.objects.filter(shop=shop, is_approved=True)


class ListSpecificFoodPackage(generics.ListAPIView):
    renderer_classes = [JSONRenderer]
    serializer_class = shop_serializer.GetFoodPackageSerializer

    def get_queryset(self):
        return shop_models.FoodPackage.objects.filter(pk=self.kwargs['pk'])

class CreateFoodPackage(generics.CreateAPIView):
    renderer_classes = [JSONRenderer]
    serializer_class = shop_serializer.CreateFoodPackageSerializer
# class CreateFoodPackage(APIView):
#     def post(self, request):
#         valid_keys = ['shop', 'name']
#         for key in valid_keys:
#             if key not in self.request.data:
#                 return Response('Include ' + key + ' in data', status=status.HTTP_400_BAD_REQUEST)
#         serializer_obj = shop_serializer.CreateFoodPackageSerializer(data=self.request.data)
#         if serializer_obj.is_valid():
#             serializer_obj.save()
#             self.add_obj_in_approval(serializer_obj)
#             return Response({'message': 'Food Package created succesfully', 'id':serializer_obj.data['id']}, status=status.HTTP_200_OK)
#         return Response(serializer_obj.errors, status=status.HTTP_400_BAD_REQUEST)

#     def add_obj_in_approval(self, serializer_obj):
#         food_package = shop_models.FoodPackage.objects.filter(pk=serializer_obj.data['id']).first()
#         food_package.is_approved = False
#         food_package.save()
#         approval_obj = approval_models.FoodPackageApproval(food_package=food_package, is_approved=False, action='Create')
#         approval_obj.save()


# class CreateFoodMeal(generics.CreateAPIView):
#     renderer_classes = [JSONRenderer]
#     serializer_class = shop_serializer.CreateFoodMealSerializer


class ListFoodMeal(generics.ListAPIView):
    renderer_classes = [JSONRenderer]
    serializer_class = shop_serializer.ListFoodMealSerializer

    def get_queryset(self):
        shop = shop_models.Shop.objects.filter(pk=self.kwargs['pk']).first()
        return shop_models.FoodMeal.objects.filter(shop=shop, is_approved=True)

class CreateFoodMeal(APIView):
    def post(self, request):
        valid_keys = ['shop', 'name', 'food_type', 'day']
        for key in valid_keys:
            if key not in self.request.data:
                return Response('Include ' + key + ' in data', status=status.HTTP_400_BAD_REQUEST)
        serializer_obj = shop_serializer.CreateFoodMealSerializer(data=self.request.data)
        if serializer_obj.is_valid():
            serializer_obj.save()
            self.add_obj_in_approval(serializer_obj)
            return Response({'message': 'Food Meal created succesfully', 'id':serializer_obj.data['id']}, status=status.HTTP_200_OK)
        return Response(serializer_obj.errors, status=status.HTTP_400_BAD_REQUEST)

    def add_obj_in_approval(self, serializer_obj):
        meal = shop_models.FoodMeal.objects.filter(pk=serializer_obj.data['id']).first()
        meal.is_approved = False
        meal.save()
        approval_obj = approval_models.FoodMealApproval(meal=meal, is_approved=False, action='Create')
        approval_obj.save()


class ChangeIsAvailibilityOfFoodMeal(APIView):
    def post(self, request):
        valid_keys = ['food_meal', 'is_available']
        for key in valid_keys:
            if key not in self.request.data:
                return Response('Include ' + key + ' in data', status=status.HTTP_400_BAD_REQUEST)

        food_meal = shop_models.FoodMeal.objects.filter(pk=self.request.data['food_meal'],).first()
        if not food_meal:
            return Response({'message': 'Invalid FoodMeal ID'}, status=status.HTTP_400_BAD_REQUEST)
        food_meal.is_available = self.request.data['is_available']
        food_meal.save()
        return Response({'message': 'FoodMeal Availability Changes Succesfully'}, status=status.HTTP_400_BAD_REQUEST)


class CreateFoodDish(generics.CreateAPIView):
    renderer_classes = [JSONRenderer]
    serializer_class = shop_serializer.CreateFoodDishesSerializer


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


class CreateShopPromocode(generics.CreateAPIView):
    renderer_classes = [JSONRenderer]
    serializer_class = shop_serializer.CreateShopPromocodeSerializer


class ListShopPromocode(generics.ListAPIView):
    renderer_classes = [JSONRenderer]
    serializer_class = shop_serializer.ListShopPromocodeSerializer

    def get_queryset(self):
        shop = shop_models.Shop.objects.filter(pk=self.kwargs['pk']).first()
        return shop_models.ShopPromocode.objects.filter(shop=shop)


class UpdateDeleteShopPromocode(generics.RetrieveUpdateDestroyAPIView):
    renderer_classes = [JSONRenderer]
    serializer_class = shop_serializer.ListShopPromocodeSerializer
    queryset = shop_models.ShopPromocode.objects.all()