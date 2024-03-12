from django.db import models

# Create your models here.

class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    id = models.IntegerField(primary_key=True)
    precio = models.IntegerField()
    descripcion = models.CharField(max_length=255)
    

    class Meta:
        ordering = ["nombre"]

    def __str__(self):
        return f"{self.nombre}"


class Stock(models.Model):
    id_producto = models.IntegerField()
    cantidad = models.IntegerField()

    class Meta:
        verbose_name = "Stock"
        verbose_name_plural = "Stock"
    
    def __str__(self):
        return f"{self.id_producto}"    


class Cliente(models.Model):
    nombre = models.CharField(max_length=60)
    apellido = models.CharField(max_length=60)
    email = models.EmailField()

    def __str__(self):
        return f"{self.apellido}, {self.nombre}"

class Orden(models.Model):
    numero = models.IntegerField()
    fechaEntrega = models.DateField()
    direccion = models.CharField(max_length=100)
    entregado = models.BooleanField(null=True)
    
    class Meta:
        verbose_name = "Orden"
        verbose_name_plural = "Ordenes"

    def __str__(self):
        return f"{self.numero}"
    
#class Tracker(models.Model):
#    #order_item = models.ForeignKey('store.CartOrderItem', on_delete=models.SET_NULL, null=True, related_name="cartorderitem_tracker")
#    estado = models.CharField(max_length=5000, null=True, blank=True)
#    ubicacion = models.CharField(max_length=5000, null=True, blank=True)
#    actividad = models.CharField(max_length=5000, null=True, blank=True)
#    fecha = models.DateField(auto_now_add=True)

#def __str__(self):
#    return self.order_item    
    