from django.contrib import admin
from gestionpedidos.models import clientes,articulos,pedidos


# Register your models here.
class clientesAdmin(admin.ModelAdmin):
    list_display=("nombre","direccion","tlfno")
    search_fields=("nombre","tlfno")

class articulosAdmin(admin.ModelAdmin):
    list_filter=("seccion",)
    #search_fields=("nombre","seccion","precio")

class pedidosAdmin(admin.ModelAdmin):
    list_display=("numeros","fecha",)
    list_filter=("fecha",)
    date_hierarchy="fecha"

admin.site.register(clientes,clientesAdmin)
admin.site.register(articulos,articulosAdmin)
admin.site.register(pedidos,pedidosAdmin)