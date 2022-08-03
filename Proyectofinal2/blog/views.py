from django.shortcuts import render
from django.http import HttpResponse
from blog.models import cliente, mecanico, reparacion
from blog.forms import clienteFormulario


# Create your views here.


def inicio(self):
    return render (self, "Bienvenida.html")


def Cliente(request):

    return render(request, "clientes.html")



def mecanico(request):
    
    return render(request, "mecanicos.html")

def reparacion(request):

    return render(request, "Reparaciones.html")


def ClienteFormulario(request):

    print('method:', request.method)
    print('post:', request.POST)

    if request.method == 'POST':

        miFormulario = clienteFormulario(request.POST)
        if miFormulario.is_valid():

            data=miFormulario.cleaned_data

            Cliente = cliente(nombre = data['nombre'], apellido= data ['apellido'], vehiculo=data['vehiculo'])
            Cliente.save()
            return render(request, "padre.html")

    else:
        miFormulario = clienteFormulario()

    return render(request, "clienteFormulario.html", {"miFormulario": miFormulario})


def BusquedaCliente(request):

    return render(request, "BusquedaCliente.html")

def Buscar(request):

    if request.GET['nombre']:
        nombre = request.GET['nombre']
        clientes = cliente.objects.filter(nombre__icontains=nombre)

        return render(request, "ResultadoBusqueda.html", {"cliente": clientes, "nombre": nombre})

    else:
        respuesta= "no enviaste datos"

    return HttpResponse(respuesta)  


def lista_clientes(self):

    lista = cliente.objects.all()

    return render(self, "lista_clientes.html", {"lista_clientes": lista})