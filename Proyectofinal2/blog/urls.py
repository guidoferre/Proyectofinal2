from django.urls import path
from blog.views import Cliente, cliente, lista_clientes, mecanico, BusquedaCliente, ClienteFormulario, reparacion, inicio, Buscar

urlpatterns = [
    path('', inicio, name="inicio"),
    path('cliente/', Cliente, name ='cliente'),
    path('mecanico/', mecanico, name="mecanico"),
    path('reparaciones/', reparacion, name= "reparaciones"),
    path('clienteFormulario/',ClienteFormulario, name="clienteFormulario" ),
    path('buscarcliente/', BusquedaCliente, name="BusquedaCliente" ),
    path('buscar/', Buscar , name ="Buscar" ), 
    path('lista-clientes/', lista_clientes, name ="lista" ), 


    
]
