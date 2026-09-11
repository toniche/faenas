from django.contrib import admin
from .models import Clientes, Reparaciones, BonoRepara

class ReparacionesAdmin(admin.ModelAdmin):
    list_display=("cliente_display", "Fecha", "Motivo", "Estado", "Descripcion")
    list_display_links = ["cliente_display", "Descripcion"]
    search_fields=("Cliente", "ClienteRelacionado__Nombre", "ClienteRelacionado__Cif", "Email", "Motivo", "Descripcion")
    list_filter=("Estado", "ClienteRelacionado", "Fecha")
    date_hierarchy=("Fecha")

    def cliente_display(self, obj):
        return obj.cliente_display

    cliente_display.short_description = "Cliente"

class ClientesAdmin(admin.ModelAdmin):
    list_display=("Nombre", "Cif", "Direccion", "Localidad", "Provincia", "CP", "Alta", "Otros")
    list_display_links=["Nombre", "Otros"]
    search_fields=("Nombre", "Cif", "Direccion", "Localidad", "Provincia", "CP", "Otros")
    list_filter=("Nombre", "Cif", "Alta", "Otros")


class BonosAdmin(admin.ModelAdmin):
    list_display=("Tipo", "Cliente", "FechaBono", "Expira")
    list_display_links=["Cliente"]
    search_fields=("Cliente", "Tipo")
    list_filter=("Cliente", "Tipo", "Expira")

admin.site.register(Clientes, ClientesAdmin)
admin.site.register(BonoRepara, BonosAdmin)
admin.site.register(Reparaciones, ReparacionesAdmin)