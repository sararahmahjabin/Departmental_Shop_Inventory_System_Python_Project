from django.shortcuts import render,redirect
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from .models import Product
from .models import Categorie
from .models import Stock
from .forms import ProductForm
from .forms import SupplierForm
from .models import Supplier
from .forms import AddStock
from .forms import AddCategory
from django.contrib import messages



# Create your views here.




def create_product(request):
    forms = ProductForm()
    if request.method == 'POST':
        forms = ProductForm(request.POST)
        if forms.is_valid():
            forms.save()
            messages.info(request, 'Product added successfully ✅')

    context = {
        'form': forms
    }
    return render(request, 'store/create_product.html', context)

def showProducts(request):

    products = Product.objects.all()

    context = {
        'all_products': products
    }

    return render(request, 'store/product_list.html', context)

def InsertSupplier(request):
    sup = SupplierForm()
    if request.method == 'POST':
        sup = SupplierForm(request.POST)
        if sup.is_valid():
            sup.save()
            messages.info(request, 'Supplier added successfully ✅')


    context = {
        'form': sup
    }
    return render(request, 'store/create_supplier.html', context)

def ShowSupplier(request):

    supplier = Supplier.objects.all()

    context = {

        'all_supplier' : supplier
    }

    return render(request, 'store/supplier_list.html', context)


def ViewStock(request):

    stock = Stock.objects.all()

    context = {

        'all_stock' : stock
    }

    return render(request, 'store/stock_list.html', context)

def ViewCatagory(request):

    cate = Categorie.objects.all()

    context = {

        'all_categories' : cate
    }
    return render(request, 'store/category_list.html', context)

def Add_stock(request):
    stk = AddStock()
    if request.method == 'POST':
        stk = AddStock(request.POST)
        if stk.is_valid():
            stk.save()
            messages.info(request, 'Stock added successfully ✅')

    context = {
        'form': stk
    }
    return render(request, 'store/create_stock.html', context)

def create_category(request):
    cate = AddCategory()
    if request.method == 'POST':
        cate = AddCategory(request.POST)
        if cate.is_valid():
            cate.save()
            messages.info(request, 'Category added successfully ✅')

    context = {
        'form': cate
    }
    return render(request, 'store/create_category.html', context)








