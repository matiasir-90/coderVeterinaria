from typing import List
from urllib import request
from django.http.request import QueryDict
from django.shortcuts import redirect, render, HttpResponse
from django.http import HttpResponse
from AppCoder.models import Animal, Avatar,  Doctor,Cliente
from AppCoder.forms import ClienteFormulario,AnimalFormulario,DoctorFormulario,UserRegisterForm,UserEditForm,AvatarFormulario

from django.urls import reverse_lazy

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required 

# Create your views here.


@login_required
def inicio(request):
      
      diccionario ={}
      cantidadDeAvatares=0
      if request.user.is_authenticated:
            
            avatar=Avatar.objects.filter(user=request.user.id)
            for a in avatar:
                  cantidadDeAvatares=cantidadDeAvatares+1
            diccionario["avatar"]=avatar[cantidadDeAvatares-1].imagen.url
            
      return render(request, "AppCoder/inicio.html",diccionario)



##########################################################################################################################################################################
@login_required
def clientes_agregar(request):
    
      if request.method == 'POST':

            miFormulario = ClienteFormulario(request.POST) #aquí mellega toda la información del html

            print(miFormulario)

            if miFormulario.is_valid:   #Si pasó la validación de Django

                  informacion = miFormulario.cleaned_data

                  cliente = Cliente ( nombre=informacion['nombre'], apellido=informacion['apellido'], direccion=informacion['direccion']) 
              
                  cliente.save()

                  return render(request, "AppCoder/leerClientes.html") #Vuelvo al inicio o a donde quieran

      else: 

            miFormulario= ClienteFormulario() #Formulario vacio para construir el html

      return render(request, "AppCoder/clientes_agregar.html", {"miFormulario":miFormulario})
@login_required
def leerClientes(request):
    
      clientes = Cliente.objects.all() #trae todos los Cliente

      contexto= {"clientes":clientes} 

      return render(request, "AppCoder/leerClientes.html",contexto)

@login_required
def eliminarCliente(request, cliente_nro):

      clientes = Cliente.objects.get(nombre=cliente_nro)
      clientes.delete()
      
      #vuelvo al menú
      cliente = Cliente.objects.all() #trae todos los profesores

      contexto= {"clientes":cliente} 

      return render(request, "AppCoder/leerClientes.html",contexto)
@login_required
def editarCliente(request, cliente_nro):
    
      #Recibe el nombre del profesor que vamos a modificar
      cliente = Cliente.objects.get(nombre=cliente_nro)

      #Si es metodo POST hago lo mismo que el agregar
      if request.method == 'POST':

            miFormulario = ClienteFormulario(request.POST) #aquí mellega toda la información del html

            print(miFormulario)

            if miFormulario.is_valid:   #Si pasó la validación de Django

                  informacion = miFormulario.cleaned_data

                  cliente.nombre = informacion['nombre']
                  cliente.apellido = informacion['apellido']
                  cliente.direccion = informacion['direccion']

                  cliente.save()

                  return render(request, "AppCoder/clientes.html") #Vuelvo al inicio o a donde quieran
      #En caso que no sea post
      else: 
            #Creo el formulario con los datos que voy a modificar
            miFormulario= ClienteFormulario(initial={'nombre': cliente.nombre, 'apellido':cliente.apellido , 
            'direccion':cliente.direccion}) 

      #Voy al html que me permite editar
      return render(request, "AppCoder/editarCliente.html", {"miFormulario":miFormulario, "cliente_nro":cliente_nro})

def buscarClientes(request):
    
      if  request.GET["nombre"]:

	      #respuesta = f"Estoy buscando la camada nro: {request.GET['camada'] }" 
            nombre = request.GET['nombre'] 
            clientes = Cliente.objects.filter(nombre__icontains=nombre)

            return render(request, "AppCoder/clientes.html", {"clientes":clientes, "nombre":nombre})

      else: 

	      respuesta = "No enviaste datos"
      #No olvidar from django.http import HttpResponse
      return HttpResponse(respuesta)

def clientes(request):
    
      if request.method == 'POST':

            miFormulario = ClienteFormulario(request.POST) #aquí mellega toda la información del html

            print(miFormulario)

            if miFormulario.is_valid:   #Si pasó la validación de Django

                  informacion = miFormulario.cleaned_data

                  cliente = Cliente ( nombre=informacion['nombre'], apellido=informacion['apellido'], direccion=informacion['direccion']) 
              
                  cliente.save()

                  return render(request, "AppCoder/leerClientes.html") #Vuelvo al inicio o a donde quieran

      else: 

            miFormulario= ClienteFormulario() #Formulario vacio para construir el html

      return render(request, "AppCoder/clientes.html", {"miFormulario":miFormulario})

#########################################################################################################################################################################################

