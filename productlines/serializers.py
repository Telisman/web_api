from rest_framework import serializers
from .models import Productlines
class ProductlinesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Productlines
        fields = [
                  'id',
                  'productLine',
                  'textDescription',
                  'htmlDescription',
                  'image',
                  ]