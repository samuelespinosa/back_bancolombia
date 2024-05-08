from rest_framework import serializers
from .models import Cuenta, Movimiento   

class CuentaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cuenta 
        fields='__all__'

class MovimientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movimiento 
        fields = '__all__'
