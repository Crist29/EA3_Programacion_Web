from django.urls import path
from rest_api.views import animales

urlpatterns = [
    path('animal/', animales, name='animales'),
]