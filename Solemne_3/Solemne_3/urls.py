"""Solemne_3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from core.views import views_animal, add_animal, delete_animal, edit_animal, home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('agregar_animal/', add_animal, name="add_animal" ),
    path('editar_animal/<pk>', edit_animal, name="edit_animal" ),
    path('eliminar_animal/<pk>', delete_animal, name="delete_animal" ),
    path('views_animal/', views_animal, name="views_animal")
]