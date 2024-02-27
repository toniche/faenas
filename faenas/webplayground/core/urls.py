from django.urls import path
from .views import HomePageView, SamplePageView, SomosPageView, ContactoPageView

urlpatterns = [
    path('', HomePageView.as_view(), name="home"),
    path('sample/', SamplePageView.as_view(), name="sample"),
    path('somos/', SomosPageView.as_view(), name="somos"),
    path('contacto/', ContactoPageView.as_view(), name="contacto")
]