from django.urls import path

# VISTAS BASADAS EN CLASES, + INFO https://ccbv.co.uk
from .views import (
    ReparaPageView, 
    ClientePageView,
    BonoPageView,
)

urlpatterns = [
    path('repara/', ReparaPageView.as_view(), name="repara"),
    path('clientes/', ClientePageView.as_view(), name="clientes"),
    path('bonos/', BonoPageView.as_view(), name="bonos"),
]



