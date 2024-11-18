from django import forms
from . import models
from django.forms import Textarea


class CrearAnuncio(forms.ModelForm):
    class Meta:
        model = models.Anuncio
        fields = ['titulo', 'cuerpo', 'imagen', 'tipo']
        widgets = {
            'cuerpo': Textarea(attrs={
                'style': 'resize: none;',
                'placeholder': 'Ingrese Detalle de Anuncio',
                'class': 'miClase'
            })
        }
