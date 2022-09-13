from django.shortcuts import render
from django.http import JsonResponse
from .models import Employees
from .serializers import EmployeesSerializers



def employees(request):
    employees = Employees.objects.all()
    serializers = EmployeesSerializers(employees, many=True)
    return JsonResponse(serializers.data, safe=False)
