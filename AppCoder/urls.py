from django.urls import path

from AppCoder import views
from django.contrib.auth.views import LogoutView




urlpatterns = [
   
    path('', views.inicio, name="Inicio"), #esta era nuestra primer view
    path('cursos', views.cursos, name="Cursos"),
    path('profesores', views.profesores, name="Profesores"),
    path('estudiantes', views.estudiantes, name="Estudiantes"),
    path('entregables', views.entregables, name="Entregables"),
    #path('cursoFormulario', views.cursoFormulario, name="CursoFormulario"),
    #path('profesorFormulario', views.profesorFormulario, name="ProfesorFormulario"),
    #path('busquedaCamada',  views.busquedaCamada, name="BusquedaCamada"),
    path('buscar/', views.buscar),
    path('leerProfesores', views.leerProfesores, name="LeerProfesores"),
    path('eliminarProfesor/<profesor_nombre>/', views.eliminarProfesor, name="EliminarProfesor"),
    path('editarProfesor/<profesor_nombre>/', views.editarProfesor, name="EditarProfesor"),


    path('curso/list', views.CursoList.as_view(), name='List'),
    path(r'^(?P<pk>\d+)$', views.CursoDetalle.as_view(), name='Detail'),
    path(r'^nuevo$', views.CursoCreacion.as_view(), name='New'),
    path(r'^editar/(?P<pk>\d+)$', views.CursoUpdate.as_view(), name='Edit'),
    path(r'^borrar/(?P<pk>\d+)$', views.CursoDelete.as_view(), name='Delete'),

    path('clientes', views.clientes, name="Clientes"),
    path('clientes_agregar', views.clientes_agregar, name="Clientes_agregar"),
    path('buscarClientes/', views.buscarClientes),
    path('leerClientes', views.leerClientes, name="LeerClientes"),
    path('eliminarCliente/<cliente_nro>/', views.eliminarCliente, name="EliminarCliente"),
    path('editarCliente/<cliente_nro>/', views.editarCliente, name="EditarCliente"),
  
    path('animales', views.animales, name="Animal"),
    path('leerAnimal', views.leerAnimales, name="LeerAnimales"),
    path('animales_agregar', views.animales_agregar, name="Animales_agregar"),
    path('buscarAnimales/', views.buscarAnimales),
    path('eliminarAnimal/<animal_nro>/', views.eliminarAnimal, name="EliminarAnimal"),
    path('editarAnimal/<animal_nro>/', views.editarAnimal, name="EditarAnimal"),
    
    path('doctores', views.doctores, name="Doctor"),
    path('doctores_agregar', views.doctores_agregar, name="Doctores_agregar"),
    path('leerDoctores', views.leerDoctores, name="LeerDoctores"),
    path('buscarDoctores/', views.buscarDoctores),
    path('eliminarDoctor/<doctor_nro>/', views.eliminarDoctor, name="EliminarDoctor"),
    path('editarDoctor/<doctor_nro>/', views.editarDoctor, name="EditarDoctor"),
 
    path('login',views.login_request, name ='Login'),
    path('register',views.register, name ='Register'),
    path('logout',LogoutView.as_view(template_name="Appcoder/logout.html"), name ='Logout'),
    path('editarPerfil',views.editarPerfil, name ='EditarPerfil'),

]

