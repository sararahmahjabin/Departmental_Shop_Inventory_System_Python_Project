from django.shortcuts import render,redirect

# Create your views here.

from .models import Customer
from .forms import CustomerInsertForm
from django.contrib import messages


def InsertCustomer(request):
    forms = CustomerInsertForm
    if request.method == "POST":
        forms = CustomerInsertForm(request.POST)
        if forms.is_valid():
            forms.save()
            messages.info(request, 'Customer added successfully ✅')



    context ={

        'form' : forms
    }
    return render(request, 'store/create_buyer.html',context)

def showCustomer(request):

    customers = Customer.objects.all()

    context = {
        'all_customers': customers
    }

    return render(request, 'store/buyer_list.html', context)