# -*- coding: utf-8 -*-
from django.http import HttpResponse, HttpResponseRedirect
from usuario.models import *
from django.shortcuts import render, get_object_or_404
from django.template import RequestContext
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
import datetime, re

from urllib.parse import urlencode

from django.db.models import Q

from django.shortcuts import redirect

from django.shortcuts import render
from django.http import HttpResponse
import logging
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404

# Create your views here.

# Create your views here.


def borrar(request, tweet_id):

	if request.user.is_authenticated:
		try :
			t = get_object_or_404(Receta, id = tweet_id)
			if t.user == request.user: #El usuario actual es el propietario del tweeet
				
				t.delete()
			else :
				return HttpResponse("Eso no te pertenece")
					
			return HttpResponseRedirect('/usuario/')
		
		except: 
			return HttpResponse("Error al eliminar")

	else : 
		return redirect('/usuario/login')





def buscar(request):

	if request.user.is_authenticated:
		if 'busqueda' in request.GET:
			
			t = Receta.objects.filter(Q(contenido__icontains = request.GET['busqueda'])|Q(user__username = request.GET['busqueda'])).order_by('-fecha')
			return render(request,'usuario/index.html',
			{
				
				'recetas' : t,
				'logueado' : request.user,
				
				'busqueda' : request.GET['busqueda'],
				'nrecetas' : len(Receta.objects.filter(user = request.user)),
				'u_siguiendo' : len(Follow.objects.filter(activo = True,
				follower = Profile2.objects.get(user = request.user))),

				'u_seguidores' : len(Follow.objects.filter(activo = True,
				followed = request.user)),
			}, RequestContext(request))
		else:
			return HttpResponseRedirect('/usuario/')
	else : 
		return redirect('/usuario/login')
def conf(request):


	if request.user.is_authenticated:

		u = request.user
		p = get_object_or_404(Profile2, user = u)
		try:
			if not u.check_password(request.POST['oldpass']):
				return render(request,'usuario/conf.html',{
					'mensaje' : '<h3>Introduzca su contraseña actual correctamente</h3>',
					'nombre' : u.first_name,
					'apellido' : u.last_name,
					'email' : u.email,
					'ubicacion' : p.ubicacion,
					'bio' : p.frase,
					'avatares':p.imagen,
					'logueado' : request.user,
					'nrecetas' : len(Receta.objects.filter(user = request.user)),
					'u_siguiendo' : len(Follow.objects.filter(activo = True,
						follower = Profile2.objects.get(user = request.user))),
					'u_seguidores' : len(Follow.objects.filter(activo = True,
						followed = request.user)),
					}, RequestContext(request))
			if request.POST['procesa'] == 'profile':
				u.first_name = request.POST['firstname']
				u.last_name = request.POST['lastname']
				u.email = request.POST['correo']
				u.save()

				p.ubicacion = request.POST['ubicacion']
				p.frase = request.POST['bio']
				p.imagen = request.POST['avatares']
				p.save()
			elif request.POST['procesa'] == 'pass':
				if request.POST['pass'] == request.POST['pass2']:
					u.set_password(request.POST['pass'])
					u.save()
					logout(request)
					return HttpResponseRedirect('/usuario/')
				else:
					return render(request,'usuario/conf.html',{
						'mensaje' : 'Las contraseñas no coinciden',
						'nombre' : u.first_name,
						'apellido' : u.last_name,
						'email' : u.email,
						'ubicacion' : p.ubicacion,
						'bio' : p.frase,
						'avatares':p.imagen,
						'logueado' : request.user,
						'nrecetas' : len(Receta.objects.filter(user = request.user)),
						'u_siguiendo' : len(Follow.objects.filter(activo = True,
							follower = Profile2.objects.get(user = request.user))),
						'u_seguidores' : len(Follow.objects.filter(activo = True,
							followed = request.user)),
						}, RequestContext(request))
			return HttpResponseRedirect('/usuario/configuracion/')
		except KeyError:
			return render(request,'usuario/conf.html',{
				'nombre' : u.first_name,
				'apellido' : u.last_name,
				'email' : u.email,
				'ubicacion' : p.ubicacion,
				'bio' : p.frase,
				'avatares':p.imagen,
				'logueado' : request.user,
				'nrecetas' : len(Receta.objects.filter(user = request.user)),
				'u_siguiendo' : len(Follow.objects.filter(activo = True,
				follower = Profile2.objects.get(user = request.user))),
				'u_seguidores' : len(Follow.objects.filter(activo = True,
				followed = request.user)),
				}, RequestContext(request))
	else : 
		return redirect('/usuario/login')	



