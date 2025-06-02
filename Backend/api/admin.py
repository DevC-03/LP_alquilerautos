from django.contrib import admin
from .models import (
    Usuario, Cliente, Propietario, Empleado, Chofer,
    Vehiculo, FotoVehiculo,
    Reserva, Contrato, Pago, Recibo,
    Calificacion
)

admin.site.register(Usuario)
admin.site.register(Cliente)
admin.site.register(Propietario)
admin.site.register(Empleado)
admin.site.register(Chofer)
admin.site.register(Vehiculo)
admin.site.register(FotoVehiculo)
admin.site.register(Reserva)
admin.site.register(Contrato)
admin.site.register(Pago)
admin.site.register(Recibo)
admin.site.register(Calificacion)
