from django.db import models
from django import forms
from django.contrib.auth.models import User      
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
import re
from urllib.parse import urlencode
from django.utils.timezone import datetime
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import datetime    


class Recetas(models.Model):
    def __unicode__(self):
        return self.contenido
    listaalbum = (
            ('0','veganos'),
            ('1','comidas rapidas'),
            ('2','tercera edad'),
            ('3','niños'),
            ('5','desayuno'),
            ('6','almuerzo'),
            ('7','cena')
    )
    listacategorias = (
            ('0','Arroces'),
            ('1','Vegetales'),
            ('2','Frutas'),
            ('3','Mariscos'),
            ('4','Parva'),
            ('5','Bebidas'),
            ('6','san valentin'),
            ('7','hallowen'),
            ('8','navidad')
    )
    user = models.ForeignKey(User,on_delete=models.CASCADE,)
    ingredientes = models.CharField(max_length=100,null=False,blank=False)
    tags =  models.CharField(max_length=100,null=False,blank=False)
    nombre = models.CharField(max_length=100,null=False,unique=True)
    categorias = models.CharField(max_length=100,null=False,choices = listacategorias)
    album = models.CharField(max_length=100,null=False,choices = listaalbum)
    imagen = models.ImageField(blank=False)
    instrucciones = models.TextField(null=False)
    preptimes =  models.CharField(max_length=100,null=False)
    coctime = models.CharField(max_length=100,null=False)
    calorias =  models.CharField(max_length=100,null=True,blank=True )
    proteinas =  models.CharField(max_length=100,null=True,blank=True)
    carbohidratos =  models.CharField(max_length=100,null=True,blank=True)
    
    def __str__(self):
        return self.nombre
    class Meta:
        ordering = ('id',)

class RecetasAdministracion(models.Model):
    
    listaalbum = (
            ('veganos','veganos'),
            ('comidas rapidas','comidas rapidas'),
            ('tercera','tercera edad'),
            ('niños','niños'),
            ('desayuno','desayuno'),
            ('almuerzo','almuerzo'),
            ('cena','cena')
      )
    listacategorias = (
            ('Arroces','Arroces'),
            ('vegetales','Vegetales'),
            ('Frutas','Frutas'),
            ('Mariscos','Mariscos'),
            ('Parva','Parva'),
            ('Bebidas','Bebidas'),
            ('san Valentin','san valentin'),
            ('hallowen','hallowen'),
            ('navidad','navidad')
      )
    user = models.ForeignKey(User,on_delete=models.CASCADE,)
    nombre = models.CharField(max_length=100,null=False,unique=True)
    categorias = models.CharField(max_length=100,null=False,choices = listacategorias)
    album = models.CharField(max_length=100,null=False,choices = listaalbum)
    imagen = models.ImageField(upload_to='imagenes/' , blank=False)
    instrucciones = models.TextField()
    #tags =  models.CharField(max_length=100,null=False,blank=False)
    coctime = models.CharField(max_length=100,null=False)
    preptimes =  models.CharField(max_length=100,null=False)
    calorias =  models.CharField(max_length=100,null=True,blank=True)
    proteinas =  models.CharField(max_length=100,null=True,blank=True)
    fecha = models.DateTimeField(default=datetime.now(), blank=True)
    carbohidratos =  models.CharField(max_length=100,null=True,blank=True)


    def __str__(self):
        return self.nombre
    

    
    
    
class IngredientesAdministracion(models.Model):
    recetas = models.ForeignKey(RecetasAdministracion, on_delete=models.CASCADE , default = '' , related_name = "ingredientesadministracion" )
    cantidad = models.IntegerField(default=1,null=False)
    cuantificador = models.CharField(max_length=100,null=False)
    nombre = models.CharField(max_length=100,null=False)
    
    def __str__(self):
        return self.nombre        
    
    
class pruebafoto2(models.Model):
    img= models.TextField(null=False)
    
