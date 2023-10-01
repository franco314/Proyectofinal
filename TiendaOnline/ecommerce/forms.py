from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class MouseFormulario(forms.Form):
    articulo = forms.CharField(required=True)
    precio = forms.IntegerField(required=True)
    stock = forms.IntegerField(required=True)

class TecladosFormulario(forms.Form):
    articulo = forms.CharField(required=True)
    precio = forms.IntegerField(required=True)
    stock = forms.IntegerField(required=True)

class MonitoresFormulario(forms.Form):
    articulo = forms.CharField(required=True)
    precio = forms.IntegerField(required=True)
    stock = forms.IntegerField(required=True)

class AuricularesFormulario(forms.Form):
    articulo = forms.CharField(required=True)
    precio = forms.IntegerField(required=True)
    stock = forms.IntegerField(required=True)

class SillasGamerFormulario(forms.Form):
    articulo = forms.CharField(required=True)
    precio = forms.IntegerField(required=True)
    stock = forms.IntegerField(required=True)


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)
 
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k:"" for k in fields}
