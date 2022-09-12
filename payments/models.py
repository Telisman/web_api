from django.db import models
from customers.models import Customers
class Payments(models.Model):
    id_payments = models.AutoField(primary_key=True)
    customerNumber = models.ForeignKey(Customers,null=True, on_delete=models.CASCADE)
    checkNumber = models.CharField(max_length=50, null=True)
    paymentDate = models.DateField(null=True)
    amount = models.DecimalField(max_digits=8, decimal_places=2)