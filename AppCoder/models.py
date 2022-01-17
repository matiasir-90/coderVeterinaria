from django.db import models

# Create your models here.
class Curso(models.Model):

    nombre=models.CharField(max_length=40)
    camada = models.IntegerField()

    def __str__(self):
        return f"Curso: {self.nombre} - Camada: {self.camada}"


class Estudiante(models.Model):
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    email= models.EmailField()

class Profesor(models.Model):
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    email= models.EmailField()
    profesion= models.CharField(max_length=30)


    def __str__(self):
        return f"Nombre: {self.nombre} - Apellido {self.apellido} - E-Mail {self.email} - Profesión {self.profesion}"

class Entregable(models.Model):
    nombre= models.CharField(max_length=30)
    fechaDeEntrega = models.DateField()  
    entregado = models.BooleanField()


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
    
    
    