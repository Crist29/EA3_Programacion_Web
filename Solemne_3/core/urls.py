from django.urls import path, include
from core.views import views_animal, add_animal, delete_animal, edit_animal 
from core.views import home

urlpatterns = [
     path('', home, name="home"),
     path('agregar_animal/', add_animal, name="add_animal" ),
     path('editar_animal/<pk>', edit_animal, name="edit_animal" ),
     path('eliminar_animal/<pk>', delete_animal, name="delete_animal" ),
     path('views_animal/', views_animal, name="views_animal")
]