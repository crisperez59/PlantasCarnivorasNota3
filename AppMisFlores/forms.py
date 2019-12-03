from django import forms
from .models import Usuario, Planta
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from rest_framework import routers, serializers, viewsets



class PlantaForm(forms.ModelForm):
    class Meta:
        model = Planta
        fields = ['nombre','descripcion','tipoPlanta','valor','imagen']
        labels = {'nombre':'nombre','descripcion':'descripcion','tipoPlanta':'tipo de planta','valor':'valor','imagen':'imagen'}



class UsuarioForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
        ]
        labels = {
                'username': 'nombre de usuario',
                'first_name':'Nombre',
                'last_name': 'Apellido',
                'email': 'Mail',
                'password1': 'Contraseña',
                'password2': 'Repite Contraseña',
        }

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email']
        
class PlantaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Planta
        fields = ['url','nombre','descripcion','tipoPlanta','valor','imagen']
