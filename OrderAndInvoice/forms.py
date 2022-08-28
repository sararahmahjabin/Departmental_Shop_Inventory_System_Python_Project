from django import forms
from django.db import models

from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['customers', 'product','quantity','Order_status']