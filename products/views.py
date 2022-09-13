from django.shortcuts import render
from django.http import JsonResponse
from .models import Products
from .serializers import ProductsSerializers



def products(request):
    products = Products.objects.all()
    serializers = ProductsSerializers(products, many=True)
    return JsonResponse(serializers.data, safe=False)
