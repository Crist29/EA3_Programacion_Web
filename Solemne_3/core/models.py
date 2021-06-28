from django.db import models

class Categoria(models.Model):
    idCategoria = models.IntegerField(primary_key=True, verbose_name="Id categoria")
    nombreCategoria = models.CharField(max_length=50, verbose_name="Nombre categoria")

    def __str__(self):
        return self.nombreCategoria

class Animal(models.Model):
    nFicha = models.AutoField(primary_key = True, verbose_name="Numero de ficha") # Campo autoincremental.
    #nFicha = models.CharField(max_length=6,primary_key=True, verbose_name="Numero de Ficha")
    nombre = models.CharField(max_length=20, verbose_name="Nombre" )
    edad = models.CharField(max_length=20, null=True, blank=True, verbose_name="Edad")
    especie = models.CharField(max_length=20, null=True, blank=True, verbose_name="Especie")
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.nFicha
