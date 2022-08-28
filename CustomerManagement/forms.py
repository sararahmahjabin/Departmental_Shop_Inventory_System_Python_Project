
from django import forms
from .models import Customer


class CustomerInsertForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['First_name','Last_name','email','phn_no','Street','City','zip_code']