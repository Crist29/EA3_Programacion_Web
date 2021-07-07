from rest_framework import serializers
from core.models import Animal

class AnimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Animal
        fields = ['nFicha', 'nombre', 'edad','especie', 'categoria']