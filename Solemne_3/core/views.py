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

    #formulario para editar animal
def edit_animal(request, pk):
    animal = Animal.objects.get(nFicha=pk)
    datos = {
        'form': AnimalForm(instance=animal)
    }
    if request.method == 'POST':
        formulario_edit = AnimalForm(data=request.POST, instance=animal)
        if formulario_edit.is_valid:
            formulario_edit.save()
            datos['mensaje'] = "Animal editado correctamente"
    return render(request, 'core/edit_animal.html', datos)

#formulario para eliminar animal
def delete_animal(request, pk):
    animal = Animal.objects.get(nFicha=pk)
    animal.delete()
    return redirect(to="views_animal")

def home(request):

    return render(request, 'core/home.html')