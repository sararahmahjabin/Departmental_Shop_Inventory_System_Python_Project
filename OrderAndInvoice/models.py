from django.db import models
from InventoryManagement.models import Product
from CustomerManagement.models import Customer


# Create your models here.


class Order(models.Model):
    customers = models.ForeignKey(Customer, on_delete=models.CASCADE, default=1)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    Payment_date = models.DateField(auto_now_add=True)
    Price = models.IntegerField(blank=True, default=1)
    quantity = models.IntegerField(blank=True)
    Order_status = models.CharField(max_length=200)
    Order_date = models.DateField(auto_now_add=True)


    def __str__(self):
        return self.customers.First_name +" "+ self.customers.Last_name + " "+self.product.title + "  "+ str(self.Price) + "  "+ str(self.quantity)+ " "+ str(self.Order_status)+ " "+ str(self.Order_date)