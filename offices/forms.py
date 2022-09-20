from django import forms
from django.forms import ModelForm
from .models import Offices

class Office(ModelForm):
    class Meta:
        model = Offices
        fields = ('officeCode',
                  'city',
                  'phone',
                  'addressLine1',
                  'addressLine2',
                  'state',
                  'country',
                  'postalCode',
                  'territory',

                  )

        widgets = {
            'officeCode': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'addressLine1': forms.TextInput(attrs={'class': 'form-control'}),
            'addressLine2': forms.TextInput(attrs={'class': 'form-control'}),
            'state': forms.TextInput(attrs={'class': 'form-control'}),
            'postalCode': forms.TextInput(attrs={'class': 'form-control'}),
            'territory': forms.TextInput(attrs={'class': 'form-control'}),
        }