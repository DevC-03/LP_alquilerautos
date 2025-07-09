from django.shortcuts import render
from . import models, serializers
from rest_framework import viewsets

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

from django.contrib.auth import authenticate

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

class Login(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request':request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'username': user.username
        })

# class Login(ObtainAuthToken):
#     def post(self, request):
#         username = request.data.get("username")
#         password = request.data.get("password")
#         user = authenticate(username=username, password=password)
#         if user is not None:
#             token, _ = Token.objects.get_or_create(user=user)
#             return Response({"token": token.key})
#         else:
#             return Response({"error": "Credenciales Inválidas"}, status=400)


