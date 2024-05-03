from ..models import Comment
from django import forms
from tinymce.widgets import TinyMCE

class CommentForm(forms.ModelForm):
    class Meta():
        model = Comment
        fields = [
            "contenido",
        ]
        labels = {
            "contenido": "Deja tu comentario",
        }
        widgets = {
            "contenido": TinyMCE(),
        }