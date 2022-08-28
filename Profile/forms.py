from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms





class CreateUserCreateForm(UserCreationForm):
    class Meta:
        model = User
        fields =['username','email','first_name','last_name','password1','password2']





class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Username',
    }))
    password = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Password',
        'type': 'password'
    }))
