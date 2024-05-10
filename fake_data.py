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
    saldo = fake.random_number(digits=5)  # Adjust digits as needed

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
    tipo_movimiento_choices = ['consignacion', 'retiro']
    fecha = fake.date_time_this_year()
    monto = fake.random_number(digits=4) 
    tipo_movimiento = choice(tipo_movimiento_choices)
    description = fake.paragraph(nb_sentences=1, variable_nb_sentences=True)
    while len(description) > 30:
        description = fake.paragraph(nb_sentences=1, variable_nb_sentences=True)
    try:
        movimiento = Movimiento.objects.create(
            fecha=fecha,
            monto=monto,
            tipo=tipo_movimiento,
            cuenta=cuenta,
            descripcion=description
        )
        return movimiento
    except :
        pass

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
