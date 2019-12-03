from .models import Planta
import django_filters

class PlantaFilter(django_filters.FilterSet):
    class Meta:
        model = Planta
        fields = ['tipoPlanta',]
        labels = {'tipoPlanta': 'Tipo de Planta'}
        

