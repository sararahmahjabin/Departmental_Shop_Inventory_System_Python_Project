from django.db import models

# Create your models here.


# Create your models here.

class Customer(models.Model):
    First_name = models.CharField(max_length=100)
    Last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=200, unique=True)
    phn_no = models.IntegerField(blank=True, null=True)
    Street = models.CharField(max_length=200)
    City = models.CharField(max_length=100)
    zip_code = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.First_name

class Member(models.Model):
    Products_points = models.IntegerField(blank=True)
    customers = models.ForeignKey(Customer,on_delete=models.CASCADE,default=1)

    def __str__(self):
        return self.customers.First_name