from django import forms


class CursoFormulario(forms.Form):

    #Especificar los campos
    curso = forms.CharField()
    camada = forms.IntegerField()


class ProfesorFormulario(forms.Form):   
    nombre= forms.CharField(max_length=30)
    apellido= forms.CharField(max_length=30)
    email= forms.EmailField()
    profesion= forms.CharField(max_length=30)

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