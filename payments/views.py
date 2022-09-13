from django.shortcuts import render
from django.http import JsonResponse
from .models import Payments
from .serializers import PaymentsSerializers



def payments(request):
    payments = Payments.objects.all()
    serializers = PaymentsSerializers(payments, many=True)
    return JsonResponse(serializers.data, safe=False)
