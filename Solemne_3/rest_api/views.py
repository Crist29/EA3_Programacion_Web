from django.shortcuts import render
from .serializers import AnimalSerializer
from core.models import Animal
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view

@api_view(['GET', 'POST'])
def animales(request):
    """
    Lista todos los animales
    """
    if request.method == 'GET':
        animales_lista = Animal.objects.all()
        serializer = AnimalSerializer(animales_lista, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        """
        Agrega un animal
        """
        data = JSONParser().parse(request)
        serializer = AnimalSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

