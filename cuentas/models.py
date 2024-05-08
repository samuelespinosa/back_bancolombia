from django.db import models

class Movimiento(models.Model):
    question_text = models.CharField(max_length=200)
    fecha= models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name = "Movimiento" 
        verbose_name_plural = "Movimientos"  

class Cuenta(models.Model):
    titular= models.CharField(max_length=50)
    balance = models.DecimalField(max_digits=15, decimal_places=4) 
    movimiento= models.ForeignKey(Movimiento, on_delete=models.CASCADE)
    numero_de_cuenta= models.CharField(max_length=50)
    class Meta:
        verbose_name = "Cuenta" 
        verbose_name_plural = ""  
