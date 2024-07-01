from django.forms import ModelForm
from .models import Formulario
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import gettext_lazy as _

class RegistroForm(ModelForm):
    class Meta:
        model = Formulario
        fields = ['nombre', 'apellido', 'correo', 'numero', 'rut', 'contrasena']


class CustomAuthenticationForm(AuthenticationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese correo electrónico'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Contraseña...'}))