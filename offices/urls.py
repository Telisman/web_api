from .views import officesView,AddOfffice
from django.urls import path

urlpatterns = [
    path('officesView/', officesView, name='officesView'),
    path('AddOfffice/', AddOfffice, name='AddOfffice'),

]
