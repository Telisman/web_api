from django.shortcuts import render
from django.http import JsonResponse
from .models import Productlines
from .serializers import ProductlinesSerializers



def productlines(request):
    productlines = Productlines.objects.all()
    serializers = ProductlinesSerializers(productlines, many=True)
    return JsonResponse(serializers.data, safe=False)
