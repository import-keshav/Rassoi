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