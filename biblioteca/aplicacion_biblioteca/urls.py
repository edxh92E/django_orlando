from django.urls import path
from . import views

urlpatterns = [
    path('', views.libros_list, name='home'),
    path('listado_libros', views.listado_libros, name='listado_libros'),
    path('detalle_libro/<int:pk>/', views.detalle_libro, name='detalle_libro'),
    path('nuevo_libro', views.nuevo_libro, name='nuevo_libro'),
    path('nuevo_libro/<int:pk>/editar/', views.editar_libro, name='editar_libro'),

]