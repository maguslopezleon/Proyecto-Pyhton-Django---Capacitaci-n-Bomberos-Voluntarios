
from django.urls import path, include
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    #______Menu principal
    path('', home, name="home"),
    path('contacto/', contacto, name="contacto"),
    path('historia/', historia, name="historia"),
    
    #_______Otras páginas
    path('acerca/', acerca, name="acerca"),
    path('typ/', typ, name="typ"),

    #_______Profesores
    path('profesores/', ProfesorList.as_view(), name="profesores"),
    path('prof_create/', ProfesorCreate.as_view(), name="prof_create"),
    path('prof_update/<int:pk>/', ProfesorUpdate.as_view(), name="prof_update"),
    path('prof_delete/<int:pk>/', ProfesorDelete.as_view(), name="prof_delete"),
     
    #_______Cuerpo Activo
    path('cuerpo/', CuerpoList.as_view(), name="cuerpo"),
    path('cuerpo_create/', CuerpoCreate.as_view(), name="cuerpo_create"),
    path('cuerpo_update/<int:pk>/', CuerpoUpdate.as_view(), name="cuerpo_update"),
    path('cuerpo_delete/<int:pk>/', CuerpoDelete.as_view(), name="cuerpo_delete"),

    #_______Cursos
    path('cursos/', cursos, name="cursos"),
    path('curso_create/', cursoCreate, name="curso_create"),
    path('curso_update/<id_curso>/', cursoUpdate, name="curso_update"),
    path('curso_delete/<int:pk>/', CursoDelete.as_view(), name="curso_delete"),
    
    #_______Cartelera de Novedades
    path('cartelera/', cartelera, name="cartelera"),
    path('cartelera_create/', CarteleraCreate.as_view(), name="cartelera_create"),
    path('cartelera_update/<int:pk>/', CarteleraUpdate.as_view(), name="cartelera_update"),
    path('cartelera_delete/<int:pk>/', CarteleraDelete.as_view(), name="cartelera_delete"),

    #_______Buscar
    path('buscar_curso/', buscarCursos, name="buscar_curso"),
    path('encontrar_curso/', encontrarCursos, name="encontrar_curso"),

    #_______Login, Logout, Registration
    path('login/', login_request, name="login"),
    path('logout/', LogoutView.as_view(template_name="aplicacion/logout.html") , name="logout"),
    path('registrar/', register, name="registrar"),
    path('registro_exitoso/', registroExitoso, name="registro_exitoso"),
 
    #_______Editar perfil, cambio de contraseña y avatar
    path('perfil/', editProfile, name="perfil"),
    path('<int:pk>/password/', CambiarClave.as_view(), name="cambiar_clave"),
    path('agregar_avatar', agregarAvatar, name="agregar_avatar"),
]