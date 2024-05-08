from ..models import Category
from django import forms

class NuevaCategoriaForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = [
            "nombre",
            "descripcion",
            "color",
        ]
        labels = {
            "nombre": "Nombre de la categoría",
            "descripcion": "Descripción",
            "color": "Color de la categoría",
        }
        widgets = {
            "nombre": forms.TextInput(
                attrs={
                    "placeholder": "Ingrese nombre de la categoría",
                    "class": "form-control",
                }
            ),
            "descripcion": forms.TextInput(
                attrs={
                    "placeholder": "Ingrese descripción de la categoría",
                    "class": "form-control",
                }
            ),
            "color": forms.TextInput(
                attrs={
                    "placeholder": "Ingrese color de la categoría",
                    "class": "form-control",
                }
            ),
        }