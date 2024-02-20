from django.contrib import admin
from .models import Clientes, Reparaciones, BonoRepara

class ReparacionesAdmin(admin.ModelAdmin):
    list_display=("Cliente", "Fecha", "Motivo", "Estado", "Descripcion")
    list_display_links = ["Cliente", "Descripcion"]
    search_fields=("Cliente", "Email", "Fecha", "Motivo", "Estado", "Descripcion")
    list_filter=("Cliente", "Email", "Fecha", "Motivo", "Estado", "Descripcion")
    date_hierarchy=("Fecha")

class ClientesAdmin(admin.ModelAdmin):
    list_display=("Nombre", "Cif", "Direccion", "Localidad", "Provincia", "CP", "Alta", "Otros")
    list_display_links=["Nombre", "Otros"]
    search_fields=("Nombre", "Cif", "Direccion", "Localidad", "Provincia", "CP", "Otros")
    list_filter=("Nombre", "Cif", "Alta", "Otros")


class BonosAdmin(admin.ModelAdmin):
    list_display=("Tipo", "Cliente", "FechaBono", "Expira")
    list_display_links=["Cliente"]
    search_fields=("Cliente", "Cif")
    list_filter=("Cliente", "Tipo", "Expira")

admin.site.register(Clientes, ClientesAdmin)
admin.site.register(BonoRepara, BonosAdmin)
admin.site.register(Reparaciones, ReparacionesAdmin)