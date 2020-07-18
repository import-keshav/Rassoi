from django import forms
from rest_framework import serializers

from . import models as shop_models


class ListShop(serializers.ModelSerializer):
    class Meta:
        model = shop_models.Shop
        fields = '__all__'


class GetGroceryInNumOfItemsPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = shop_models.GroceryInNumOfItemsPrice
        fields = '__all__'

class GetGroceryInKgQuantityPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = shop_models.GroceryInKgQuantityPrice
        fields = '__all__'

class GetGroceryInLitresPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = shop_models.GroceryInLitresPrice
        fields = '__all__'


class ListGroceriesSerializer(serializers.ModelSerializer):
    kg_price = serializers.SerializerMethodField()
    num_of_items_price = serializers.SerializerMethodField()
    litre_price = serializers.SerializerMethodField()

    def get_kg_price(self, obj):
        items = shop_models.GroceryInKgQuantityPrice.objects.filter(grocery=obj)
        return [GetGroceryInKgQuantityPriceSerializer(item).data for item in items]

    def get_num_of_items_price(self, obj):
        items = shop_models.GroceryInNumOfItemsPrice.objects.filter(grocery=obj)
        return [GetGroceryInNumOfItemsPriceSerializer(item).data for item in items]

    def get_litre_price(self, obj):
        items = shop_models.GroceryInLitresPrice.objects.filter(grocery=obj)
        return [GetGroceryInLitresPriceSerializer(item).data for item in items]

    class Meta:
        model = shop_models.Grocery
        fields = '__all__'


class CreateGrocerySerializer(serializers.ModelSerializer):
    class Meta:
        model = shop_models.Grocery
        fields = '__all__'
    def validate(self, data):
        must_keys = ['shop', 'name']
        for key in must_keys:
            if not key in data:
                raise forms.ValidationError('Include ' + key + ' in data')
        return data


class ListFruitsSerializer(serializers.ModelSerializer):
    class Meta:
        model = shop_models.Fruit
        fields = '__all__'


class CreateFruitsSerializer(serializers.ModelSerializer):
    class Meta:
        model = shop_models.Fruit
        fields = '__all__'
    def validate(self, data):
        must_keys = ['shop', 'name', 'price_per_kg', 'price_per_dozen']
        for key in must_keys:
            if not key in data:
                raise forms.ValidationError('Include ' + key + ' in data')
        return data

class ListVegetableSerializer(serializers.ModelSerializer):
    class Meta:
        model = shop_models.Vegetable
        fields = '__all__'


class CreateVegetableSerializer(serializers.ModelSerializer):
    class Meta:
        model = shop_models.Vegetable
        fields = '__all__'
    def validate(self, data):
        must_keys = ['shop', 'name', 'price_per_kg']
        for key in must_keys:
            if not key in data:
                raise forms.ValidationError('Include ' + key + ' in data')
        return data


class ListSlotsSerializer(serializers.ModelSerializer):
    class Meta:
        model = shop_models.Slots
        fields = '__all__'


class CreateSlotSerializer(serializers.ModelSerializer):
    class Meta:
        model = shop_models.Slots
        fields = '__all__'
    def validate(self, data):
        must_keys = ['shop', 'category', 'start_time', 'end_time', 'date']
        for key in must_keys:
            if not key in data:
                raise forms.ValidationError('Include ' + key + ' in data')
        return data

class UpdateDeleteSlotsSerializer(serializers.ModelSerializer):
    class Meta:
        model = shop_models.Slots
        fields = '__all__'


class ListFoodDishesSerializer(serializers.ModelSerializer):
    class Meta:
        model = shop_models.FoodDishes
        fields = '__all__'


class CreateFoodDishesSerializer(serializers.ModelSerializer):
    class Meta:
        model = shop_models.FoodDishes
        fields = '__all__'
    def validate(self, data):
        must_keys = ['meal', 'name', 'number_of_items']
        for key in must_keys:
            if not key in data:
                raise forms.ValidationError('Include ' + key + ' in data')
        return data


class ListFoodMealSerializer(serializers.ModelSerializer):
    dishes = serializers.SerializerMethodField()
    def get_dishes(self, obj):
        dishes = shop_models.FoodDishes.objects.filter(meal=obj)
        return [ListFoodDishesSerializer(dish).data for dish in dishes]

    class Meta:
        model = shop_models.FoodMeal
        fields = '__all__'


class CreateFoodMealSerializer(serializers.ModelSerializer):
    class Meta:
        model = shop_models.FoodMeal
        fields = '__all__'
    def validate(self, data):
        must_keys = ['shop', 'name', 'food_type', 'day', 'price']
        for key in must_keys:
            if not key in data:
                raise forms.ValidationError('Include ' + key + ' in data')
        return data

class GetFoodPackageSerializer(serializers.ModelSerializer):
    # meals = serializers.SerializerMethodField()
    # def get_meals(self, obj):
    #     meals = shop_models.FoodMeal.objects.filter(package=obj)
    #     return [ListFoodMealSerializer(meal).data for meal in meals]

    class Meta:
        model = shop_models.FoodPackage
        fields = '__all__'


class CreateFoodPackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = shop_models.FoodPackage
        fields = '__all__'
    def validate(self, data):
        must_keys = ['shop', 'name', 'price_per_week_total', 'price_per_week_type']
        for key in must_keys:
            if not key in data:
                raise forms.ValidationError('Include ' + key + ' in data')
        return data


class CreateShopPromocodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = shop_models.ShopPromocode
        fields = '__all__'
    def validate(self, data):
        must_keys = ['promocode', 'shop', 'discount_percentage',
        'valid_date', 'maximum_discount_price', 'maximum_number_of_usage',
        'category']
        for key in must_keys:
            if not key in data:
                raise forms.ValidationError('Include ' + key + ' in data')
        return data


class ListShopPromocodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = shop_models.ShopPromocode
        fields = '__all__'
