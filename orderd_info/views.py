from django.shortcuts import render
from django.http import JsonResponse
from .models import Orderd_info
from .serializers import OrdersInfoSerializers



def orderd_info(request):
    orderd_info = Orderd_info.objects.all()
    serializers = OrdersInfoSerializers(orderd_info, many=True)
    return JsonResponse(serializers.data, safe=False)
