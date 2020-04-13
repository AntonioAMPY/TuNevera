from django.conf.urls import url

from . import views
from django.urls import path

from django.contrib.auth import views as auth_views



from django.urls import reverse_lazy



from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

app_name = 'usuario'

urlpatterns = [


	path('', views.index,name='bienvenida'),
	
	path('login/', views.nevera_login),
	path('login/process/', views.login_process),
	path('logout/', views.nevera_logout),
    url(r'^users_existentes/$', views.users_existentes, name='users_existentes'),
    url(r'^correos_existentes/$', views.correos_existentes, name='correos_existentes'),
	path('register/', views.register),

	#para editar la cuenta(pass,name,username,ets)
	path('configuracion/', views.conf),

	path('profile/<username>/', views.profile,name='profile'),
	
	path('follow/', views.follow),
	path('seguirprueba/<username>/', views.seguirprueba),
	
	path('borrar/<tweet_id>/', views.borrar),

	path('buscar/', views.buscar),

	url('^(?P<method>(seguidores|siguiendo))/(?P<username>[a-zA-Z0-9\\_]+)/$', views.seguidores)

	



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)