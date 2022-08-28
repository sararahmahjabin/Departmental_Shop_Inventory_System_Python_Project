from .forms import CreateUserCreateForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

from .forms import LoginForm
from django.contrib import messages

# Create your views here.
def Userregistration(request):

    form_obj = CreateUserCreateForm()

    if request.method == "POST":

        form_obj = CreateUserCreateForm(request.POST)

        if form_obj.is_valid():
            form_obj.save()
            messages.info(request, 'User added successfully ✅')


    context ={

        "reg_form": form_obj

    }
    return render(request, 'Profile/userregistration.html', context)



def login_page(request):
    forms = LoginForm()
    if request.method == 'POST':
        forms = LoginForm(request.POST)
        if forms.is_valid():
            username = forms.cleaned_data['username']
            password = forms.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('dashboard')
    context = {'form': forms}
    return render(request, 'users/login.html', context)


def logout_page(request):
    logout(request)
    return redirect('login')

