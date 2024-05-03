from ..models import Post, Category
from django import forms
from tinymce.widgets import TinyMCE

class NuevoPostForm(forms.ModelForm):
    categoria = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        required=False,
        empty_label="Seleccione la categoría",
        widget=forms.Select(attrs={"class": "form-control"}),
    )
    class Meta:
        model = Post
        fields = [
            "titulo",
            "contenido",
            "descripcion",
            "estado",
            "imagen",
        ]
        labels = {
            "titulo": "Titulo del post",
            "contenido": "Contenido del post",
            "descripcion": "Descripción del post",
            "estado": "Estado",
            "imagen": "Imágen de portada",
        }
        widgets = {
            "titulo": forms.TextInput(
                attrs={
                    "placeholder": "Ingrese titulo del post",
                    "class": "form-control"
                }
            ),
            "contenido": TinyMCE(),
            "descripcion": forms.TextInput(
                attrs={
                    "placeholder": "Ingrese la descripción corta",
                    "class": "form-control"
                }
            ),
            "estado": forms.Select(attrs={"class": "form-control"}),
            "imagen": forms.FileInput(attrs={"class": "form-control"}),
        }