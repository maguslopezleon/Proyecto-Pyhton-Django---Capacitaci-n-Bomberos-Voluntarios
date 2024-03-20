from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class CursoForm(forms.Form):
    nombre = forms.CharField(max_length=50, required=True)
    tipo = forms.CharField(max_length=50, required=True)
    mes = forms.CharField(max_length=50, required=True)
    anio = forms.IntegerField()


class ProfesorForm(forms.Form):
    nombre = forms.CharField(max_length=50, required=True)
    apellido = forms.CharField(max_length=50, required=True)
    email = forms.EmailField()
    jerarquia = forms.CharField(max_length=50, required=True)
    cuartel = forms.CharField(max_length=50, required=True)


class CarteleraForm(forms.Form):
    titulo = forms.CharField(max_length=50, required=True)
    subtitulo = forms.CharField(max_length=50, required=True)
    autor = forms.CharField(max_length=50, required=True)
    novedad = forms.CharField(max_length=200, required=True)


class CuerpoForm(forms.Form):
    nombre = forms.CharField(max_length=50, required=True)
    apellido = forms.CharField(max_length=50, required=True)
    jerarquia = forms.CharField(max_length=50, required=True)
    email = forms.EmailField()
    legajo = forms.IntegerField()


class RegistroForm(UserCreationForm): 
    email = forms.EmailField(required=True)   
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirma Contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class UserEditForm(UserChangeForm): 
    email = forms.EmailField(required=True)   
    first_name = forms.CharField(label="Nombre", max_length=50, required=True)
    last_name = forms.CharField(label="Apellido", max_length=50, required=True)

    class Meta:
        model = User
        fields = ["email", "first_name", "last_name"]  


class AvatarForm(forms.Form):
    imagen = forms.ImageField(required=True)
   

