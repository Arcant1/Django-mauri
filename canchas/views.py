from django.shortcuts import render, redirect
from .models import Cancha, Turno

# Create your views here.
def home(request):
	canchas = Cancha.objects.all()
	return render(request, 'home.html', {'canchas': canchas})

def detail(request, id):
	cancha = Cancha.objects.get(id=id)
	turno = Turno.objects.all()[:20]
	return render(request, 'detail.html', {'cancha': cancha, 'turno':turno})

def newturno(request, id):
	cancha = Cancha.objects.get(id=id)
	if request.method == 'POST':
		data = request.POST
		todos = Turno.objects.all()
		turno = Turno(cancha=cancha, cliente=data['cliente'], empleado=data['empleado'], fyh=data['datetime'])
		turno.save()
		return redirect('detail', id=id)
	return render(request, 'new-turno.html', {'cancha': cancha})

def deleteturno(request,id):
	turno = Turno.objects.get(id=id)
	volver = turno.cancha.id
	turno.delete()
	return redirect('detail', id=volver)

def updateturno(request,id):
	turno = Turno.objects.get(id=id)
	if request.method == 'POST':
		data = request.POST
		turno.fyh = data['datetime']
		turno.save()
		return redirect('detail', id=turno.cancha.id)
	return render(request, 'update-turno.html', {'turno': turno})


def deletecancha(request,id):
	cancha = Cancha.objects.get(id=id)
	cancha.delete()
	return redirect('home')

def newcancha(request):
	canchas = Cancha.TIPO
	if request.method == 'POST':
		data = request.POST
		ves = data.get('vestuario', False)
		ilu = data.get('iluminacion', False)
		sin = data.get('sintetico', False)
		if ves == "on":
			ves = True
		if ilu == "on":
			ilu = True
		if sin == "on":
			sin = True
		can = Cancha.objects.create(
			nombre = data['nombre'], 
			cod = data['codigo'], 
			tipo = data['tipo'],
			vestuario = ves, 
			iluminacion = ilu, 
			sintetico = sin
		)
		return redirect('home')
	return render(request, 'new-cancha.html', {'canchas': canchas})