from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

# Create your models here.
class Reparaciones(models.Model):
    """ idCliente=models.OneToOneField(User, on_delete=models.CASCADE) """
    Cliente=models.CharField(max_length=40)
    Email=models.EmailField(verbose_name="Correo Electrónico")
    Fecha=models.DateTimeField(verbose_name="Fecha de creación")
    Motivo=models.CharField(max_length=200)
    Estado=models.BooleanField()
    Descripcion=models.TextField(verbose_name="Descripción", max_length=600)

    class Meta:
        verbose_name = "Reparaciones"
        verbose_name_plural = "Reparaciones"
        ordering = ['Cliente']

    # método estándar de las clases de Python __str__() para devolver una cadena
    # de texto legible por humanos para cada objeto.  Esta cadena se usa para
    # representar registros individuales en el sitio de administración (y en
    # cualquier otro lugar donde necesites referirte a una instancia del modelo).
    # Con frecuencia éste devolverá un título o nombre de campo del modelo.
    def __str__(self):
        return self.Cliente

class Clientes(models.Model):
    """ idCliente=models.ForeignKey(related_name=None) """
    Nombre=models.CharField(max_length=200)
    Cif=models.CharField(max_length=10)
    Direccion=models.CharField(verbose_name="Dirección", max_length=200)
    Localidad=models.CharField(max_length=200)
    Provincia=models.CharField(max_length=200)
    CP=models.IntegerField()
    Alta=models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    Otros=models.TextField(verbose_name="Otros", max_length=600)

    class Meta:
        verbose_name = "Clientes"
        verbose_name_plural = "Clientes"
        ordering = ['Nombre']

    def __str__(self):
        return self.Nombre

class BonoRepara(models.Model):
    """ idCliente=models.ForeignKey(related_name=None) """
    Tipo=models.CharField(max_length=200)
    Cliente=models.CharField(max_length=200)
    FechaBono=models.DateField(verbose_name="Fecha de Creación")
    Expira=models.DateField(verbose_name="Fecha Caducidad")

    class Meta:
        verbose_name = "Bonos"
        verbose_name_plural = "Bonos"
        ordering = ['Cliente']

    def __str__(self):
        return self.Cliente



