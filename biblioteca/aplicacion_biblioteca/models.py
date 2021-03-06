from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib import admin

class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    categoria = models.CharField(max_length=100)
    descripcion = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    fecha_publicacion = models.DateTimeField(blank=True, null=True)
    usuario   = models.ManyToManyField(User, through='DetallePrestado')
    
    def publicacion(self):
        self.fecha_publicacion = timezone.now()
        self.save()

    def __str__(self):
        return self.titulo

class LibroUsuario(models.Model):
    comentario = models.TextField()
    fecha_prestada = models.DateTimeField(default=timezone.now)
    fecha_devolucion = models.DateTimeField(blank=True, null=True)
    usuario = models.ManyToManyField(User)
    libro = models.ManyToManyField(Libro)

    def __str__(self):
         return self.comentario

class DetallePrestado(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)

class DetallePrestadoInLine(admin.TabularInline):
    model = DetallePrestado
    extra = 1

class UserAdmin(admin.ModelAdmin):
    inlines = (DetallePrestadoInLine,)

class LibroAdmin (admin.ModelAdmin):
    inlines = (DetallePrestadoInLine,)