from django.db import models
from offices.models import Offices
class Employees(models.Model):
    employeeNumber = models.AutoField(primary_key=True)
    lastName = models.CharField(max_length=100)
    firstName = models.CharField(max_length=100)
    extension = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    officeCode = models.ForeignKey(Offices,null=True, on_delete=models.CASCADE)
    jobTitle = models.CharField(max_length=100)
    reportsTo = models.IntegerField(null=True)
    jobTitle = models.CharField(max_length=100)

