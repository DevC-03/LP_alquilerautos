from rest_framework import routers
from . import views
from django.urls import path,include
from .views import UsuarioActualView

router = routers.DefaultRouter()

router.register('usuarios', views.UsuarioViewSet)
router.register('clientes', views.ClienteViewSet)
router.register('propietarios', views.PropietarioViewSet)
router.register('empleados', views.EmpleadoViewSet)
router.register('choferes', views.ChoferViewSet)
router.register('vehiculos', views.VehiculoViewSet)
router.register('fotos', views.FotoVehiculoViewSet)
router.register('reservas', views.ReservaViewSet)
router.register('contratos', views.ContratoViewSet)
router.register('pagos', views.PagoViewSet)
router.register('recibos', views.ReciboViewSet)
router.register('calificaciones', views.CalificacionViewSet)

urlpatterns = [
    path('',include(router.urls)),
    path('login/', views.Login.as_view(), name='login'),
    path('usuario-actual/', UsuarioActualView.as_view(), name='usuario-actual'),
]