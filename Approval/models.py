from django.db import models
from django.db.models.query import QuerySet

from Fruit import models as fruit_models
from Food import models as food_models
from Grocery import models as grocery_models
from Vegetable import models as vegetable_models

ACTIONS = (
    ('Create', 'Create'),
    ('Update', 'Update'),
    ('Delete', 'Delete'),
)

class GroceryApproval(models.Model):
    grocery = models.ForeignKey(grocery_models.Grocery, on_delete=models.CASCADE, related_name="grocery_grocery_approval_grocery", null=True, blank=True)
    is_approved = models.BooleanField(default=False, null=True, blank=True)
    action = models.TextField(choices=ACTIONS, null=True, blank=True)

    class Meta:
        verbose_name = 'Grocery Approval'
        verbose_name_plural = 'Grocery Approvals'
    def __str__(self):
        return self.grocery.name
    def save(self):
        super(GroceryApproval, self).save()
        if self.is_approved:
            grocery = grocery_models.Grocery.objects.filter(pk=self.grocery.pk).first()
            grocery.is_approved = True
            grocery.save()
            super(GroceryApproval, self).delete()


class FruitApproval(models.Model):
    fruit = models.ForeignKey(fruit_models.Fruit, on_delete=models.CASCADE, related_name="fruit_fruit_approval_fruit", null=True, blank=True)
    is_approved = models.BooleanField(default=False, null=True, blank=True)
    action = models.TextField(choices=ACTIONS, null=True, blank=True)

    class Meta:
        verbose_name = 'Fruit Approval'
        verbose_name_plural = 'Fruit Approvals'
    def __str__(self):
        return self.fruit.name
    def save(self):
        super(FruitApproval, self).save()
        if self.is_approved:
            fruit = fruit_models.Fruit.objects.filter(pk=self.fruit.pk).first()
            fruit.is_approved = True
            fruit.save()
            super(FruitApproval, self).delete()


class VegetableApproval(models.Model):
    vegetable = models.ForeignKey(vegetable_models.Vegetable, on_delete=models.CASCADE, related_name="vegetable_vegetable_approval_vegetable", null=True, blank=True)
    is_approved = models.BooleanField(default=False, null=True, blank=True)
    action = models.TextField(choices=ACTIONS, null=True, blank=True)

    class Meta:
        verbose_name = 'Vegetable Approval'
        verbose_name_plural = 'Vegetable Approvals'
    def __str__(self):
        return self.vegetable.name
    def save(self):
        super(VegetableApproval, self).save()
        if self.is_approved:
            vegetable = vegetable_models.Vegetable.objects.filter(pk=self.vegetable.pk).first()
            vegetable.is_approved = True
            vegetable.save()
            super(VegetableApproval, self).delete()


class FoodMealApproval(models.Model):
    meal = models.ForeignKey(food_models.FoodMeal, on_delete=models.CASCADE, related_name="approval_food_meal_meal", null=True, blank=True)
    is_approved = models.BooleanField(default=False, null=True, blank=True)
    action = models.TextField(choices=ACTIONS, null=True, blank=True)

    class Meta:
        verbose_name = 'Food Meal Approval'
        verbose_name_plural = 'Food Meal Approvals'
    def save(self):
        super(FoodMealApproval, self).save()
        if self.is_approved:
            meal = food_models.FoodMeal.objects.filter(pk=self.meal.pk).first()
            meal.is_approved = True
            meal.save()
            super(FoodMealApproval, self).delete()