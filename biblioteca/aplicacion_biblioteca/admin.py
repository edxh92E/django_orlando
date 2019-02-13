from django.contrib import admin
from .models import Libro, LibroUsuario, DetallePrestado

# Register your models here.
admin.site.register(Libro)
admin.site.register(LibroUsuario)
admin.site.register(DetallePrestado)
