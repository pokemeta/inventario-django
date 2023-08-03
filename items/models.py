from django.db import models
from location.models import Location
from django.contrib.auth.models import User # importar el modelo de usuario de Django


# Create your models here.

class Item(models.Model):
    n_oficialia = models.CharField(max_length=15, blank=False, verbose_name='Número de Oficialia')
    descripcion = models.CharField(max_length=250,blank=False,verbose_name='Descripción')
    n_serie = models.CharField(max_length=100, blank=False, verbose_name='Número de serie')
    marca = models.CharField(max_length=20, blank=False, verbose_name='Marca')
    modelo_i = models.CharField(max_length=50, blank=True, verbose_name='Modelo')
    f_factura = models.DateField(blank=True, verbose_name='Fecha de factura')
    n_factura = models.CharField(max_length=10,blank=True, verbose_name='Número de factura')
    orden_c = models.CharField(max_length=8,blank=True, verbose_name='Orden de compra')
    proveedor_c = models.CharField(max_length=25,blank=True, verbose_name='Proveedor')
    centro_c = models.CharField(max_length=6,blank=True, verbose_name='Centrocosto')
    comentarios = models.TextField(blank=True, verbose_name='Comentarios')
    lugar = models.ForeignKey(Location,on_delete=models.CASCADE, verbose_name='Lugar')
    funcionario = models.ForeignKey(User,on_delete=models.CASCADE, verbose_name='Funcionario')
    active = models.BooleanField(default=True, verbose_name='Activo')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.n_oficialia+ '   '+self.descripcion