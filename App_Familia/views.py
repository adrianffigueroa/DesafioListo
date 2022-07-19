from django.http import HttpResponse
from django.shortcuts import render

from App_Familia.models import Pariente

# Create your views here.

def carga_pariente(self, nombre, parentezco, edad, fecha_nacimiento):
    pariente=Pariente(nombre=nombre, parentezco=parentezco, edad=edad, fecha_nacimiento=fecha_nacimiento)
    pariente.save()
    documento=f'Se agregó a la base de datos a {pariente.nombre}, es mi {pariente.parentezco}, tiene {pariente.edad} y nació el {pariente.fecha_nacimiento}'
    return HttpResponse(documento)

def lista_parientes(self):
    lista=Pariente.objects.all()
    return render(self, "index.html", {"parientes": lista})