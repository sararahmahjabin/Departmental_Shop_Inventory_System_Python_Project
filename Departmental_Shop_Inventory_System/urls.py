"""Departmental_Shop_Inventory_System URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from InventoryManagement import views as productsviews
from StaffManagement import views as staffmanagementviews
from Profile import views as usrregviews
from CustomerManagement import views as cus_insert
from CustomerManagement import views as viewcus
from InventoryManagement import views as create_product
from InventoryManagement import views as Supplier_ins
from InventoryManagement import views as show_sup
from OrderAndInvoice import views as New_order
from OrderAndInvoice import views as view_order
from OrderAndInvoice import views as total_sell
from .views import dashboard
from InventoryManagement import views as stkviw
from InventoryManagement import views as cateview
from InventoryManagement import views as addstk
from InventoryManagement import views as add_cate



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', dashboard, name='dashboard'),
    path('users/', include('Profile.urls')),
    path('products/',productsviews.showProducts,name = 'products'),
    path('ShowStaffInfo/',staffmanagementviews.ShowStaffInfo, name='staff-list'),
    path('userregistration/',usrregviews.Userregistration, name='add-user'),
    path('InsertCustomer/',cus_insert.InsertCustomer, name='create-buyer'),
    path('ViewCustomers/', viewcus.showCustomer, name='buyer-list'),
    path('create-product/', create_product.create_product, name='create-product'),
    path('products/',productsviews.showProducts, name='product-list'),
    path('InsertSupplier/',Supplier_ins.InsertSupplier, name='create-supplier'),
    path('ShowSupplier/', show_sup.ShowSupplier, name='supplier-list'),
    path('CreateOrder/', New_order.create_Order, name ='create-order'),
    path('Invoice/',view_order.ShowOrder, name='order-list'),
    path('StockView/', stkviw.ViewStock, name='stock-list' ),
    path('AddStock/', addstk.Add_stock, name='add-stock'),
    path('ViewCategories/', cateview.ViewCatagory, name='category-list'),
    path('AddCategory/',add_cate.create_category, name='add-category'),
    path('profile/', staffmanagementviews.ViewProfile, name='show_profile'),
    path('setupProfile/', staffmanagementviews.CreateProfile, name='create_profile'),
    path('totalsell/', total_sell.TotalSell, name='total-sell'),



]

if settings.DEBUG == True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)