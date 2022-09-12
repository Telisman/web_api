from django.db import models
from customers.models import Customers
class Orders(models.Model):
    orderNumber = models.AutoField(primary_key=True)
    orderDate = models.DateField(null=True)
    requiredDate = models.DateField(null=True)
    shippedDate= models.DateField(null=True)
    status = models.CharField(max_length=15,null=True)
    comments= models.TextField(null=True)
    customerNumber= models.ForeignKey(Customers,null=True, on_delete=models.CASCADE)
