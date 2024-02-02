from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from . import models

class PerfilForm(forms.ModelForm):
    class Meta:
        model = models.Perfil
        fields = "__all__"
        widgets = {
            'user': forms.TextInput(attrs={'type': 'hidden'}),
#            'nombre': forms.TextInput(attrs={'value': 'Nombre Hardcodeado'}),
        }


class ViajeForm(forms.ModelForm):
    class Meta:
        model = models.Viaje
        fields = "__all__"
        widgets = {
            'perfil': forms.TextInput(attrs={'type': 'hidden'}),
        }
