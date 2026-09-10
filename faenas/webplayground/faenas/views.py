from django.views.generic.base import TemplateView
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.utils.timezone import localdate
from .models import Clientes, Reparaciones, BonoRepara
from django.db.models import Q

# VISTAS BASADAS EN CLASES, + INFO https://ccbv.co.uk
class ReparaPageView(LoginRequiredMixin, TemplateView):
    template_name = "faenas/repara.html"
    def get(self, request, *arg, **kwargs):
        queryset = Reparaciones.objects.all()
        if not request.user.is_superuser:
            queryset = queryset.filter(Email__iexact=request.user.email)

        search = request.GET.get("q", "").strip()
        if search:
            queryset = queryset.filter(
                Q(Cliente__icontains=search)
                | Q(Email__icontains=search)
                | Q(Motivo__icontains=search)
                | Q(Descripcion__icontains=search)
            )

        estado = request.GET.get("estado", "").strip().lower()
        if estado == "pendiente":
            queryset = queryset.filter(Estado=False)
        elif estado == "solucionado":
            queryset = queryset.filter(Estado=True)

        queryset = queryset.order_by("-Fecha", "-id")
        context = {
            "object_list": queryset,
            "Cliente": "List",
            "search": search,
            "estado": estado,
        }
        return render(request, self.template_name, context)
        
class ClientePageView(LoginRequiredMixin, UserPassesTestMixin, TemplateView):
    template_name = "faenas/clientes.html"

    def test_func(self):
        return self.request.user.is_staff

    def get(self, request, *arg, **kwargs):
        queryset = Clientes.objects.all()
        context = {
            "object_list": queryset,
            "Nombre": "List",
        }
        return render(request, self.template_name, context)

class BonoPageView(LoginRequiredMixin, TemplateView):
    template_name = "faenas/bonos.html"
    def get(self, request, *arg, **kwargs):
        queryset = BonoRepara.objects.all()
        if not request.user.is_superuser:
            queryset = queryset.filter(Cliente__iexact=request.user.first_name)
        context = {
            "object_list": queryset,
            "Cliente": "List",
            "today": localdate(),
        }
        return render(request, self.template_name, context)



