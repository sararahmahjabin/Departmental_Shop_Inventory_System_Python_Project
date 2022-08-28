from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


# Create your models here.

class Staff(models.Model):
    Full_name = models.CharField(max_length=50)                     #models.CharField(max_length=200, default="First Name")
    Designation = models.CharField(max_length=200)
    Expertise = models.TextField(max_length=200)
    Date_of_Birth = models.CharField(max_length=100, blank=True, null=True)
    Phone_num = models.IntegerField(blank=True,null=True)
    Email = models.EmailField(max_length=200, unique=True)
    Profile_Picture = models.ImageField(upload_to='users/profile_pictures', blank=True, null=True)

    user = models.ForeignKey(User, default=None, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
