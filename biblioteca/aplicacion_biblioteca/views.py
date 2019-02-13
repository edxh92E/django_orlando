from .models import Libro, LibroUsuario, DetallePrestado
from .forms import LibroForm, PrestarLibro, LibroUserForm
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect


# Create your views here.
def libros_list(request):
    libros = Libro.objects.all()
    return render(request, 'libros/libros_list_home.html', {'listado_libros': libros })

def listado_libros(request):
    libros = Libro.objects.all()
    return render(request, 'libros/listado_libros.html', {'listado_libros': libros })

def detalle_libro(request, pk):
    libro = get_object_or_404(Libro, pk=pk)
    usuarios = DetallePrestado.objects.filter(libro_id = pk)
    return render(request, 'libros/detalle_libro.html', {'libro': libro, 'usuarios': usuarios})

@login_required
def nuevo_libro(request):
    if request.method == "POST":
        form = LibroForm(request.POST)
        if form.is_valid():
            libro = form.save(commit=False)
            libro.save()
            return redirect('detalle_libro', pk=libro.pk)
    else:
        form = LibroForm()
    return render(request, 'libros/nuevo_libro.html', {'form': form})

@login_required
def editar_libro(request, pk):
    libro = get_object_or_404(Libro, pk=pk)
    if request.method == "POST":
        form = LibroForm(request.POST, instance=libro)
        if form.is_valid():
            libro = form.save(commit=False)
            libro.save()
            return redirect('detalle_libro', pk=libro.pk)
    else:
        form = LibroForm(instance=libro)
    return render(request, 'libros/nuevo_libro.html', {'form': form})

# def prestar_libro(request):
def prestar_libro(request):
    if request.method == "POST":
        form = LibroUserForm(request.POST)
        if form.is_valid():
            libro_us = Libro.objects.create(titulo=form.cleaned_data['titulo'], descripcion = form.cleaned_data['descripcion'], categoria = form.cleaned_data['categoria'],fecha_publicacion = form.cleaned_data['fecha_publicacion'])
            for usuario_id in request.POST.getlist('usuario'):
                detalle = DetallePrestado(usuario_id=usuario_id, libro_id = libro_us.id)
                detalle.save()
            return redirect('detalle_libro', pk=libro_us.pk)
    else:
        form = LibroUserForm()
    return render(request, 'libro_usuario/libro_usuario.html', {'form': form})

