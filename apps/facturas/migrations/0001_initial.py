# Generated by Django 3.0.3 on 2020-05-22 05:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('api', '0001_initial'),
        ('Usuarios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Factura',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diferencia', models.BigIntegerField()),
                ('cargo_mora', models.DecimalField(decimal_places=1, max_digits=300)),
                ('total', models.DecimalField(decimal_places=1, max_digits=300)),
                ('pagada', models.BooleanField(default=False)),
                ('fecha', models.DateField(auto_now=True)),
                ('consumo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api.Consumo')),
                ('contrato', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Usuarios.Contrato')),
            ],
        ),
        migrations.CreateModel(
            name='Mora',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dias_retraso', models.BigIntegerField()),
                ('factura', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='facturas.Factura')),
            ],
        ),
    ]
