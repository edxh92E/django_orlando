from django import forms
from .models import Libro, LibroUsuario
from django.forms.fields import DateField

BIRTH_YEAR_CHOICES = ('1980', '1981', '1982')

class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ['titulo', 'descripcion','categoria', 'fecha_publicacion']
        widgets = {
            'titulo': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'libro de ejemplo'}),
            'descripcion': forms.Textarea(attrs={'class':'form-control', 'placeholder': 'escribe una breve descripcion del libro', 'rows': 6 }),
            'categoria': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'categoria de ejemplo'}),
            'fecha_publicacion': forms.TextInput(attrs={'class':'form-control', 'placeholder': '2018-01-02'}) 
        }

class PrestarLibro(forms.ModelForm):
    class Meta:
        model = LibroUsuario
        fields = ['comentario','fecha_prestada','fecha_devolucion','usuario','libro']
        widgets = {
            'comentario':forms.Textarea(attrs={'class':'form-control', 'rows': 6}),
            'fecha_prestada': forms.TextInput(attrs={'class':'form-control', 'placeholder': '2018-01-02'}), 
            'fecha_devolucion':forms.TextInput(attrs={'class':'form-control', 'placeholder': '2018-01-02'}),
        }