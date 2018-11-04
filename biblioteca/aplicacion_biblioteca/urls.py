from django.urls import path
from . import views

urlpatterns = [
    path('', views.libros_list, name='libros_list')
]