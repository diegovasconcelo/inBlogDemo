from django import forms
from django.core import validators
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields=['username','email','first_name','last_name','password1','password2']

    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Nombre de usuario', 'class': 'form-control border-primary',}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'placeholder': 'Correo electrónico', 'class': 'form-control border-primary'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Nombre', 'class': 'form-control border-primary',}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Apellido', 'class': 'form-control border-primary',}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Contraseña', 'class': 'form-control border-primary',}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirme contraseña', 'class': 'form-control border-primary',}))


