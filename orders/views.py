from django.shortcuts import render
from django.http import JsonResponse
from .models import Orders
from .serializers import OrdersSerializers



def orders(request):
    orders = Orders.objects.all()
    serializers = OrdersSerializers(orders, many=True)
    return JsonResponse(serializers.data, safe=False)
