from django import forms
from rest_framework import serializers

from . import models as order_models
from Client import models as cliet_models
from Fruit import models as fruit_models
from Food import models as food_models
from Grocery import models as grocery_models
from Vegetable import models as vegetable_models
from Shop import models as shop_models

from Client import serializers as client_serializer
from Fruit import serializers as fruit_serializer
from Food import serializers as food_serializer
from FoodPackage import serializers as food_package_serializer
from Grocery import serializers as grocery_serializer
from Promocode import serializers as promocode_serializer
from Shop import serializers as shop_serializer
from Vegetable import serializers as vegetable_serializer


class ListOrderGrocerySerializer(serializers.ModelSerializer):
    grocery = grocery_serializer.ListGroceriesSerializer()
    grocery_price = grocery_serializer.GetGroceryPriceSerializer()
    class Meta:
        model = order_models.OrderGrocery
        fields = '__all__'


class ListOrderFruitSerializer(serializers.ModelSerializer):
    fruit = fruit_serializer.ListFruitsSerializer()
    fruit_price = fruit_serializer.GetFruitPriceSerializer()
    class Meta:
        model = order_models.OrderFruit
        fields = '__all__'


class ListOrderVegetableSerializer(serializers.ModelSerializer):
    vegetable = vegetable_serializer.ListVegetableSerializer()
    vegetable_price = vegetable_serializer.GetVegetablePriceSerializer()
    class Meta:
        model = order_models.OrderVegetable
        fields = '__all__'


class ListOrderFoodMealSerializer(serializers.ModelSerializer):
    food_meal = food_serializer.ListFoodMealSerializer()
    class Meta:
        model = order_models.OrderFoodMeal
        fields = '__all__'


class ListOngoingShopOrderSerializer(serializers.ModelSerializer):
    client = client_serializer.GetClientInfoSerializer()
    shop = shop_serializer.ListShop()
    slot = shop_serializer.ListSlotsSerializer()
    promocode_used = promocode_serializer.ListShopPromocodeSerializer()
    items = serializers.SerializerMethodField()

    def get_items(self, obj):
        if obj.order_type == 'Grocery':
            return [ListOrderGrocerySerializer(order_grocery).data for order_grocery in order_models.OrderGrocery.objects.filter(order=obj)]
        elif obj.order_type == 'Fruit':
            return [ListOrderFruitSerializer(order_fruit).data for order_fruit in order_models.OrderFruit.objects.filter(order=obj)]
        elif obj.order_type == 'Vegetable':
            return [ListOrderVegetableSerializer(order_vegetable).data for order_vegetable in order_models.OrderVegetable.objects.filter(order=obj)]
        elif obj.order_type == 'Food':
            return [ListOrderFoodMealSerializer(order_food_meal).data for order_food_meal in order_models.OrderFoodMeal.objects.filter(order=obj)]

    class Meta:
        model = order_models.Order
        fields = '__all__'


class CreateOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = order_models.Order
        fields = '__all__'

    def validate(self, data):
        must_keys = [
        	'shop', 'client', 'payment_method', 'total_amount',
        	'order_type', 'slot', 'client_address_details']
        for key in must_keys:
            if not key in data:
                raise forms.ValidationError('Include ' + key + ' in data')
        # if data['slot'].category != data['order_type']:
        #     raise forms.ValidationError('This Slot is not of the given order type')            
        if data['slot'].shop != data['shop']:
            raise forms.ValidationError('This Slot is not of the given Shop')            
        return data


class CreateOrderGrocerySerializer(serializers.ModelSerializer):
    class Meta:
        model = order_models.OrderGrocery
        fields = '__all__'

    def validate(self, data):
        must_keys = ['order', 'grocery', 'grocery_price', 'num_of_items']
        for key in must_keys:
            if not key in data:
                raise forms.ValidationError('Include ' + key + ' in data')
        if data['order'].shop != data['grocery'].shop:
            raise forms.ValidationError('This Grocery not belongs to the given order shop')
        if data['grocery_price'].grocery != data['grocery']:
            raise forms.ValidationError('This Grocery Price not belongs to the given Grocery')
        return data


class CreateOrderFruitSerializer(serializers.ModelSerializer):
    class Meta:
        model = order_models.OrderFruit
        fields = '__all__'

    def validate(self, data):
        must_keys = ['order', 'fruit', 'fruit_price', 'num_of_items']
        for key in must_keys:
            if not key in data:
                raise forms.ValidationError('Include ' + key + ' in data')
        if data['order'].shop != data['fruit'].shop:
            raise forms.ValidationError('This Fruit not belongs to the given order shop')
        if data['fruit_price'].fruit != data['fruit']:
            raise forms.ValidationError('This Fruit Price not belongs to the given Fruit')
        return data


class CreateOrderVegetableSerializer(serializers.ModelSerializer):
    class Meta:
        model = order_models.OrderVegetable
        fields = '__all__'

    def validate(self, data):
        must_keys = ['order', 'vegetable', 'vegetable_price', 'num_of_items']
        for key in must_keys:
            if not key in data:
                raise forms.ValidationError('Include ' + key + ' in data')
        if data['order'].shop != data['vegetable'].shop:
            raise forms.ValidationError('This Vegetable not belongs to the given order shop')
        if data['vegetable_price'].vegetable != data['vegetable']:
            raise forms.ValidationError('This Vegetable Price not belongs to the given Vegetable')
        return data


class CreateOrderFoodMealSerializer(serializers.ModelSerializer):
    class Meta:
        model = order_models.OrderFoodMeal
        fields = '__all__'

    def validate(self, data):
        must_keys = ['order', 'food_meal', 'num_of_items']
        for key in must_keys:
            if not key in data:
                raise forms.ValidationError('Include ' + key + ' in data')
        if data['order'].shop != data['food_meal'].shop:
            raise forms.ValidationError('This Food Meal not belongs to the given order shop')
        return data


class UpdateOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = order_models.Order
        fields = '__all__'


class CreateFoodPackageEachMealOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = order_models.FoodPackageEachMealOrder
        fields = '__all__'


class GetFoodPackageEachMealOrderSerializer(serializers.ModelSerializer):
    order = ListOngoingShopOrderSerializer()
    food_package = food_package_serializer.ListFoodPackageSerializerOnly()
    food_meal = food_serializer.ListFoodMealSerializer()

    class Meta:
        model = order_models.FoodPackageEachMealOrder
        fields = '__all__'