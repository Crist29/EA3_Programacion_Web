from django.shortcuts import render
from django.http import request
from django.shortcuts import render, redirect
from .models import Animal
from .forms import AnimalForm

#listado de Animales
def views_animal(request):
    animales = Animal.objects.all()
    datos = {
        'animales' : animales
    }
    return render(request, 'core/views_animal.html', datos)