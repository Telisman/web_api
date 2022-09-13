from rest_framework import serializers
from .models import Employees
class EmployeesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields = [
                  'employeeNumber',
                  'lastName',
                  'firstName',
                  'extension',
                  'email',
                  'officeCode',
                  'jobTitle',
                  'reportsTo',
                  'jobTitle',

                  ]