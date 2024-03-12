from django.urls import path, include
from .views import *

urlpatterns = [
        path('', home, name="home"),
        path('ordenes/', ordenes, name="ordenes"),
        path('filosofia/', filosofia, name="filosofia"),
        path('productos/', productos, name="productos"),
        path('clientes/', clientes, name="clientes"),
        path('ordenes/', ordenes, name="ordenes"),
        


        #____________________ Busqueda
        path('buscar/', buscarProductos, name="buscar"),
        path('encontrar_productos/', encontrarProductos, name="encontrar_productos"),

        #___________________ Clientes
        path('clientes/', ClienteList.as_view(), name="clientes"), 
        path('cliente_create/', ClienteCreate.as_view(), name="cliente_create"), 
        path('cliente_update/<int:pk>/', ClienteUpdate.as_view(), name="cliente_update"), 
        path('cliente_delete/<int:pk>/', ClienteDelete.as_view(), name="cliente_delete"), 

        #__________Forms
        path('producto_form/', productoForm, name="producto_form"),
        path('cliente_form/', clienteForm, name="cliente_form"),



]