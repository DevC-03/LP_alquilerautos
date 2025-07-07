from rest_framework import serializers
from . import models

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Usuario
        fields = '__all__'

class ClienteSerializer(serializers.ModelSerializer):
    cliente_user = serializers.CharField(source='usuario.username', read_only=True)

    class Meta:
        model = models.Cliente
        fields = '__all__' 

class PropietarioSerializer(serializers.ModelSerializer):
    propietario_user = serializers.CharField(source='usuario.username', read_only=True)
    class Meta:
        model = models.Propietario
        fields = '__all__'

class EmpleadoSerializer(serializers.ModelSerializer):
    empleado_user = serializers.CharField(source='usuario.username', read_only=True)
    class Meta:
        model = models.Empleado
        fields = '__all__'

class ChoferSerializer(serializers.ModelSerializer):
    chofer_user = serializers.CharField(source='usuario.username', read_only=True)
    class Meta:
        model = models.Chofer
        fields = '__all__'

class VehiculoSerializer(serializers.ModelSerializer):
    propietario_vehiculo = serializers.CharField(source='propietario.usuario.username', read_only=True)
    class Meta:
        model = models.Vehiculo
        fields = '__all__'

class FotoVehiculoSerializer(serializers.ModelSerializer):
    marca_vehiculo = serializers.CharField(source='vehiculo.marca', read_only=True)
    modelo_vehiculo = serializers.CharField(source='vehiculo.modelo', read_only=True)
    class Meta:
        model = models.FotoVehiculo
        fields = '__all__'

class ReservaSerializer(serializers.ModelSerializer):
    cliente_reserva = serializers.CharField(source='cliente.usuario.username', read_only=True)
    vehiculo_reserva = serializers.CharField(source='vehiculo.placa', read_only=True)
    chofer_reserva = serializers.CharField(source='chofer.usuario.username', read_only=True, allow_null=True)
    class Meta:
        model = models.Reserva
        fields = '__all__'

class ContratoSerializer(serializers.ModelSerializer):
    contrato_reserva = serializers.CharField(source='reserva.cliente.usuario.username', read_only=True)
    class Meta:
        model = models.Contrato
        fields = '__all__'

class PagoSerializer(serializers.ModelSerializer):
    pago_contrato = serializers.CharField(source='contrato.reserva.cliente.usuario.username', read_only=True)
    class Meta:
        model = models.Pago
        fields = '__all__'

class ReciboSerializer(serializers.ModelSerializer):
    recibo_contrato = serializers.CharField(source='contrato.reserva.cliente.usuario.username', read_only=True)
    class Meta:
        model = models.Recibo
        fields = '__all__'

class CalificacionSerializer(serializers.ModelSerializer):
    calificacion_cliente = serializers.CharField(source='cliente.usuario.username', read_only=True)
    class Meta:
        model = models.Calificacion
        fields = '__all__'
