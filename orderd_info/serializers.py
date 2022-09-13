from rest_framework import serializers
from .models import Orderd_info
class OrdersInfoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Orderd_info
        fields = [
                  'orderd_info_id',
                  'orderNumber',
                  'productCode',
                  'quantityOrdered',
                  'orderLineNumber',
                  'priceEach',
                  ]