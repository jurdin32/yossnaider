# Generated by Django 2.0 on 2020-02-04 00:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Clientes', '0001_initial'),
        ('Cobradores', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DetalleVenta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FECHA', models.DateField(auto_now_add=True)),
                ('CANTIDAD', models.IntegerField(default=1)),
                ('VALOR', models.DecimalField(decimal_places=2, max_digits=9)),
                ('TOTAL', models.DecimalField(decimal_places=2, max_digits=9)),
            ],
        ),
        migrations.CreateModel(
            name='Kardex',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DETALLE', models.TextField()),
                ('TIPO', models.CharField(max_length=2)),
                ('FECHA', models.DateField()),
                ('CANTIDAD', models.IntegerField()),
                ('PRECIO_COMPRA', models.DecimalField(decimal_places=2, max_digits=9)),
                ('PRECIO_VENTA', models.DecimalField(decimal_places=2, max_digits=9)),
                ('TOTAL_COMPRA', models.DecimalField(decimal_places=2, max_digits=9)),
                ('TOTAL_VENTA', models.DecimalField(decimal_places=2, max_digits=9)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NOMBRE', models.CharField(max_length=120)),
                ('DETALLE', models.TextField(blank=True, null=True)),
                ('PRECIO_COMPRA', models.DecimalField(decimal_places=2, max_digits=9)),
                ('MARCA', models.CharField(blank=True, max_length=60, null=True)),
                ('SERIE', models.CharField(blank=True, max_length=60, null=True, verbose_name=60)),
                ('ESTADO', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tarjeta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FECHA', models.DateField(auto_now_add=True)),
                ('ABONO', models.DecimalField(decimal_places=2, max_digits=9)),
                ('COBRADOR', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Cobradores.Cobrador')),
            ],
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FECHA', models.DateField(auto_now_add=True)),
                ('GANACIA', models.DecimalField(decimal_places=2, max_digits=9)),
                ('VALOR', models.DecimalField(decimal_places=2, max_digits=9)),
                ('ESTADO', models.BooleanField(default=True)),
                ('CLIENTE', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Clientes.Cliente')),
            ],
        ),
        migrations.AddField(
            model_name='tarjeta',
            name='VENTA',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Productos.Venta'),
        ),
        migrations.AddField(
            model_name='kardex',
            name='PRODUCTO',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Productos.Producto'),
        ),
        migrations.AddField(
            model_name='detalleventa',
            name='PRODUCTO',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Productos.Producto'),
        ),
        migrations.AddField(
            model_name='detalleventa',
            name='VENTA',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Productos.Venta'),
        ),
    ]