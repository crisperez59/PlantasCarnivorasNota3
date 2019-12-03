from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers, serializers, viewsets
from .views import UserViewSet, UserSerializer, PlantaSerializer, PlantaViewSet

router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('plantas', PlantaViewSet)

urlpatterns = [
    path('', views.index, name='index'),

     path('API', include(router.urls)),
    path('api-auth/', include('rest_framework.urls'), name="rest_framework"),


    
    path('agregarUsuario', views.RegistroUsuario.as_view(), name='agregarUsuario'), #create
    path('borrarUsuario/<int:usuarioId>', views.borrarUsuario,), #delete
    path('editarUsuario/<int:usuarioId>', views.editarUsuario), #edit
    path('listarUsuariosFull', views.listarUsuarioFull, name="listarUsuariosFull"), #readFull
    path('listarUsuarios', views.listarUsuarios, name='listarUsuarios'), #read


    path('agregarPlanta', views.RegistroPlanta.as_view(), name='agregarPlanta'), #create
    path('listarPlantas', views.listarPlantas, name='search'), #read
    path('borrarPlanta/<int:plantaId>', views.borrarPlanta), #delete
    path('editarPlanta/<int:plantaId>', views.editarPlanta), #edit
    path('listarPlantasFull', views.listarPlantasFull, name="listarPlantasFull"), #readFull

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
