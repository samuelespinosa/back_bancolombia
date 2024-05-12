import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bancolombia.settings')

import django
django.setup()

from faker import Faker
from random import choice
from cuentas.models import Cuenta, Movimiento

fake = Faker()

def nueva_cuenta():
    tipo_cuenta_choices = ['ahorro', 'corriente', 'nomina']
    titular = fake.name()
    saldo = 0 

    tipo_cuenta = choice(tipo_cuenta_choices)
    numero_de_cuenta = fake.random_number(digits=10)  # Adjust digits as needed

    cuenta = Cuenta.objects.create(
        titular=titular,
        saldo=saldo,
        numero_de_cuenta=numero_de_cuenta,
        tipo=tipo_cuenta
    )
    return cuenta

def nuevo_movimiento(cuenta):
    saldo_calculado=None
    tipo_movimiento = choice(['consignacion','retiro'])
    monto = fake.random_number(digits=4)
    if tipo_movimiento=='retiro': 
        saldo_calculado=cuenta.saldo-monto
        if saldo_calculado<0: 
            saldo_calculado=cuenta.saldo+monto #:) ajaj
            tipo_movimiento='consignacion'
    else:saldo_calculado=cuenta.saldo+monto
    cuenta.saldo=saldo_calculado
    Cuenta.objects.filter(numero_de_cuenta=cuenta.numero_de_cuenta).update(saldo=saldo_calculado)
    fecha = fake.date_time_this_year()
    description = fake.paragraph(nb_sentences=1, variable_nb_sentences=True)
    while len(description) > 30:
        description = fake.paragraph(nb_sentences=1, variable_nb_sentences=True)
    movimiento = Movimiento.objects.create(
        fecha=fecha,
        monto=monto,
        tipo=tipo_movimiento,
        cuenta=cuenta,
        descripcion=description,
        saldo_calculado=saldo_calculado
    )
    return movimiento

def generate_fake_data(num_cuentas, movimientos_por_cuenta):
    cuentas = []
    for _ in range(num_cuentas):
        cuenta = nueva_cuenta()
        cuentas.append(cuenta)
        print('Creando cuenta', cuenta.numero_de_cuenta) 
        for _ in range(movimientos_por_cuenta):
            movimiento=nuevo_movimiento(cuenta)
            print("Agregando movimiento")
    return cuentas

if __name__ == '__main__':  
    generate_fake_data(10,5)
