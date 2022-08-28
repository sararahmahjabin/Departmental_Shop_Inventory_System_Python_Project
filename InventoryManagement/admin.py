from django.contrib import admin
from .models import Product,Stock,Supplier,Categorie

# Register your models here.
admin.site.register([Product,Stock,Supplier,Categorie])