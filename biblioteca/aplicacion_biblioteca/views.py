from django.shortcuts import render, get_object_or_404
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

def detalle_libro(request, pk):
    libro = get_object_or_404(Libro, pk=pk)
    return render(request, 'libros/detalle_libro.html', {'libro': libro})