from rest_framework import serializers
from .models import Products
class ProductsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = [
                  'id',
                  'productCode',
                  'productName',
                  'productLine',
                  'productScale',
                  'productVendor',
                  'productDescription',
                  'quantityInStock',
                  'buyPrice',
                  'MSRP',
                  ]