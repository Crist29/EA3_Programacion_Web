from django.urls import path
from rest_api.views import animales,animal

urlpatterns = [
    path('animal/', animales, name='animales'),
    path('animal/<pk>', animal, name="animal"),
]