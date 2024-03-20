from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .models import *
from .forms import *

from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import PasswordChangeView

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

#_______Cursos

@login_required
def cursos(request):
    contexto = {'cursos': Curso.objects.all()}
    return render(request, "aplicacion/cursos.html", contexto)



@login_required
def cursoCreate(request):
    if request.method == "POST":
        miForm = CursoForm(request.POST)
        if miForm.is_valid():
            curso_nombre = miForm.cleaned_data.get("nombre")
            curso_tipo = miForm.cleaned_data.get("tipo")
            curso_mes = miForm.cleaned_data.get("mes")
            curso_anio = miForm.cleaned_data.get("anio")
            curso = Curso(nombre=curso_nombre, 
                          tipo=curso_tipo, 
                          mes=curso_mes, 
                          anio=curso_anio,)
            curso.save()
            return render(request, "aplicacion/typ.html")
    else:
        miForm = CursoForm()
    return render(request, "aplicacion/cursoForm.html", {"form": miForm})



@login_required
def cursoUpdate(request, id_curso):
    curso = Curso.objects.get(id=id_curso)
    if request.method == "POST":
        miForm = CursoForm(request.POST)
        if miForm.is_valid():
            curso.nombre = miForm.cleaned_data.get("nombre")
            curso.tipo = miForm.cleaned_data.get("tipo")
            curso.mes = miForm.cleaned_data.get("mes")
            curso.anio = miForm.cleaned_data.get("anio")
            curso.save()         
            contexto = {'cursos': Curso.objects.all().order_by("id")}
            return render(request, "aplicacion/cursos.html", contexto)
    else:
        miForm = CursoForm(initial={'nombre': curso.nombre, 
                                    'tipo': curso.tipo,
                                    'mes': curso.mes,
                                    'anio': curso.anio})

    return render(request, "aplicacion/cursoForm.html", {"form": miForm})



class CursoDelete(LoginRequiredMixin, DeleteView):
    model = Curso
    success_url = reverse_lazy("cursos")


#_______Busqueda de Cursos
    
@login_required
def buscarCursos(request):
    return render(request, "aplicacion/buscar_curso.html")


@login_required
def encontrarCursos(request):
    if request.GET["buscar_curso"]:
        patron = request.GET["buscar_curso"]
        cursos = Curso.objects.filter(nombre__icontains=patron)
        contexto = {"cursos": cursos}
        return render(request, "aplicacion/cursos.html", contexto)
    
    contexto = {'cursos': Curso.objects.all()}
    return render(request, "aplicacion/cursos.html", contexto)


#_________Cuerpo Activo

class CuerpoList(LoginRequiredMixin,ListView):
    model = Cuerpo


class CuerpoCreate(LoginRequiredMixin,CreateView):
    model = Cuerpo
    fields = ["nombre", "apellido", "jerarquia", "email", "legajo"]
    success_url = reverse_lazy("cuerpo")


class CuerpoUpdate(LoginRequiredMixin,UpdateView):
    model = Cuerpo
    fields = ["nombre", "apellido", "jerarquia", "email", "legajo"]
    success_url = reverse_lazy("cuerpo")
    

class CuerpoDelete(LoginRequiredMixin,DeleteView):
    model = Cuerpo
    success_url = reverse_lazy("cuerpo")


#_______Instructores

class ProfesorList(LoginRequiredMixin,ListView):
    model = Profesor


class ProfesorCreate(LoginRequiredMixin,CreateView):
    model = Profesor
    fields = ["nombre", "apellido", "email", "jerarquia", "cuartel"]
    success_url = reverse_lazy("profesores")


class ProfesorUpdate(LoginRequiredMixin,UpdateView):
    model = Profesor
    fields = ["nombre", "apellido", "email", "jerarquia", "cuartel"]
    success_url = reverse_lazy("profesores")


class ProfesorDelete(LoginRequiredMixin,DeleteView):
    model = Profesor
    success_url = reverse_lazy("profesores")


#_______Cartelera de novedades
    
@login_required
def cartelera(request):
    contexto = {'cartelera': Cartelera.objects.all()}
    return render(request, "aplicacion/cartelera_list.html", contexto)


