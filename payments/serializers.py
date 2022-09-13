from rest_framework import serializers
from .models import Payments
class PaymentsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Payments
        fields = [
                  'id_payments',
                  'customerNumber',
                  'checkNumber',
                  'paymentDate',
                  'amount',
                  ]