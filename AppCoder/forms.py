from dataclasses import field
from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User






class AnimalFormulario (forms.Form):
    nombre=forms.CharField(required=True)
    especie=forms.CharField(required=True)
    raza=forms.CharField(required=True)
    antecedentes=forms.CharField(required=True)


class ClienteFormulario(forms.Form):
    
    #Especificar los campos
    clientenro=forms.IntegerField
    nombre=forms.CharField(max_length=40)
    apellido=forms.CharField(max_length=40)
    direccion=forms.CharField(max_length=40)
    
class DoctorFormulario(forms.Form):   
    nombre= forms.CharField(max_length=40)
    direccion= forms.CharField(max_length=40)
    especialidad= forms.CharField(max_length=40)
    
class UserRegisterForm(UserCreationForm):
    username=forms.CharField()
    email=forms.EmailField()
    password1=forms.CharField(label="Contraseña",widget=forms.PasswordInput)
    password2=forms.CharField(label="Repetir laContraseña",widget=forms.PasswordInput)
    
    last_name=forms.CharField()
    first_name=forms.CharField()
    image_avatar=forms.ImageField(required=False)
    class Meta:
        model=User
        fields=['username','email','password1','password2','last_name','first_name']
        help_text = {k:"" for k in fields}
        
class UserEditForm(UserCreationForm):
    
    email=forms.EmailField(label="Modificar Email")
    password1=forms.CharField(label="Contraseña",widget=forms.PasswordInput)
    password2=forms.CharField(label="Repetir laContraseña",widget=forms.PasswordInput)
    
    class Meta:
        model=User
        fields=['email','password1','password2']
        help_text = {k:"" for k in fields}