@login_required
def carteleraForm(request):
    if request.method == "POST":
        miForm = CarteleraForm(request.POST)
        if miForm.is_valid():
            cartelera_titulo = miForm.cleaned_data.get("titulo")
            cartelera_subtitulo = miForm.cleaned_data.get("subtitulo")
            cartelera_autor = miForm.cleaned_data.get("autor")
            cartelera_novedad = miForm.cleaned_data.get("novedad")
            cartelera = Cartelera(titulo=cartelera_titulo, 
                                subtitulo=cartelera_subtitulo, 
                                autor=cartelera_autor, 
                                novedad=cartelera_novedad)
            cartelera.save()
            contexto = {'cartelera': Cartelera.objects.all()}
            return render(request, "aplicacion/typ.html", contexto)
    else:        
        miForm = CarteleraForm(initial={'cartelera': 'Escriba aquí su novedad'})
    return render(request, "aplicacion/cartelera_form.html", {"form": miForm})


class CarteleraCreate(LoginRequiredMixin,CreateView):
    model = Cartelera
    fields = ["titulo", "subtitulo", "autor", "novedad"]
    success_url = reverse_lazy("cartelera")


class CarteleraUpdate(LoginRequiredMixin,UpdateView):
    model = Cartelera
    fields = ["titulo", "subtitulo", "autor", "novedad"]
    success_url = reverse_lazy("cartelera")


class CarteleraDelete(LoginRequiredMixin,DeleteView):
    model = Cartelera
    success_url = reverse_lazy("cartelera")


#_________Login, Logout, Autenticación de usuarios, Registro de usuarios
def login_request(request):         
    if request.method == "POST":
        usuario = request.POST['username']
        clave = request.POST['password']
        user = authenticate(request, username=usuario, password=clave)
        if user is not None:
            login(request, user)
            
            #___Avatar
            try:
                avatar = Avatar.objects.get(user=request.user.id).imagen.url
            except:
                avatar = "/media/avatares/default.png"
            finally:
                request.session["avatar"] = avatar
            #_____    

            return render(request, "aplicacion/index.html")
        else:
            return redirect(reverse_lazy('login'))
    else: 
        miForm = AuthenticationForm()

    return render(request, "aplicacion/login.html", {"form": miForm})



def register(request):
    if request.method == "POST":
        miForm = RegistroForm(request.POST)
        if miForm.is_valid():
            usuario = miForm.cleaned_data.get("username")
            miForm.save()
            return redirect(reverse_lazy('registro_exitoso'))
    else: 
        miForm = RegistroForm()

    return render(request, "aplicacion/registro.html", {"form": miForm})



def registroExitoso(request):
    return render(request, "aplicacion/registro_exitoso.html")



#_______Edición de perfil, cambio de contraseña y Avatar

@login_required
def editProfile(request):
    usuario = request.user
    if request.method == "POST":
        miForm = UserEditForm(request.POST)
        if miForm.is_valid():
            user = User.objects.get(username=usuario)
            user.email = miForm.cleaned_data.get("email")
            user.first_name = miForm.cleaned_data.get("first_name")
            user.last_name = miForm.cleaned_data.get("last_name")
            user.save()
            return redirect(reverse_lazy('home'))
    else: 
        miForm = UserEditForm(instance=usuario)

    return render(request, "aplicacion/editar_perfil.html", {"form": miForm} )    


class CambiarClave(LoginRequiredMixin, PasswordChangeView):
    template_name = "aplicacion/cambiar_clave.html"
    success_url = reverse_lazy("home")



@login_required
def agregarAvatar(request):
    if request.method == "POST":
        miForm = AvatarForm(request.POST, request.FILES)
        if miForm.is_valid():
            usuario = User.objects.get(username=request.user)
            
            avatarViejo = Avatar.objects.filter(user=usuario)
            if len(avatarViejo) > 0:
                for i in range(len(avatarViejo)):
                    avatarViejo[i].delete()
            
            avatar = Avatar(user=usuario,
                            imagen=miForm.cleaned_data["imagen"])
            avatar.save()
            imagen = Avatar.objects.get(user=usuario).imagen.url
            request.session["avatar"] = imagen  
            return redirect(reverse_lazy('home'))
    
    else:
        miForm = AvatarForm()

    return render(request, "aplicacion/agregar_avatar.html", {"form": miForm} )    


#_____Views del proyecto

@login_required
def home(request):
    return render(request, "aplicacion/index.html")

def contacto(request):
    return render(request, "aplicacion/contacto.html")

def historia(request):
    return render(request, "aplicacion/historia.html")

#_______Adicionales
@login_required
def acerca(request):
    return render(request, "aplicacion/acerca.html")
@login_required
def typ(request):
    return render(request, "aplicacion/typ.html")