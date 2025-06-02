from rest_framework import serializers
from . import models

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Usuario
        fields = '__all__'

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Cliente
        fields = '__all__'

class PropietarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Propietario
        fields = '__all__'

class EmpleadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Empleado
        fields = '__all__'

class ChoferSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Chofer
        fields = '__all__'

class VehiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Vehiculo
        fields = '__all__'

class FotoVehiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.FotoVehiculo
        fields = '__all__'

class ReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Reserva
        fields = '__all__'

class ContratoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Contrato
        fields = '__all__'

class PagoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Pago
        fields = '__all__'

class ReciboSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Recibo
        fields = '__all__'

class CalificacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Calificacion
        fields = '__all__'
