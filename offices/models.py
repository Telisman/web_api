from django.db import models
class Offices(models.Model):
    id = models.AutoField(primary_key=True)
    officeCode = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    addressLine1 = models.CharField(max_length=50,null=True)
    addressLine2 = models.CharField(max_length=50,null=True)
    state = models.CharField(max_length=50,null=True)
    country = models.CharField(max_length=50)
    postalCode = models.CharField(max_length=15)
    territory = models.CharField(max_length=10)