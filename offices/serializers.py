from rest_framework import serializers
from .models import Offices
class OfficesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Offices
        fields = [
                  'id',
                  'officeCode',
                  'city',
                  'phone',
                  'addressLine1',
                  'addressLine2',
                  'state',
                  'postalCode',
                  'country',
                  'territory',
                  ]