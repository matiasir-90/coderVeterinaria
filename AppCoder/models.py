from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Veterinaria (models.Model):
    nombre=models.CharField(max_length=40)
    direccion=models.CharField(max_length=40)
    encargado=models.CharField(max_length=40)
    capacidad=models.IntegerField
    ocupacion=models.IntegerField
    
class Cliente (models.Model):
    clientenro=models.IntegerField
    nombre=models.CharField(max_length=40)
    apellido=models.CharField(max_length=40)
    direccion=models.CharField(max_length=40)
    def __str__(self):
        return f"Nombre: {self.nombre} - Apellido {self.apellido} - Dirección {self.direccion} "
    
class Animal (models.Model):
    nombre=models.CharField(max_length=40)
    especie=models.CharField(max_length=40)
    raza=models.CharField(max_length=40)
    antecedentes=models.CharField(max_length=500)
    def __str__(self):
        return f"Nombre: {self.nombre} - especie: {self.especie} - raza: {self.raza} - antecedentes: {self.antecedentes} "
    
class Doctor (models.Model):
    nombre=models.CharField(max_length=40)
    direccion=models.CharField(max_length=40)
    especialidad=models.CharField(max_length=40)
    def __str__(self):
        return f"Nombre: {self.nombre} - direccion: {self.direccion} - especialidad: {self.especialidad} "

class Avatar (models.Model):
    user= models.ForeignKey(User,on_delete=models.CASCADE)
    imagen=models.ImageField(upload_to='avatares',null=True,blank=True)
    