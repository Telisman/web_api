"""web_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path,include
from customers.views import customers
from employees.views import employees
from offices.views import offices
from orderd_info.views import orderd_info
from orders.views import orders
from payments.views import payments
# from productlines.views import productlines
from products.views import products
urlpatterns = [
    path('admin/', admin.site.urls),
    path('customers/', include('customers.urls')),
    path('employees/', include('employees.urls')),
    path('offices/', include('offices.urls')),
    path('orderdinfo/', include('orderd_info.urls')),
    path('orders/', include('orders.urls')),
    path('payments/', include('payments.urls')),
    path('productlines/', include('productlines.urls')),
    path('products/', include('products.urls')),

    # API page(JSON)
    path('api-auth/', include('rest_framework.urls')),
    path('customersAPI/', customers),
    path('employeesAPI/', employees),
    path('officesAPI/', offices),
    path('orderd_infoAPI/', orderd_info),
    path('paymentsAPI/', payments),
    path('ordersAPI/', orders),
    # path('productlinesAPI/', productlines),
    path('productsAPI/', products),
\
]
