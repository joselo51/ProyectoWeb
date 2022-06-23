from django.db import models

# Create your models here.

class CategoriaProd(models.Model):
    nombre=models.CharField(max_length=50)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.nombre

class Meta:
    verbose_name="categoriaProd"
    verbose_name_plural="categoriasProd"

    
class Producto(models.Model):
    nombre=models.CharField(max_length=50)
    categorias=models.ForeignKey(CategoriaProd, on_delete=models.CASCADE)
    imagen=models.ImageField(upload_to="tienda", max_length = 100, null=True, blank=True)
    precio=models.DecimalField(max_digits=10, decimal_places=2)
    disponibilidad=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.nombre
    def __str__(self):
        return  self.nombre + ": $" + str(self.precio)
    
    

class Meta:
    verbose_name="producto"
    verbose_name_plural="productos"
