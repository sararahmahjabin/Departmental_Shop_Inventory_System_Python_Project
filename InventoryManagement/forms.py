from django import forms
from django.db import models

from .models import Product
from .models import Supplier
from .models import Stock
from .models import Categorie


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'brand','price','weight','categories','supplier']



class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = ['Supplier_Name','Phone_num','Email']


class AddStock(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['Quantity','product']

class AddCategory(forms.ModelForm):
    class Meta:
        model = Categorie
        fields = ['Categories_Name']