"""def follow(request):
	if request.user.is_authenticated:

		try:
			user = request.POST['user']
		except KeyError:
			return HttpResponseRedirect('/usuario/')
		
		u = get_object_or_404(User, username = user)
		f = Follow.objects.filter(follower__user =request.user, followed = u)
		if f: #Ya hay algun follow del mismo usuario, se cambia el activo en vez de crear uno nuevo
			f = f[0]
			f.activo = not f.activo #Si lo esta siguiendo lo deja de seguir, sino lo sigue
			f.save()
		else: #Crea un nuevo objecto folllow
			f = Follow.objects.create(
				fecha = datetime.datetime.now(),
				activo = True,
				follower = Profile2.objects.get(user = request.user),
				followed = u
			)
			f.save()
		return HttpResponseRedirect('/usuario/profile/%s/' % user)
	else : 
		return redirect('/usuario/login')"""

def follow(request):
	if request.user.is_authenticated:

		try:
			user = request.POST['seguir']
		except KeyError:
			return HttpResponseRedirect('/usuario/')
		
		u = get_object_or_404(User, username = user)
		f = Follow.objects.filter(follower__user =request.user, followed = u)
		if f: #Ya hay algun follow del mismo usuario, se cambia el activo en vez de crear uno nuevo
			f = f[0]
			f.activo = not f.activo #Si lo esta siguiendo lo deja de seguir, sino lo sigue
			f.save()
		else: #Crea un nuevo objecto folllow
			f = Follow.objects.create(
				fecha = datetime.datetime.now(),
				activo = True,
				follower = Profile2.objects.get(user = request.user),
				followed = u
			)
			f.save()
		return HttpResponseRedirect('/usuario/seguirprueba/%s/' % user)
	else : 
		return redirect('/usuario/login')

def index(request):

	
	if request.user.is_authenticated:
		
		p = Profile2.objects.get(user = request.user)
		users = Follow.objects.filter(follower = p, activo = True) #Busca los users que sigue el usuario
		users = [u.followed for u in users] #Hace que users sea un array de los usuarios que sigue
		users.append(request.user) #Le agrega el usuario actual
		tweets_ = Receta.objects.filter(user__in = users, activo = True).order_by('-fecha')

		#Procesa retweets
		tweets = []
		for t in tweets_:
			tweets.append(t)

		return render(request,'usuario/index.html',
		{
			'logueado' : request.user,

			'recetas' : tweets,
			'nrecetas' : len(Receta.objects.filter(user = request.user)),
			'u_siguiendo' : len(Follow.objects.filter(activo = True,
				follower = Profile2.objects.get(user = request.user))),
			'u_seguidores' : len(Follow.objects.filter(activo = True,
				followed = request.user)),
		}, RequestContext(request))
	else:
		return HttpResponseRedirect('/usuario/login/')
		
"""        
f = Follow.objects.filter(follower__user =request.user, followed = u)
		if f: #Ya hay algun follow del mismo usuario, se cambia el activo en vez de crear uno nuevo
			f = f[0]
			f.activo = not f.activo #Si lo esta siguiendo lo deja de seguir, sino lo sigue
			f.save()
		else: #Crea un nuevo objecto folllow
			f = Follow.objects.create(
				fecha = datetime.datetime.now(),
				activo = True,
				follower = Profile2.objects.get(user = request.user),
				followed = u
			)
			f.save()        
        """
