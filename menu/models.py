from django.db import models

# Create your models here.
class categoria(models.Model):
    nombre = models.CharField(max_length=100,unique=True)
    Orden= models.PositiveSmallIntegerField(default=1)

    def __str__(self):
        return self.nombre

class meta():
    ordering = ['orden']


class plato(models.Model):
    nombre = models.CharField(max_length=100,unique=True)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=5, decimal_places=2)
    categoria = models.ForeignKey(categoria,on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre