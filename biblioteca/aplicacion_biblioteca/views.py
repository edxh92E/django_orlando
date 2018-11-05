from django.shortcuts import render
from django.utils import timezone
from .models import Libro

# Create your views here.
def libros_list(request):
    libros = Libro.objects.all()
    # print(libros)
    return render(request, 'libros/libros_list_home.html', {'listado_libros': libros })

def listado_libros(request):
    libros = Libro.objects.all()
    return render(request, 'libros/listado_libros.html', {'listado_libros': libros })