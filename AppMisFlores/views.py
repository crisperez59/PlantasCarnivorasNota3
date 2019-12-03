from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from rest_framework import routers, serializers, viewsets
from .forms import PlantaForm, UsuarioForm

from .forms import UsuarioForm, UserSerializer, PlantaSerializer
from .filters import PlantaFilter
# Create your views here.
from .models import Usuario, Planta

def index(request):
    return render(request, 'appMisFlores/base.html', {})


class RegistroPlanta(CreateView):
    model = Planta
    form_class = PlantaForm
    template_name = "appMisFlores/plantas/agregarPlantas.html"
    success_url = reverse_lazy('index')

@login_required
def listarPlantas(request):
    planta_list = Planta.objects.all()
    planta_filter = PlantaFilter(request.GET, queryset=planta_list)
    return render(request, 'appMisFlores/plantas/listarPlantas.html', {'filter': planta_filter})


@login_required
def listarPlantasFull(request):
    #creamos una coleccion la cual carga todos los registros
    planta = Planta.objects.all()
    #renderizamos la coleccion en el template
    return render(request, 
            "appMisFlores/plantas/listarPlantasFull.html", {'plantas': planta})

#@login_required
def editarPlanta(request, plantaId):
    planta = Planta.objects.get(id=plantaId)
    data = {
        'form': PlantaForm(instance=planta)
    }
    
    if request.method=="POST":
        #Actualizamos el Formulario con los datos del objeto
        formulario=PlantaForm(request.POST, instance=planta)
        #si el form es valido
        if formulario.is_valid():
           
            formulario.save()
            data['mensaje'] = "modificado correctamente"
        data['form'] = formulario
    return render(request, "appMisFlores/plantas/editarPlanta.html",data)   

@login_required
def borrarPlanta(request, plantaId):
    instacia = Planta.objects.get(id=plantaId)
    instacia.delete()
    return redirect('/')

#USUARIO

class RegistroUsuario(CreateView):
    model = User
    template_name = "appMisFlores/usuario/agregarUsuario.html"
    form_class = UsuarioForm
    success_url = reverse_lazy('index')


def listarUsuarios(request):
    # creamos una coleccion la cual carga todos los registros
    usuario = User.objects.all()
    # renderizamos la coleccion en el template
    return render(request,
                "appMisFlores/usuario/listarUsuarios.html", {'usuarios': usuario}) 

@login_required
def listarUsuarioFull(request):
    #creamos una coleccion la cual carga todos los registros
    usuario = User.objects.all()
    #renderizamos la coleccion en el template
    return render(request, 
            "appMisFlores/usuario/listarUsuariosFull.html", {'usuarios': usuario})


def editarUsuario(request, usuarioId):
    instancia= Usuario.objects.get(id=usuarioId)
    form= UsuarioForm(instance=instancia)
    if request.method=="POST":
        #Actualizamos el Formulario con los datos del objeto
        form=UsuarioForm(request.POST, instance=instancia)
        #si el form es valido
        if form.is_valid():
            #guardamos el formulario pero sin confirmar aun
            instancia= form.save(commit=False)
            #grabamos
            instancia.save()
    return render(request, "appMisFlores/usuario/editarUsuario.html", {'form':form})   


def borrarUsuario(request, usuarioId):
    instacia = User.objects.get(id=usuarioId)
    instacia.delete()
    return redirect('/')




# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class PlantaViewSet(viewsets.ModelViewSet):
    queryset = Planta.objects.all()
    serializer_class = PlantaSerializer
