from colorsys import ONE_THIRD
from pickle import TRUE
from xml.etree.ElementTree import TreeBuilder
from django.db import models
from django.db.models import F, Sum, FloatField
from models import Producto

from django.contrib.auth import get_user_model

# Create your models here.

User=get_user_model()

class Pedido(models.Model):

    user=models.ForeignKey(User, on_delete=models.CASCADE)
    created_at=models.DateTimefield(auto_now_add=True)

def __str__(self):
    return self.id

@property
def total(self):
    return self.lineapedido_set.aggregate(

    total=Sum(F("precio")*F("cantidad"), output_field=FloatField())
  
    )["total"]
class Meta:
    db_table='lineapedidos'
    vebose_name='Línea Pedido'
    verbose_name_plural='Líneas Pedidos'
    ordering=['id']

class LineaPedido(models.Model):

    user=models.ForeignKey(User, on_delete=models.CASCADE)
    producto_id=models.ForeignKey(Producto, on_delete=models.CASCADE)
    pedido_id=models.ForeignKey(Pedido, ONE_THIRD)
    cantidad=models.IntegerField(default=1)
    created_at=models.DateTiemField(auto_now_add=TreeBuilder)

    def __str__(self):
        return f'{self.cantidad} unidades de {self.producto.id.nombre}'

    class Meta:
        db_table='pedidos'
        verbose_name='pedido'
        verbose_name_plural='pedidos'
        ordering=['id']