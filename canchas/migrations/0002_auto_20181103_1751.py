# Generated by Django 2.1.2 on 2018-11-03 20:51

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('canchas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cancha',
            name='cod',
            field=models.CharField(default='Codigo', max_length=20),
        ),
        migrations.AddField(
            model_name='cancha',
            name='iluminacion',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='cancha',
            name='nombre',
            field=models.CharField(default='Nombre', max_length=20),
        ),
        migrations.AddField(
            model_name='cancha',
            name='sintetico',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='cancha',
            name='tipo',
            field=models.CharField(choices=[('5', 'Cancha de 5'), ('7', 'Cancha de 7'), ('9', 'Cancha de 9'), ('11', 'Cancha de 11')], default=('5', 'Cancha de 5'), max_length=2),
        ),
        migrations.AddField(
            model_name='cancha',
            name='vestuario',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='turno',
            name='cancha',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='canchas.Cancha'),
        ),
        migrations.AddField(
            model_name='turno',
            name='cliente',
            field=models.CharField(default='Cliente', max_length=20),
        ),
        migrations.AddField(
            model_name='turno',
            name='empleado',
            field=models.CharField(default='Empleado', max_length=20),
        ),
        migrations.AddField(
            model_name='turno',
            name='fecha',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='turno',
            name='fyh',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
