from django.urls import path
from . import views

urlpatterns = [
    path('', views.libros_list, name='home'),
    path('listado_libros', views.listado_libros, name='listado_libros'),
]