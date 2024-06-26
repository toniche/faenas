from django.views.generic.base import TemplateView
from django.shortcuts import render

class HomePageView(TemplateView):
    template_name = "core/home.html"
    def get(self, request, *arg, **kwargs):
        return render(request, self.template_name,
        {'title':"Consultoría y Asistencia Informática"},)

class SamplePageView(TemplateView):
    template_name = "core/sample.html"

class SomosPageView(TemplateView):
    template_name = "core/somos.html"

class ContactoPageView(TemplateView):
    template_name = "core/contacto.html"