def profile(request, username):
	if request.user.is_authenticated:
        
		u = get_object_or_404(User, username=username)
  
		#tweets = Tweet.objects.filter(user = u).order_by('-fecha')
		recetas_ = u.receta_set.all().filter(activo = True).order_by('-fecha')
		m = request.user
		#Procesa retweets
		recetas = []
		for t in recetas_:
			recetas.append(t)
		p = Profile2.objects.get(user = request.user) #El perfil del usuario
		pp = Profile2.objects.get(user = u) #El perfil del usuario
		f = Follow.objects.filter(followed = m, activo = True) #Los objetos follow activos
		f = [user.followed for user in f] #Convierte f a un array de usuarios que sigue
     
		return render(request,'usuario/profile.html',
		{
            'avatares':p.imagen,
            'avatares2':pp.imagen,
			'following' : (u in f),
			'length' : len(recetas),
			'logueado' : request.user,
			'profile' : get_object_or_404(Profile2, user=u),
			'recetas' : recetas,
			'user' : u,
			'siguiendo' : (f),
			'seguidores' : Follow.objects.filter(activo = True, followed = u),
			'nrecetas' : len(Receta.objects.filter(user = request.user)),
			'u_siguiendo' : len(Follow.objects.filter(activo = True,
				follower = Profile2.objects.get(user = request.user))),
			'u_seguidores' : len(Follow.objects.filter(activo = True,
				followed = request.user)),
		}, RequestContext(request))
	else:
		return redirect('/usuario/login')	
	

def register(request):
    if request.user.is_authenticated:
        return redirect('/usuario/')

    else : 
        try : 
            try:
                request.POST['procesa']
                try:
                    if not re.match('^[a-zA-Z0-9_]+$', request.POST['login']):
                        return render(request,
                            'usuario/login.html',
                            {'mensaje_register' : 'El nombre de usuario solo puede contener letras, numeros y _'},
                            RequestContext(request))
                    if not re.match('^[^@]+@[^@]+$', request.POST['correo']):
                        return render(request,
                            'usuario/login.html',
                            {'mensaje_register' : 'Ingrese un email valido'},
                            RequestContext(request))
                    if request.POST['pass'] != request.POST['pass2']:
                        return render(request,
                            'usuario/login.html',
                            {'mensaje_register' : 'No coincide el password'},
                            RequestContext(request))
                    if User.objects.filter(username = request.POST['login']):
                        return render(request,
                            'usuario/login.html',
                            {'mensaje_register' : 'El usuario ya existe'},
                            RequestContext(request))
                    
                    
                    username = request.POST['login']
                    email = request.POST['correo']
                    if email and User.objects.filter(email=email).exclude(username=username).exists():
                        return render(request,
                            'usuario/login.html',
                            {'mensaje_register' : 'el email esta en uso'},
                            RequestContext(request))
                    
                    
                    else:
                        u = User.objects.create_user(
                            request.POST['login'],
                            request.POST['correo'],
                            request.POST['pass'],
                        )
                        u.first_name = request.POST['firstname']
                        u.last_name = request.POST['lastname']

                    #Comprueba que existan las otras claver
                    request.POST['ubicacion']
                    request.POST['bio']

                    u.save()

                    p = Profile2.objects.create(
                        user = u,
                        frase = request.POST['bio'],
                        ubicacion = request.POST['ubicacion'],
                        imagen = ''
                    )
                    p.save()
                    return HttpResponseRedirect('/usuario/')
                except KeyError:
                    return render(request,'usuario/login.html',
                        {'message' : 'Rellene todos los campos'},
                        RequestContext(request))
            except KeyError:
                return render(request,'usuario/login.html', {}, RequestContext(request))
        except:    
            return redirect('/usuario/')  
            
def seguidores(request, method, username):
	if request.user.is_authenticated:

		u = get_object_or_404(User, username = username)
		p = get_object_or_404(Profile2, user__username = username)
		if method == 'seguidores':
			u = Follow.objects.filter(followed = u, activo = True).order_by('-fecha')
			u = [f.follower.user for f in u]
		elif method == 'siguiendo':
			u = Follow.objects.filter(follower = p, activo = True).order_by('-fecha')
			u = [f.followed for f in u]
		
		for n in range(len(u)):
			u[n].profile2 = get_object_or_404(Profile2, user = u[n])

		return render(request,
		'usuario/seguidores.html',
		{
			'logueado' : request.user,
			'users' : u,
			'nrecetas' : len(Receta.objects.filter(user = request.user)),
			'u_siguiendo' : len(Follow.objects.filter(activo = True,
				follower = Profile2.objects.get(user = request.user))),
			'u_seguidores' : len(Follow.objects.filter(activo = True,
				followed = request.user)),
		}, RequestContext(request))
	else : 
		return redirect('/usuario/login')	