def animales(request):
    
      if request.method == 'POST':

            miFormulario = AnimalFormulario(request.POST) #aquí mellega toda la información del html

            print(miFormulario)

            if miFormulario.is_valid:   #Si pasó la validación de Django

                  informacion = miFormulario.cleaned_data

                  animal = Animal ( nombre=informacion['nombre'], especie=informacion['especie'], raza=informacion['raza'],antecedentes=informacion['antecedentes']) 
              
                  animal.save()

                  return render(request, "AppCoder/leerAnimales.html") #Vuelvo al inicio o a donde quieran

      else: 

            miFormulario= AnimalFormulario() #Formulario vacio para construir el html

      return render(request, "AppCoder/animales.html", {"miFormulario":miFormulario})
@login_required
def animales_agregar(request):
    
      if request.method == 'POST':

            miFormulario = AnimalFormulario(request.POST) #aquí mellega toda la información del html

            print(miFormulario)

            if miFormulario.is_valid:   #Si pasó la validación de Django

                  informacion = miFormulario.cleaned_data

                  animal = Animal ( nombre=informacion['nombre'], especie=informacion['especie'], raza=informacion['raza'],antecedentes=informacion['antecedentes']) 
              
                  animal.save()

                  return render(request, "AppCoder/leerAnimales.html") #Vuelvo al inicio o a donde quieran

      else: 

            miFormulario= AnimalFormulario() #Formulario vacio para construir el html

      return render(request, "AppCoder/animales_agregar.html", {"miFormulario":miFormulario})
@login_required
def leerAnimales(request):
    
      animales = Animal.objects.all() #trae todos los Cliente

      contexto= {"animales":animales} 

      return render(request, "AppCoder/leerAnimales.html",contexto)

@login_required
def eliminarAnimal(request, animal_nro):

      animales = Animal.objects.get(nombre=animal_nro)
      animales.delete()
      
      #vuelvo al menú
      animal = Animal.objects.all() #trae todos los profesores

      contexto= {"animales":animal} 

      return render(request, "AppCoder/leerAnimales.html",contexto)
@login_required
def editarAnimal(request, animal_nro):
    
      #Recibe el nombre del profesor que vamos a modificar
      animal = Animal.objects.get(nombre=animal_nro)

      #Si es metodo POST hago lo mismo que el agregar
      if request.method == 'POST':

            miFormulario = AnimalFormulario(request.POST) #aquí mellega toda la información del html

            print(miFormulario)

            if miFormulario.is_valid:   #Si pasó la validación de Django

                  informacion = miFormulario.cleaned_data

                  animal.nombre = informacion['nombre']
                  animal.especie = informacion['especie']
                  animal.raza = informacion['raza']
                  animal.antecedentes = informacion['antecedentes']
                  

                  animal.save()

                  return render(request, "AppCoder/leerAnimales.html") #Vuelvo al inicio o a donde quieran
      #En caso que no sea post
      else: 
            #Creo el formulario con los datos que voy a modificar
            miFormulario= AnimalFormulario(initial={'nombre': animal.nombre, 'especie':animal.especie , 'raza':animal.raza,'antecedentes':animal.antecedentes}) 

      #Voy al html que me permite editar
      return render(request, "AppCoder/editarAnimal.html", {"miFormulario":miFormulario, "nombre":animal_nro})


def buscarAnimales(request):
    
      if  request.GET["nombre"]:

	      #respuesta = f"Estoy buscando la camada nro: {request.GET['camada'] }" 
            nombre = request.GET['nombre'] 
            animales = Animal.objects.filter(nombre__icontains=nombre)

            return render(request, "AppCoder/animales.html", {"animales":animales, "nombre":nombre})

      else: 

	      respuesta = "No enviaste datos"
      #No olvidar from django.http import HttpResponse
      return HttpResponse(respuesta)

######################################################################################################################################################


def doctores(request):
    
      if request.method == 'POST':

            miFormulario = DoctorFormulario(request.POST) #aquí mellega toda la información del html

            print(miFormulario)

            if miFormulario.is_valid:   #Si pasó la validación de Django

                  informacion = miFormulario.cleaned_data

                  doctor = Doctor(nombre=informacion['nombre'],direccion=informacion['direccion'], especialidad=informacion['especialidad']) 
                  doctor.save()

                  return render(request, "AppCoder/leerDoctores.html") #Vuelvo al inicio o a donde quieran

      else: 

            miFormulario= DoctorFormulario() #Formulario vacio para construir el html

      return render(request, "AppCoder/doctores.html", {"miFormulario":miFormulario})
@login_required
def leerDoctores(request):
    
      doctores = Doctor.objects.all() #trae todos los Cliente

      contexto= {"doctores":doctores} 

      return render(request, "AppCoder/leerDoctores.html",contexto)

@login_required
def eliminarDoctor(request, doctor_nro):

      doctor = Doctor.objects.get(nombre=doctor_nro)
      doctor.delete()
      
      #vuelvo al menú
      doctor = Doctor.objects.all() #trae todos los profesores

      contexto= {"doctores":doctor} 

      return render(request, "AppCoder/leerDoctores.html",contexto)
