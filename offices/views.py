from django.shortcuts import render
from django.http import JsonResponse
from .models import Offices
from .serializers import OfficesSerializers



def offices(request):
    offices = Offices.objects.all()
    serializers = OfficesSerializers(offices, many=True)
    return JsonResponse(serializers.data, safe=False)
