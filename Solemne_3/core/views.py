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

#formularo para crear animal
def add_animal(request):
    datos = {
        'form': AnimalForm() 
        }
    if request.method == 'POST':
        formulario_add = AnimalForm(request.POST)
        if formulario_add.is_valid:
            formulario_add.save()
            datos['mensaje'] = "Animal agregado correctamente"

    return render(request, 'core/add_animal.html', datos)