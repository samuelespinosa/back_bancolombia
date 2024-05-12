
from rest_framework import serializers
from .models import Cuenta, Movimiento

class CuentasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cuenta
        fields = '__all__'

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
                raise serializers.ValidationError('Saldo insuficiente para retirar.')
            cuenta.saldo -= monto
            cuenta.save()
        else:
            raise serializers.ValidationError('Tipo de movimiento no válido.')
        
        validated_data['saldo_calculado']=cuenta.saldo
        movimiento = Movimiento.objects.create(**validated_data)
        return movimiento
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        fecha_obj = instance.fecha
        formatted_fecha = fecha_obj.strftime('%d/%m')
        representation['fecha'] = formatted_fecha
        return representation

    class Meta:
        model = Movimiento
        fields = '__all__'
        read_only_fields = ('saldo_calculado',)
