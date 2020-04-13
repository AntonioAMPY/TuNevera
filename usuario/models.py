from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
import re
from urllib.parse import urlencode
from django.utils.timezone import datetime

from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.










class Receta(models.Model):
	def __unicode__(self):
		return self.contenido
		
	user = models.ForeignKey(User,on_delete=models.CASCADE,)

	fecha = models.DateTimeField()
	contenido = models.CharField(max_length = 140)
	
	activo = models.BooleanField(default  =True)
	respuesta = models.IntegerField(null = True, blank = True)
	def __int__(self): 
		return self.id



class Profile2(models.Model):
    def __unicode__(self):
        return str(self.user)
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='Profile2')
    frase = models.CharField(max_length = 160,null = True, blank = True)
    ubicacion = models.CharField(max_length = 50,null = True, blank = True)
    imagen = models.TextField(max_length = 255,null = True, blank = True) 
    def __str__(self): 
        return self.user.username



class Profile(models.Model):
	def __unicode__(self):
		return str(self.user)
	user = models.ForeignKey(User,on_delete=models.CASCADE,)
	frase = models.CharField(max_length = 160)
	ubicacion = models.CharField(max_length = 50)
	avatar = models.CharField(max_length = 160)



@receiver(post_save, sender=User)
def crear_usuario_perfil(sender, instance, created, **kwargs):
    if created:
        Profile2.objects.create(user=instance)

@receiver(post_save, sender=User)
def guardar_usuario_perfil(sender, instance, **kwargs):
    instance.Profile2.save()





class Follow(models.Model):
	fecha = models.DateTimeField()
	activo = models.BooleanField()
	follower = models.ForeignKey(Profile2,on_delete=models.CASCADE,)
	followed = models.ForeignKey(User,on_delete=models.CASCADE,)