def seguirprueba(request, username):
    if request.user.is_authenticated:
        u = get_object_or_404(User, username=username)
		#tweets = Tweet.objects.filter(user = u).order_by('-fecha')
        recetas_ = u.receta_set.all().filter(activo = True).order_by('-fecha')
        m = request.user
		#Procesa retweets
        recetas = []
        for t in recetas_:
            recetas.append(t)
        p = Profile2.objects.get(user = request.user) #El perfil del usuario
        f = Follow.objects.filter(followed = m, activo = True) #Los objetos follow activos
        f = [user.followed for user in f] #Convierte f a un array de usuarios que sigue
        return render(request,'usuario/seguirprueba.html',
		{
			'following' : (u in f),
			'length' : len(recetas),
			'logueado' : request.user,
            
			'profile' : get_object_or_404(Profile2, user=u),
			'recetas' : recetas,
			'user' : u,
			'siguiendo' : (f),
			'seguidores' : Follow.objects.filter(activo = True, followed = u),
			'nrecetas' : len(Receta.objects.filter(user = request.user)),

			'u_siguiendo' : len(Follow.objects.filter(activo = True,
				follower = Profile2.objects.get(user = request.user))),

			'u_seguidores' : len(Follow.objects.filter(activo = True,
				followed = request.user)),
		}, RequestContext(request))
    else: 
        return redirect('/usuario/login')	
	
    return render(request,'usuario/seguirprueba.html')

def nevera_login(request):
	if request.user.is_authenticated:
		return redirect('/indexex/')	

	else : 
		return render(request,'usuario/login.html',
			{},
			RequestContext(request))

def nevera_logout(request):
	logout(request)
	return HttpResponseRedirect('/usuario/')


def login_process(request):
	if request.user.is_authenticated:
		return redirect('/indexex/')	

	else : 
		try:
			user = authenticate(username = request.POST['user'],
				password = request.POST['pass'])
		except KeyError:
			return render(request,'usuario/login.html',{
				'mensaje_login' : 'Rellene todos los campos',
				},RequestContext(request)) 
		if user is not None:
			#User y pass correctos
			if user.is_active:
				login(request, user)
			else:
				return render(request,'usuario/login.html',{
					'mensaje_login' : 'El usuario ha sido eliminado',
				},RequestContext(request))
		else:
			return render(request,'usuario/login.html',{
				'mensaje_login' : 'Ingrese el usuario y clave correctamente',
			},RequestContext(request))
		return HttpResponseRedirect('/indexex/')

def users_existentes(request):
    if request.method == "GET":
        raise Http404("URL doesn't exists")
    else:   
        response_data = {}
        login = request.POST["login"]
        user = None
        try:
            try:
                user = User.objects.get(username=login)
            except ObjectDoesNotExist as e:
                pass
            except Exception as e:
                raise e
            if not user:
                response_data["is_success"] = True
            else:
                response_data["is_success"] = False
        except Exception as e:
            response_data["is_success"] = False
            response_data["msg"] = "Some error occurred. Please let Admin know."

        return JsonResponse(response_data)    
    
def correos_existentes(request):
    if request.method == "GET":
        raise Http404("URL doesn't exists")
    else:   
        response_data = {}
        correo = request.POST["correo"]
        correouser = None
        try:
            try:
                correouser = User.objects.get(email=correo)
            except ObjectDoesNotExist as e:
                pass
            except Exception as e:
                raise e
            if not correouser:
                response_data["is_success"] = True
            else:
                response_data["is_success"] = False
        except Exception as e:
            response_data["is_success"] = False
            response_data["msg"] = "Some error occurred. Please let Admin know."

        return JsonResponse(response_data)        