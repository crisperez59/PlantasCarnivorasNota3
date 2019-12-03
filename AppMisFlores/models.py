from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Usuario(models.Model):
    usuario = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    #igual al de los juegos 
    prime = models.BooleanField()
    rut = models.CharField(max_length=12)
    celular = models.CharField(max_length=12)
    

    def __str__(self):
        return self.usuario.username
        
class Planta(models.Model):
    nombre = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=60)
    tipoPlanta = models.CharField(max_length=20)
    valor = models.IntegerField()
    imagen = models.ImageField(verbose_name="imagen", upload_to="plantas", null=True, blank=True)

    def __str__(self):
        return self.nombre
    