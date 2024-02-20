from django.views.generic.base import TemplateView
from django.shortcuts import render
from .models import Clientes, Reparaciones, BonoRepara
from django.db import models

# VISTAS BASADAS EN CLASES, + INFO https://ccbv.co.uk
class ReparaPageView(TemplateView):
    template_name = "faenas/repara.html"
    def get(self, request, *arg, **kwargs):
        queryset = Reparaciones.objects.all()
        context = {
            "object_list": queryset,
            "Cliente": "List"
        }
        Cliente = ""
        if request.POST.get('Cliente'):
            print("ENTRA POST")
        #     nombres = filter(lambda reparapageview: reparapageview.Cliente == request.POST.get, Cliente)
            return render(request, self.template_name, context)
        return render(request, self.template_name, context)
        
class ClientePageView(TemplateView):
    template_name = "faenas/clientes.html"
    def get(self, request, *arg, **kwargs):
        queryset = Clientes.objects.all()
        context = {
            "object_list": queryset,
            "Nombre": "List"
        }
        return render(request, self.template_name, context)
class BonoPageView(TemplateView):
    template_name = "faenas/bonos.html"
    def get(self, request, *arg, **kwargs):
        queryset = BonoRepara.objects.all()
        context = {
            "object_list": queryset,
            "Cliente": "List"
        }
        return render(request, self.template_name, context)



