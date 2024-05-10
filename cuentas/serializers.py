from rest_framework import serializers
from .models import Cuenta, Movimiento   

class CuentasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cuenta 
        fields='__all__'

class MovimientosSerializer(serializers.ModelSerializer):
    cuenta = serializers.PrimaryKeyRelatedField(queryset=Cuenta.objects.all())
    
    def create(self, validated_data):
        cuenta = validated_data['cuenta']
        monto = validated_data['monto']
        tipo = validated_data['tipo']

        if tipo == 'consignacion':
            cuenta.saldo += monto
            cuenta.save()
        elif tipo == 'retiro':
            if cuenta.saldo < monto:
                raise serializers.ValidationError('saldo insuficiente para retirar')
            cuenta.saldo -= monto
            cuenta.save()
        else:
            raise serializers.ValidationError('Tipo de movimiento no válido.')

        return Movimiento.objects.create(**validated_data)
    
    class Meta:
        model = Movimiento 
        fields = '__all__'

