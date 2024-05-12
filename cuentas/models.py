from django.db import models
from .validators import validate_number
from .mixins import ImmutableModelMixin;  
class Cuenta(models.Model):
    TIPOS_CUENTA= (
        ('ahorro', 'Ahorro'),
        ('corriente', 'Corriente'),
        ('nomina', 'Nomina'),
    )
    titular= models.CharField(max_length=50)
    saldo = models.DecimalField(max_digits=15, decimal_places=4) 
    numero_de_cuenta= models.CharField(max_length=10,primary_key=True,validators=[validate_number])
    tipo= models.CharField(max_length=12,choices=TIPOS_CUENTA)
    class Meta:
        verbose_name = "Cuenta" 
        verbose_name_plural = "Cuentas"  

class Movimiento(ImmutableModelMixin,models.Model):
    TIPOS_MOVIMIENTO= (
        ('consignacion', 'Consignacion'),
        ('retiro', 'Retiro'),
    )
    
    descripcion = models.CharField(max_length=30)
    fecha= models.DateTimeField(auto_now_add=True)
    monto= models.DecimalField(max_digits=15, decimal_places=4) 
    tipo= models.CharField(max_length=12,choices=TIPOS_MOVIMIENTO)
    cuenta = models.ForeignKey(Cuenta, related_name='movimientos', on_delete=models.CASCADE)   
    saldo_calculado = models.DecimalField(max_digits=15, decimal_places=4,null=True) 
    class Meta:
        verbose_name = "Movimiento" 
        verbose_name_plural = "Movimientos"  
