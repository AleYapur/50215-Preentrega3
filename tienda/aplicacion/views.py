from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .models import *
from .forms import * 


from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView


def home(request):
    return render(request, "aplicacion/index.html") 

def clientes(request):
    contexto = {'clientes': Cliente.objects.all()}
    return render(request, "aplicacion/clientes.html", contexto) 

def ordenes(request):
    return render(request, "aplicacion/ordenes.html") 

def productos(request):
    contexto = {'productos': Producto.objects.all()}
    return render(request, "aplicacion/productos.html", contexto) 

def filosofia(request):
    return render(request, "aplicacion/filosofia.html") 

#_______________________________________ Buscar productos

def buscarProductos(request):
    return render(request, "aplicacion/buscar.html")

def encontrarProductos(request):
    if request.GET["buscar"]:
        patron = request.GET["buscar"]
        productos = Producto.objects.filter(nombre__icontains=patron)
        contexto = {"productos": productos}
        return render(request, "aplicacion/productos.html", contexto)
    

    contexto = {'productos': Producto.objects.all()}
    return render(request, "aplicacion/productos.html", contexto) 

#________________________ Clientes
class ClienteList(ListView):
    model = Cliente

class ClienteCreate(CreateView):
    model = Cliente
    fields = ["nombre", "apellido", "email"]
    success_url = reverse_lazy("clientes")

class ClienteUpdate(UpdateView):
    model = Cliente
    fields = ["nombre", "apellido", "email"]
    success_url = reverse_lazy("clientes")

class ClienteDelete(DeleteView):
    model = Cliente
    success_url = reverse_lazy("clientes")


#________________________________________ Forms
def productoForm(request):
    
    if request.method == "POST":
        miForm = ProductoForm(request.POST)
        if miForm.is_valid():
            producto_nombre = miForm.cleaned_data.get("nombre")
            producto_id = miForm.cleaned_data.get("id")
            producto_precio = miForm.cleaned_data.get("precio")
            producto_descripcion = miForm.cleaned_data.get("descripción")
            producto = Producto(nombre=producto_nombre, id=producto_id, precio=producto_precio, descripcion=producto_descripcion)
            producto.save()

            contexto = {'productos': Producto.objects.all()}
            return render(request, "aplicacion/productos.html", contexto) 

    else:    
        miForm = ProductoForm()

    return render(request, "aplicacion/productoForm.html", {"form": miForm} )

def clienteForm(request):
        if request.method == "POST":
            miForm = ClienteForm(request.POST)
            if miForm.is_valid():
                cliente_nombre = miForm.cleaned_data.get("nombre")
                cliente_apellido = miForm.cleaned_data.get("apellido")
                cliente_email = miForm.cleaned_data.get("email")
                
                cliente = Cliente(nombre=cliente_nombre, 
                                apellido=cliente_apellido,
                                email=cliente_email,
                                )
                cliente.save()
            
            contexto = {'clientes': Cliente.objects.all()}
            return render(request, "aplicacion/clientes.html", contexto) 

        else:     
            miForm = ClienteForm()

        return render(request, "aplicacion/clienteForm.html", {"form": miForm} )



#________________________Seguimiento de ordenes
#def order_tracker(request):
 #   if request.method=="POST":
  #      numero_orden = request.POST.get('numero_orden', '')
   #     try:
    #        orden=Orden.objects.filter(pk=numero_orden)
#
 #           if len(orden)>0:
  #              update = Orden.objects.filter(pk=numero_orden)
   #             updates = []
    #            for orden in update:
     #               # change order status to scheduled
      #              if orden.status == 'En curso':
       ##                 orden.status = 'Programada'
         #               orden.save()
          #          updates.append({'status' : orden.status})
           #         response = json.dumps(updates)
            #        return HttpResponse(response)
            #else:
             #   return HttpResponse('{}')
        #except Exception as e:
            # add some logging here
         #   return HttpResponse('{}')
    #return render(request,"tracker.html")