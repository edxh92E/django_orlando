from django import forms
from .models import Libro

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