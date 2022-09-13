from django.db import models
class Productlines(models.Model):
    productLine = models.CharField(max_length=50)
    textDescription = models.CharField(max_length=4000)
    htmlDescription = models.CharField(max_length=50, null=True)
    image = models.CharField(max_length=50, null=True)