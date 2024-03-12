from django.contrib import admin

from .models import *

class ProductoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "id")
    list_filter = ("nombre",)

class OrdenAdmin(admin.ModelAdmin):
    list_display = ("numero", "fechaEntrega")
    list_filter = ("numero",)


admin.site.register(Producto, ProductoAdmin)
admin.site.register(Stock)
admin.site.register(Cliente)
admin.site.register(Orden, OrdenAdmin)
