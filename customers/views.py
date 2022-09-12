from django.shortcuts import render
from django.http import JsonResponse
from .models import Customers
from .serializers import Customersserializers



def customers(request):
    customers = Customers.objects.all()
    serializers = Customersserializers(customers, many=True)
    return JsonResponse(serializers.data, safe=False)
