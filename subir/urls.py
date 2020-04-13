from django.urls import path
from django.views.generic import TemplateView
from . import views



urlpatterns = [
    path('', views.index, name='index'),
    path('indexpk/<int:pk>', views.receta_detalle, name='receta_detalle'),
    path('registro/', views.registro, name='registro'),
    
    path('login/', views.login, name='login'),
    path('seccionveganos/', views.seccionveganos, name='seccionveganos'),
    
    
    path('subirrecetas/', views.subirrecetas_set, name='subirrecites'),
    path('perfil/', views.verperfil, name='verpefil'),
    path('categorias/',views.categorias,name='categorias'),
    path('ve_a_cocinar/',views.cocina,name='cocinar'),
    path('buscadoring/',views.buscadoring,name='buscadoring'),
    path('album/',views.album,name='album'),
    path('recuperar/',views.recuperar,name='recuperar'),
    path('done_recuperar/',views.done_recuperar,name='done_recuperar'),
    path('recuperacion_fallida/',views.fallida,name='recuperacion_fallada'),
    path('confirmar_recuperacion/',views.confirmacionrecuperar,name='confirmacion_recuperacion'),
    path('vista_receta/',views.vista_receta,name='vista_receta'),
    path('resultadosglobales/',views.resultadosglobales,name='resultadosglobales'),
    path('vista_perfil/',views.vista_perfil,name='vista_perfil'),
    path('fotoprueba/',views.fotoprueba,name='fotoprueba'),
    path('vistafotorecortada/',views.vistafotorecortada,name='vistafotorecortada')
    
   
]