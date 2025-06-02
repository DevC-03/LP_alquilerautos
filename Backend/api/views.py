from django.shortcuts import render
from . import models, serializers
from rest_framework import viewsets

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = models.Usuario.objects.all()
    serializer_class = serializers.UsuarioSerializer

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = models.Cliente.objects.all()
    serializer_class = serializers.ClienteSerializer

class PropietarioViewSet(viewsets.ModelViewSet):
    queryset = models.Propietario.objects.all()
    serializer_class = serializers.PropietarioSerializer

class EmpleadoViewSet(viewsets.ModelViewSet):
    queryset = models.Empleado.objects.all()
    serializer_class = serializers.EmpleadoSerializer

class ChoferViewSet(viewsets.ModelViewSet):
    queryset = models.Chofer.objects.all()
    serializer_class = serializers.ChoferSerializer

class VehiculoViewSet(viewsets.ModelViewSet):
    queryset = models.Vehiculo.objects.all()
    serializer_class = serializers.VehiculoSerializer

class FotoVehiculoViewSet(viewsets.ModelViewSet):
    queryset = models.FotoVehiculo.objects.all()
    serializer_class = serializers.FotoVehiculoSerializer

class ReservaViewSet(viewsets.ModelViewSet):
    queryset = models.Reserva.objects.all()
    serializer_class = serializers.ReservaSerializer

class ContratoViewSet(viewsets.ModelViewSet):
    queryset = models.Contrato.objects.all()
    serializer_class = serializers.ContratoSerializer

class PagoViewSet(viewsets.ModelViewSet):
    queryset = models.Pago.objects.all()
    serializer_class = serializers.PagoSerializer

class ReciboViewSet(viewsets.ModelViewSet):
    queryset = models.Recibo.objects.all()
    serializer_class = serializers.ReciboSerializer

class CalificacionViewSet(viewsets.ModelViewSet):
    queryset = models.Calificacion.objects.all()
    serializer_class = serializers.CalificacionSerializer