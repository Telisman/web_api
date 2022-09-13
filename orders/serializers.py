from rest_framework import serializers
from .models import Orders
class OrdersSerializers(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = [
                  'orderNumber',
                  'orderDate',
                  'requiredDate',
                  'shippedDate',
                  'status',
                  'comments',
                  'customerNumber',
                  ]