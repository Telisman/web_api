from rest_framework import serializers
from .models import Customers
class Customersserializers(serializers.ModelSerializer):
    class Meta:
        model = Customers
        fields = [
                  'customerNumber',
                  'customerName',
                  'contactLastName',
                  'contactFirstName',
                  'phone',
                  'addressLine1',
                  'addressLine2',
                  'city',
                  'state',
                  'postalCode',
                  'country',
                  'creditLimit'
                  ]