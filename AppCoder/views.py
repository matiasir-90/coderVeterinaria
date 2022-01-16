from typing import List
from django.http.request import QueryDict
from django.shortcuts import redirect, render, HttpResponse
from django.http import HttpResponse
from AppCoder.models import Curso, Profesor,Cliente
from AppCoder.forms import CursoFormulario, ProfesorFormulario,ClienteFormulario

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy



# Create your views here.

def curso(request):

      curso =  Curso(nombre="Desarrollo web", camada="19881")
      curso.save()
      documentoDeTexto = f"--->Curso: {curso.nombre}   Camada: {curso.camada}"


      return HttpResponse(documentoDeTexto)


def inicio(request):

      return render(request, "AppCoder/inicio.html")



def estudiantes(request):

      return render(request, "AppCoder/estudiantes.html")


def entregables(request):

      return render(request, "AppCoder/entregables.html")


def cursos(request):

      if request.method == 'POST':

            miFormulario = CursoFormulario(request.POST) #aquí mellega toda la información del html

            print(miFormulario)

            if miFormulario.is_valid:   #Si pasó la validación de Django

                  informacion = miFormulario.cleaned_data

                  curso = Curso (nombre=informacion['curso'], camada=informacion['camada']) 

                  curso.save()

                  return render(request, "AppCoder/inicio.html") #Vuelvo al inicio o a donde quieran

      else: 

            miFormulario= CursoFormulario() #Formulario vacio para construir el html

      return render(request, "AppCoder/cursos.html", {"miFormulario":miFormulario})




def profesores(request):

      if request.method == 'POST':

            miFormulario = ProfesorFormulario(request.POST) #aquí mellega toda la información del html

            print(miFormulario)

            if miFormulario.is_valid:   #Si pasó la validación de Django

                  informacion = miFormulario.cleaned_data

                  profesor = Profesor (nombre=informacion['nombre'], apellido=informacion['apellido'],
                   email=informacion['email'], profesion=informacion['profesion']) 

                  profesor.save()

                  return render(request, "AppCoder/inicio.html") #Vuelvo al inicio o a donde quieran

      else: 

            miFormulario= ProfesorFormulario() #Formulario vacio para construir el html

      return render(request, "AppCoder/profesores.html", {"miFormulario":miFormulario})






def buscar(request):

      if  request.GET["camada"]:

	      #respuesta = f"Estoy buscando la camada nro: {request.GET['camada'] }" 
            camada = request.GET['camada'] 
            cursos = Curso.objects.filter(camada__icontains=camada)

            return render(request, "AppCoder/inicio.html", {"cursos":cursos, "camada":camada})

      else: 

	      respuesta = "No enviaste datos"
      #No olvidar from django.http import HttpResponse
      return HttpResponse(respuesta)

def leerProfesores(request):

      profesores = Profesor.objects.all() #trae todos los profesores

      contexto= {"profesores":profesores} 

      return render(request, "AppCoder/leerProfesores.html",contexto)



def eliminarProfesor(request, profesor_nombre):

      profesor = Profesor.objects.get(nombre=profesor_nombre)
      profesor.delete()
      
      #vuelvo al menú
      profesores = Profesor.objects.all() #trae todos los profesores

      contexto= {"profesores":profesores} 

      return render(request, "AppCoder/leerProfesores.html",contexto)



def editarProfesor(request, profesor_nombre):

      #Recibe el nombre del profesor que vamos a modificar
      profesor = Profesor.objects.get(nombre=profesor_nombre)

      #Si es metodo POST hago lo mismo que el agregar
      if request.method == 'POST':

            miFormulario = ProfesorFormulario(request.POST) #aquí mellega toda la información del html

            print(miFormulario)

            if miFormulario.is_valid:   #Si pasó la validación de Django

                  informacion = miFormulario.cleaned_data

                  profesor.nombre = informacion['nombre']
                  profesor.apellido = informacion['apellido']
                  profesor.email = informacion['email']
                  profesor.profesion = informacion['profesion']

                  profesor.save()

                  return render(request, "AppCoder/inicio.html") #Vuelvo al inicio o a donde quieran
      #En caso que no sea post
      else: 
            #Creo el formulario con los datos que voy a modificar
            miFormulario= ProfesorFormulario(initial={'nombre': profesor.nombre, 'apellido':profesor.apellido , 
            'email':profesor.email, 'profesion':profesor.profesion}) 

      #Voy al html que me permite editar
      return render(request, "AppCoder/editarProfesor.html", {"miFormulario":miFormulario, "profesor_nombre":profesor_nombre})




class CursoList(ListView):

      model = Curso 
      template_name = "AppCoder/cursos_list.html"



class CursoDetalle(DetailView):

      model = Curso
      template_name = "AppCoder/curso_detalle.html"



class CursoCreacion(CreateView):

      model = Curso
      success_url = "/AppCoder/curso/list"
      fields = ['nombre', 'camada']


class CursoUpdate(UpdateView):

      model = Curso
      success_url = "/AppCoder/curso/list"
      fields  = ['nombre', 'camada']


class CursoDelete(DeleteView):

      model = Curso
      success_url = "/AppCoder/curso/list"


class ClienteList(ListView):
    model = Cliente
    template_name="/AppCoder/cliente_list.html"

class ClienteDetalle(DetailView):
    model = Cliente
    template_name="/AppCoder/cliente_detalle.html"

#class ClienteCreacion(CreateView)
def cliente(request):
    
      cliente =  Cliente(nombre="Desarrollo web", camada="19881")
      cliente.save()
      documentoDeTexto = f"--->Cliente nombre: {clientes.nombre}   Cliente apellido: {clientes.apellido} Cliente direccion: {clientes.direccion}"

      return HttpResponse(documentoDeTexto)

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

def leerClientes(request):
    
      clientes = Cliente.objects.all() #trae todos los Cliente

      contexto= {"clientes":clientes} 

      return render(request, "AppCoder/leerClientes.html",contexto)


def eliminarCliente(request, cliente_nro):

      clientes = Cliente.objects.get(nombre=cliente_nro)
      clientes.delete()
      
      #vuelvo al menú
      cliente = Cliente.objects.all() #trae todos los profesores

      contexto= {"clientes":cliente} 

      return render(request, "AppCoder/leerClientes.html",contexto)

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

                  return render(request, "AppCoder/leerClientes.html") #Vuelvo al inicio o a donde quieran
      #En caso que no sea post
      else: 
            #Creo el formulario con los datos que voy a modificar
            miFormulario= ClienteFormulario(initial={'nombre': cliente.nombre, 'apellido':cliente.apellido , 
            'direccion':cliente.direccion}) 

      #Voy al html que me permite editar
      return render(request, "AppCoder/editarCliente.html", {"miFormulario":miFormulario, "cliente_nro":cliente_nro})




class ClienteCreacion(CreateView):
    model = Cliente
    success_url = "../cliente/list"
    fields = ["clientenro","nombre","apellido","direccion"]

class ClienteUpdate(UpdateView):
    model = Cliente
    success_url = "../cliente/list"
    fields = ["clientenro","nombre","apellido","direccion"]
    
class ClienteDelete(DeleteView):
    model = Cliente
    success_url = "../cliente/list"
