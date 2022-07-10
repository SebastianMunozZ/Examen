# Generated by Django 4.0.2 on 2022-06-11 00:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TipoMascota',
            fields=[
                ('id_tipomascota', models.AutoField(primary_key=True, serialize=False, verbose_name='Id de tipo mascota')),
                ('tipoMascota', models.CharField(max_length=50, verbose_name='Nombre tipo mascota')),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id_prod', models.AutoField(primary_key=True, serialize=False, verbose_name='Id producto')),
                ('nombre_prod', models.CharField(max_length=50, verbose_name='Nombre producto')),
                ('descripcion_prod', models.CharField(max_length=50, verbose_name='Descripción de Producto')),
                ('valor_prod', models.IntegerField(verbose_name='Valor producto')),
                ('imagen_prod', models.CharField(max_length=2000, verbose_name='Descripción de Mascota')),
                ('stock_prod', models.IntegerField(verbose_name='cantidad disponible')),
                ('tipo_prod', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.tipomascota')),
            ],
        ),
    ]