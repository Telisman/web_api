from django.db import models

class Products(models.Model):
    id = models.AutoField(primary_key=True)
    productCode = models.CharField(max_length=15,null=True)
    productName = models.CharField(max_length=70,null=True)
    productLine = models.CharField(max_length=50,null=True)
    productScale= models.CharField(max_length=10,null=True)
    productVendor = models.CharField(max_length=50,null=True)
    productDescription= models.TextField()
    quantityInStock= models.IntegerField(null=True)
    buyPrice= models.DecimalField(max_digits=10, decimal_places=2)
    MSRP= models.DecimalField(max_digits=10, decimal_places=2)