@login_required
def editarDoctor(request, doctor_nro):
    
      #Recibe el nombre del profesor que vamos a modificar
      doctor = Doctor.objects.get(nombre=doctor_nro)

      #Si es metodo POST hago lo mismo que el agregar
      if request.method == 'POST':

            miFormulario = DoctorFormulario(request.POST) #aquí mellega toda la información del html

            print(miFormulario)

            if miFormulario.is_valid:   #Si pasó la validación de Django

                  informacion = miFormulario.cleaned_data

                  doctor.nombre = informacion['nombre']
                  doctor.direccion = informacion['direccion']
                  doctor.especialidad = informacion['especialidad']
    
                  doctor.save()

                  return render(request, "AppCoder/leerDoctores.html") #Vuelvo al inicio o a donde quieran
      #En caso que no sea post
      else: 
            #Creo el formulario con los datos que voy a modificar
            miFormulario= DoctorFormulario(initial={'nombre': doctor.nombre,'direccion':doctor.direccion,'especialidad':doctor.especialidad}) 

      #Voy al html que me permite editar
      
      return render(request, "AppCoder/editarDoctor.html", {"miFormulario":miFormulario, "nombre":doctor_nro})

def buscarDoctores(request):
    
      if  request.GET["nombre"]:

	      #respuesta = f"Estoy buscando la camada nro: {request.GET['camada'] }" 
            nombre = request.GET['nombre'] 
            doctores = Doctor.objects.filter(nombre__icontains=nombre)

            return render(request, "AppCoder/doctores.html", {"doctores":doctores, "nombre":nombre})

      else: 

	      respuesta = "No enviaste datos"
      #No olvidar from django.http import HttpResponse
      return HttpResponse(respuesta)
@login_required
def doctores_agregar(request):
    
      if request.method == 'POST':

            miFormulario = DoctorFormulario(request.POST) #aquí mellega toda la información del html

            print(miFormulario)

            if miFormulario.is_valid:   #Si pasó la validación de Django

                  informacion = miFormulario.cleaned_data

                  doctor = Doctor(nombre=informacion['nombre'],direccion=informacion['direccion'], especialidad=informacion['especialidad']) 
                  doctor.save()

                  return render(request, "AppCoder/leerDoctores.html") #Vuelvo al inicio o a donde quieran

      else: 

            miFormulario= DoctorFormulario() #Formulario vacio para construir el html

      return render(request, "AppCoder/doctores_agregar.html", {"miFormulario":miFormulario})
######################################################################################################################################################

def login_request(request):
      if request.method== "POST":
            form =AuthenticationForm(request,data=request.POST)
            
            if form.is_valid():
                  usuario= form.cleaned_data.get('username')
                  contra= form.cleaned_data.get('password')
                  
                  user= authenticate(username=usuario,password=contra)
                  
                  if user is not None:
                        login (request,user)
                        return render(request,"Appcoder/inicio.html",{"mensaje":f"{usuario}"})
                  else:
                        return render(request,"Appcoder/inicio.html",{"mensaje":"datos incorrectos"})
            else:
                  return render(request,"Appcoder/inicio.html",{"mensaje":f"formulario erroneo"})
      form=AuthenticationForm()
      
      return render(request,"Appcoder/login.html",{'form':form})

def register(request):
      if request.method =='POST':
            form= UserRegisterForm(request.POST)
            if form.is_valid():
                  username= form.cleaned_data['username']
                  form.save()
                  return render(request,"AppCoder/inicio.html",{"mensaje":"Usuario Creado"})
      else:
            form=UserRegisterForm()
      return render(request,"Appcoder/register.html",{"form":form})

@login_required
def editarPerfil(request):
      usuario = request.user
      if request.method=='POST':
            miFormulario=UserEditForm(request.POST)
            if  miFormulario.is_valid():
                  information= miFormulario.cleaned_data
                  usuario.email=information['email']
                  usuario.password1=information['password1']
                  usuario.password2=information['password2']

                  usuario.save()
                  
                  return render(request,"Appcoder/inicio.html")
      else:
            miFormulario = UserEditForm(initial={'email':usuario.email})
      
      return render(request,"AppCoder/editarPerfil.html",{"miFormulario":miFormulario,"usuario":usuario})


@login_required
def agregarAvatar(request):
      if request.method=='POST':
            miFormulario=AvatarFormulario(request.POST,request.FILES)
            
            if miFormulario.is_valid():
                  u= User.objects.get(username=request.user)
                  avatar=Avatar(user=u, imagen=miFormulario.cleaned_data['imagen'])
                  avatar.save()
                  
                  return render(request,"AppCoder/inicio.html")
      else:
            miFormulario=AvatarFormulario()
      return render(request,"AppCoder/agregarAvatar.html",{"miformulario":miFormulario})