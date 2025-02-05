from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User


class Categoria(models.Model):
    name=models.CharField(max_length=100,verbose_name="nombre")
    created=models.DateTimeField(auto_now_add=True,verbose_name="Fecha de Creacion")
    updated=models.DateTimeField(auto_now=True,verbose_name="Fecha de Edición")

    class Meta:
        verbose_name="Categoria"
        verbose_name_plural="Categorias"

    def __str__(self):
        return self.name
    
class Producto(models.Model):
    name=models.CharField(max_length=100,verbose_name="nombre")
    detail=models.TextField(verbose_name="detalle")
    image = models.ImageField(upload_to="producto", null=True, blank=True,
        verbose_name="Imagen")
    published=models.DateTimeField(default=now,verbose_name="Fecha Publicación")
    author=models.ForeignKey(User,on_delete=models.CASCADE,verbose_name="autor")
    category=models.ManyToManyField(Categoria,verbose_name="categoria")
    created=models.DateTimeField(auto_now_add=True,verbose_name="Fecha de Creacion")
    updated=models.DateTimeField(auto_now=True,verbose_name="Fecha de Edición")

    class Meta:
        verbose_name="Producto"
        verbose_name_plural="Productos"

    def __str__(self):
        return self.name
