from django.db import models
from firm.models import MyFirm
# Create your models here.
class Inventory(models.Model):
    firm = models.ForeignKey(MyFirm, on_delete=models.CASCADE, related_name='firm_inventories')
    title = models.CharField(max_length=50,blank=False, null=False)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.title} ({self.firm.name})"

class Category(models.Model):
    inventory = models.ForeignKey(Inventory, on_delete=models.CASCADE, related_name='categories')
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    class Meta:
        unique_together = ('inventory', 'name')  # avoid duplicate category names within the same inventory

    def __str__(self):
        return f"{self.name} ({self.inventory.title})"

class Item(models.Model):
    inventory = models.ForeignKey(Inventory, on_delete=models.CASCADE, related_name='inventory_items')
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL, related_name='category_items')

    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    sku = models.CharField(max_length=100, blank=True)
    stock = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.name} ({self.inventory.name})"
