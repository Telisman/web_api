from django.db import models
from employees.models import Employees
class Customers(models.Model):
    customerNumber = models.AutoField(primary_key=True)
    customerName = models.CharField(max_length=100,null=True)
    contactLastName = models.CharField(max_length=100,null=True)
    contactFirstName= models.CharField(max_length=100,null=True)
    phone = models.CharField(max_length=100,null=True)
    addressLine1= models.CharField(max_length=100,null=True)
    addressLine2= models.CharField(max_length=100, null=True)
    city= models.CharField(max_length=100,null=True)
    state= models.CharField(max_length=100,null=True)
    postalCode = models.CharField(max_length=100,null=True)
    country= models.CharField(max_length=100,null=True)
    salesRepEmployeeNumber = models.ForeignKey(Employees,null=True, on_delete=models.CASCADE)
    creditLimit= models.DecimalField(max_digits=8, decimal_places=2)