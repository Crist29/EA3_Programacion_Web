from django.urls import path
from rest_api.views import animales,animal
from .viewsLogin import login

urlpatterns = [
    path('animal/', animales, name='animales'),
    path('animal/<pk>', animal, name="animal"),
    path('login/', login, name='login'),
]