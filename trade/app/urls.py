from django.urls import path

from .views import *

urlpatterns = [
    path('home/', base, {'name': 'Home'}, name='home'),
    path('company/', base, {'name': 'Markets'}, name='markets'),
    path('development/', base, {'name': 'Platforms'}, name='platforms'),
    path('development/cpp', base, {'name': 'Mt4'}, name='mt4'),
    path('development/cpp/qt', base, {'name': 'Download'}, name='download'),
    path('development/python', base, {'name': 'Mt5'}, name='mt5'),
    path('development/python/django', base, {'name': 'Desktop'}, name='desktop'),
    path('development/python/tornado', base, {'name': 'Phone'}, name='phone'),
    path('prices/', base, {'name': 'Investment'}, name='investment'),
]