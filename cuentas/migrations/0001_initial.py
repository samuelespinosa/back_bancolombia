# Generated by Django 5.0.3 on 2024-05-11 21:11

import cuentas.mixins
import cuentas.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cuenta',
            fields=[
                ('titular', models.CharField(max_length=50)),
                ('saldo', models.DecimalField(decimal_places=4, max_digits=15)),
                ('numero_de_cuenta', models.CharField(max_length=10, primary_key=True, serialize=False, validators=[cuentas.validators.validate_number])),
                ('tipo', models.CharField(choices=[('ahorro', 'Ahorro'), ('corriente', 'Corriente'), ('nomina', 'Nomina')], max_length=12)),
            ],
            options={
                'verbose_name': 'Cuenta',
                'verbose_name_plural': 'Cuentas',
            },
        ),
        migrations.CreateModel(
            name='Movimiento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=30)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('monto', models.DecimalField(decimal_places=4, max_digits=15)),
                ('tipo', models.CharField(choices=[('consignacion', 'Consignacion'), ('retiro', 'Retiro')], max_length=12)),
                ('cuenta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movimientos', to='cuentas.cuenta')),
            ],
            options={
                'verbose_name': 'Movimiento',
                'verbose_name_plural': 'Movimientos',
            },
            bases=(cuentas.mixins.ImmutableModelMixin, models.Model),
        ),
    ]
