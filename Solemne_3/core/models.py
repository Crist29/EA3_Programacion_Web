from django.db import models

class Categoria(models.Model):
    idCategoria = models.IntegerField(primary_key=True, verbose_name="Id categoria")
    nombreCategoria = models.CharField(max_length=50, verbose_name="Nombre categoria")

    def _str_(self):
        return self.nombreCategoria
