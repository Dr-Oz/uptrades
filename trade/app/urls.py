from django.urls import path

from .views import *

urlpatterns = [
    path('home/', base, {'name': 'Home'}, name='home'),
    path('markets/', base, {'name': 'Markets'}, name='markets'),
    path('platforms/', base, {'name': 'Platforms'}, name='platforms'),
    path('platforms/mt4', base, {'name': 'Mt4'}, name='mt4'),
    path('platforms/mt4/download', base, {'name': 'Download'}, name='download'),
    path('platforms/mt5', base, {'name': 'Mt5'}, name='mt5'),
    path('platforms/mt5/desktop', base, {'name': 'Desktop'}, name='desktop'),
    path('platforms/mt5/phone', base, {'name': 'Phone'}, name='phone'),
    path('prices/', base, {'name': 'Investment'}, name='investment'),
]
