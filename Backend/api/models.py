from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager


class UsuarioManager(BaseUserManager):
    def create_user(self,username,email,password=None,**extra_fields):
        #Creamos un usario en base a nombre de usuario, contraseña y correo
        if not email:
            raise ValueError('Correo es obligatorio')
        email = self.normalize_email(email)
        user = self.model(username=username,email=email,**extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self,username,email,password=None,**extra_fields):
        #Creamos un superusario en base a nombre de usuario, contraseña y correo
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('El campo staff debe ser True')
        
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('El campo superusuario debe ser True')
        
        return self.create_user(username,email,password,**extra_fields)
    
# ====================== MODELO USUARIO ======================
class Usuario(AbstractUser):
    objects = UsuarioManager()
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    es_proveedor = models.BooleanField(default=False)
    
    def __str__(self):
        return self.username

# ====================== MODELOS DE USUARIOS ======================
class Cliente(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()
    licencia_conducir = models.CharField(max_length=20)
    telefono = models.CharField(max_length=15)
    reputacion = models.FloatField(default=5.0)
    
    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Propietario(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, primary_key=True)
    telefono = models.CharField(max_length=15)
    direccion = models.TextField()
    reputacion = models.FloatField(default=5.0)
    fecha_registro = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return str(self.usuario)

class Empleado(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, primary_key=True)
    cargo = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.usuario.username} ({self.cargo})"

class Chofer(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, primary_key=True)
    licencia = models.CharField(max_length=20)
    disponible = models.BooleanField(default=True)
    telefono = models.CharField(max_length=15)
    reputacion = models.FloatField(default=5.0)
    
    def __str__(self):
        return str(self.usuario)

# ====================== MODELO VEHÍCULO Y FOTOS ======================
class Vehiculo(models.Model):
    ESTADO_CHOICES = [
        ('DISPONIBLE', 'Disponible'),
        ('ALQUILADO', 'Alquilado'),
        ('MANTENIMIENTO', 'En mantenimiento'),
    ]
    
    propietario = models.ForeignKey(Propietario, on_delete=models.CASCADE)
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    año = models.PositiveIntegerField()
    placa = models.CharField(max_length=10, unique=True)
    precio_diario = models.DecimalField(max_digits=10, decimal_places=2)
    estado = models.CharField(max_length=15, choices=ESTADO_CHOICES, default='DISPONIBLE')
    descripcion = models.TextField(blank=True)
    promedio_calificaciones = models.FloatField(default=0.0)
    cantidad_resenas = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return f"{self.marca} {self.modelo} - {self.placa}"

class FotoVehiculo(models.Model):
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE, related_name='fotos')
    # imagen = models.ImageField(upload_to='vehiculos/')
    es_principal = models.BooleanField(default=False)
  
  
# ====================== MODELOS DE ALQUILER ======================
class Reserva(models.Model):
    ESTADO_CHOICES = [
        ('PENDIENTE', 'Pendiente'),
        ('CONFIRMADA', 'Confirmada'),
        ('CANCELADA', 'Cancelada'),
        ('COMPLETADA', 'Completada'),
    ]
    
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE)
    chofer = models.ForeignKey(Chofer, on_delete=models.SET_NULL, null=True, blank=True)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    estado = models.CharField(max_length=10, choices=ESTADO_CHOICES, default='PENDIENTE')
    precio_total = models.DecimalField(max_digits=10, decimal_places=2)
    seguro = models.BooleanField(default=False)
    requiere_chofer = models.BooleanField(default=False)
    
    def __str__(self):
        return f"Reserva #{self.id} - {self.vehiculo}"

class Contrato(models.Model):
    reserva = models.OneToOneField(Reserva, on_delete=models.CASCADE, primary_key=True)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    precio_total = models.DecimalField(max_digits=10, decimal_places=2)
    estado = models.CharField(max_length=50, default="VIGENTE")
    
    def __str__(self):
        return f"Contrato #{self.id}"

class Pago(models.Model):
    contrato = models.ForeignKey(Contrato, on_delete=models.CASCADE)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    metodo_pago = models.CharField(max_length=50)
    es_reembolsado = models.BooleanField(default=False)
    
    def __str__(self):
        return f"Pago #{self.id} - ${self.monto}"

class Recibo(models.Model):
    contrato = models.OneToOneField(Contrato, on_delete=models.CASCADE, primary_key=True)
    codigo = models.CharField(max_length=20, unique=True)
    fecha_emision = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return f"Recibo {self.codigo}"

# ====================== MODELO DE CALIFICACIONES ======================
class Calificacion(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE)
    puntuacion = models.PositiveSmallIntegerField()
    comentario = models.TextField(blank=True)
    fecha = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Calificación de {self.cliente} para {self.vehiculo}"