# Generated by Django 2.1.2 on 2018-11-03 20:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('canchas', '0002_auto_20181103_1751'),
    ]

    operations = [
        migrations.AlterField(
            model_name='turno',
            name='cancha',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='canchas.Cancha'),
        ),
    ]
