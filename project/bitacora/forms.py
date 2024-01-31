from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from . import models

class PerfilForm(forms.ModelForm):
    class Meta:
        model = models.Perfil
        fields = "__all__"
        model.user = User

class ViajeForm(forms.ModelForm):
    class Meta:
        model = models.Viaje
        fields = "__all__"
