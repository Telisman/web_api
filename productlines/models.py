from django.db import models
class Productlines(models.Model):
    id = models.AutoField(primary_key=True)
    productLine = models.CharField(max_length=50)
    textDescription = models.CharField(max_length=4000)
    htmlDescription = models.CharField(max_length=50, null=True)
    image = models.CharField(max_length=50, null=True)