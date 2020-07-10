from django.db import models
from django.db.models.query import QuerySet

from Shop import models as shop_models

ACTIONS = (
    ('Create', 'Create'),
    ('Update', 'Update'),
    ('Delete', 'Delete'),
)

class GroceryApproval(models.Model):
    grocery = models.ForeignKey(shop_models.Grocery, on_delete=models.CASCADE, related_name="grocery_grocery_approval_grocery", null=True, blank=True)
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
            grocery = shop_models.Grocery.objects.filter(pk=self.grocery.pk).first()
            grocery.is_approved = True
            grocery.save()
            super(GroceryApproval, self).delete()


class FruitApproval(models.Model):
    fruit = models.ForeignKey(shop_models.Fruit, on_delete=models.CASCADE, related_name="fruit_fruit_approval_fruit", null=True, blank=True)
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
            fruit = shop_models.Fruit.objects.filter(pk=self.fruit.pk).first()
            fruit.is_approved = True
            fruit.save()
            super(FruitApproval, self).delete()


class VegetableApproval(models.Model):
    vegetable = models.ForeignKey(shop_models.Vegetable, on_delete=models.CASCADE, related_name="vegetable_vegetable_approval_vegetable", null=True, blank=True)
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
            vegetable = shop_models.Vegetable.objects.filter(pk=self.vegetable.pk).first()
            vegetable.is_approved = True
            vegetable.save()
            super(VegetableApproval, self).delete()


class FoodPackageApproval(models.Model):
    food_package = models.ForeignKey(shop_models.FoodPackage, on_delete=models.CASCADE, related_name="food_package_food_package_approval_food_package", null=True, blank=True)
    is_approved = models.BooleanField(default=False, null=True, blank=True)
    action = models.TextField(choices=ACTIONS, null=True, blank=True)

    class Meta:
        verbose_name = 'Food Package Approval'
        verbose_name_plural = 'Food Package Approvals'
    def __str__(self):
        return self.food_package.name
    def save(self):
        super(FoodPackageApproval, self).save()
        if self.is_approved:
            food_package = shop_models.FoodPackage.objects.filter(pk=self.food_package.pk).first()
            food_package.is_approved = True
            food_package.save()
            super(FoodPackageApproval, self).delete()