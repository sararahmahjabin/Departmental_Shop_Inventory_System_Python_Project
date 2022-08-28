from django.shortcuts import render
from django.contrib import messages

from .models import Order
from .forms import OrderForm
from .models import Product
from InventoryManagement.models import Stock




#global a
#a=0
# Create your views here.
def create_Order(request):
    #count = 0
    forms = OrderForm()
    if request.method == 'POST':
        forms = OrderForm(request.POST)

        if forms.is_valid():

            order = forms.save(commit=False)

            print(forms)

            product = forms.cleaned_data['product']

            price = product.price

            quantity = forms.cleaned_data['quantity']

            total_price = price*quantity

            order.Price = total_price

            print(total_price, order.Price)

            stock = Stock.objects.get(product=product)
        if stock.Quantity >= quantity:
            
            stock.Quantity -= quantity
            stock.sell+=quantity
            #print(count)
            stock.save()

            order.save()
            messages.info(request, 'Order has been created successfully ✅')

        else:
            messages.info(request, 'Insufficient Stock ⚠️')
    #class New:
        #def __init__(self):
            #self.count = count

    #def f():
        #return New()
    #x = count 
    #def fun2():
        #print(x)

    #return fun2

    context = {
        'form': forms
    }
    return render(request, 'store/create_order.html', context)

#t = create_Order()()
    

def ShowOrder(request):
    order = Order.objects.all()

    context = {

        'all_Orders' : order,
        
    }

    return render(request, 'store/order_list.html', context)

def TotalSell(request):
    
    stock = Stock.objects.all()
    #.order_by("-sell")
    #.filter(Quantity=Product.id).order_by('-check_in')
    
    

    context = {

        'totalsell' : stock
    }

    return render(request, 'store/totalsell.html', context)    



