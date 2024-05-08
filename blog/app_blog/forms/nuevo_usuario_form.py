from ..models import CustomUser
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class NuevoUsuarioForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            'username',
            'password1',
            'password2',
        )
        labels = {
            "username": "Nombre de usuario",
            "password1": "Contraseña",
            "password2": "Repetir contraseña",
        }
        widgets = {
            "username": forms.TextInput(
                attrs={
                    "placeholder": "Ingrese su nombre de usuario",
                }
            ),
            "password1": forms.PasswordInput(
                attrs={
                    "placeholder": "Ingrese su contraseña",
                    "class": "form-control"
                }
            ),
            "password2": forms.PasswordInput(
                attrs={
                    "placeholder": "Repita su contraseña",
                    "class": "form-control"
                }
            ),
        }
