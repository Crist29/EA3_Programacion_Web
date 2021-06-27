from django import forms
from django.forms import ModelForm
from .models import Animal

#formulario para crear (y editar) animal
class AnimalForm(ModelForm):

    class Meta:
        model = Animal
        fields = ['nFicha','nombre','edad','especie','categoria']