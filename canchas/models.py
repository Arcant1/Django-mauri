from django.db import models
from django.utils import timezone

# Create your models here.
class Cancha(models.Model):
	TIPO = (
		('5','Cancha de 5'),
		('7','Cancha de 7'),
		('9','Cancha de 9'),
		('11','Cancha de 11'),
	)
	nombre = models.CharField(max_length=20, default='Nombre')
	cod = models.CharField(max_length=20, default='Codigo')
	tipo = models.CharField(max_length=2, choices=TIPO, default=TIPO[0])
	vestuario = models.BooleanField(default=True)
	iluminacion = models.BooleanField(default=True)
	sintetico = models.BooleanField(default=True)

	def __str__(self):
		return self.nombre	

class Turno(models.Model):
	cancha = models.ForeignKey(Cancha, on_delete=models.CASCADE, default='')
	cliente = models.CharField(max_length=20, default='Cliente')
	empleado = models.CharField(max_length=20, default='Empleado')
	fecha = models.DateField(auto_now_add=True)
	fyh = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return f'{self.cancha.nombre} + {self.fyh}'