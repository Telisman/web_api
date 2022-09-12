from django.db import models
from orders.models import Orders
class Orderd_info(models.Model):
    orderd_info_id = models.AutoField(primary_key=True)
    orderNumber = models.ForeignKey(Orders,null=True, on_delete=models.CASCADE)
    productCode = models.CharField(max_length=15,null=True)
    quantityOrdered= models.IntegerField(null=True,blank=True)
    orderLineNumber= models.IntegerField(null=True,blank=True)
    priceEach= models.DecimalField(max_digits=8, decimal_places=2)