from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from .forms import Prb1Form,ContactForm,pruebafotoform
from .models import *
from django.core.mail import EmailMessage
from django.core.mail import send_mail
from django.core.paginator import Paginator , EmptyPage , PageNotAnInteger
from django.template import loader
from django.contrib.auth.models import Group
from django.db.models import Q
from django.db.models import Count
from usuario.models import Profile2 , Follow
from datetime import date
from django.contrib.auth.models import User
# Create your views here.

def index(request):
    if request.user.is_authenticated:
        u = request.user
        p = get_object_or_404(Profile2, user = u)
        Rec=RecetasAdministracion.objects.all()

        hoy = date.today()        
        filtro_fecha = RecetasAdministracion.objects.filter(fecha__lte = hoy).order_by('-fecha')
        cantidad_usuarios = User.objects.annotate(cantidad_us = Count('username'))
        cant = len(cantidad_usuarios)
        usuarios_ff = Follow.objects.filter(followed__lte = cant).order_by('-followed')[:3]
        #usuarios_recientes =  RecetasAdministracion.objects.annotate(num_seguidores = Count('ingredientesadministracion__nombre',filter=Q(ingredientesadministracion__nombre__in = texto_buscar))).order_by('-num_ingredientes')[:3]
        
        fofo = Follow.objects.all().values('followed')
        
        print('FFOFOOFOF',fofo)
                
        context={'Rec':Rec,'filtro_fecha': filtro_fecha,'usuarios_ff' : usuarios_ff ,'logueado' : request.user, 'avatares':p.imagen} 
        return render(request,'subir/indexex.html',context)
    else:
        return redirect('/usuario/login')
        
def verperfil(request):
    return render(request,'subir/perfil_usuario_logeado.html')

def categorias(request):
    if request.user.is_authenticated:
        u = request.user
        p = get_object_or_404(Profile2, user = u)
        context={'logueado':request.user,'avatares':p.imagen}
        return render(request,'subir/categorias.html',context)
    else:
        return redirect('/usuario/login')

def cocina(request):
    if request.user.is_authenticated:
        u = request.user
        p = get_object_or_404(Profile2, user = u)
        per=RecetasAdministracion.objects.all()
        context={'per':per,'logueado':request.user,'avatares':p.imagen} 
        return render(request,'subir/ve a cocinar2.html',context)
    else:
        return redirect('/usuario/login')

def album(request):
    if request.user.is_authenticated:
        u = request.user
        p = get_object_or_404(Profile2, user = u)
        context={'logueado':request.user,'avatares':p.imagen} 
        return render(request,'subir/album.html',context)
    else:
        return redirect('/usuario/login')
    """
    ('veganos','veganos'),
    ('comidas rapidas','comidas rapidas'),
    ('tercera','tercera edad'),
    ('niños','niños'),
    ('desayuno','desayuno'),
    ('almuerzo','almuerzo'),
    ('cena','cena')
    """
def seccionveganos(request):
    if request.user.is_authenticated:
        u = request.user
        p = get_object_or_404(Profile2, user = u)
        albunes=request.POST['inputalbum']
        tt = RecetasAdministracion.objects.filter(album=albunes)
        return render(request,'subir/seccionveganos.html',{'tt':tt,'logueado':request.user,'avatares':p.imagen})
    else:
        return redirect('/usuario/login')
            

def recuperar(request):
    return render(request,'subir/recuperar_contrasenia2.html')

def done_recuperar(request):
    return render(request,'subir/done_recuperar2.html')

def fallida(request):
    return render(request,'subir/recuperacion_fallada.html')

def confirmacionrecuperar(request):
    return render(request,'subir/confirmacion_recuperacion.html')

def registro(request):
    return render(request,'subir/REGISTRO.html')

def login(request):
    return render(request,'subir/index_login.html')

def vista_receta(request):
    if request.user.is_authenticated:
        u = request.user
        p = get_object_or_404(Profile2, user = u)
        context={'logueado':request.user,'avatares':p.imagen} 
        return render(request,'subir/vista_receta.html',context)
        def __str__(self):
            return "%s (%s)" % (
                self.nombre,
                ", ".join(ingrediente.nombre for ingrediente in self.Ingredientes.all()),
        )
    else:
        return redirect('/usuario/login')
    


def resultadosglobales(request):
    if request.user.is_authenticated:
        u = request.user
        p = get_object_or_404(Profile2, user = u)
        buscar=request.POST['buscador'].lower()
        pr=RecetasAdministracion.objects.filter(nombre__icontains=buscar)
        context={'pr':pr,'avatares':p.imagen,'logueado' : request.user}
        return render(request,'subir/resultadosglobales.html',context)
    else:
        return redirect('/usuario/login')
    
        
def receta_detalle(request,pk):
    if request.user.is_authenticated:
        u = request.user
        p = get_object_or_404(Profile2, user = u)
        Rec=RecetasAdministracion.objects.all()
        receta=get_object_or_404(RecetasAdministracion,pk=pk)
        context={'logueado':request.user,'receta':receta,'avatares':p.imagen} 
        return render(request,'subir/vista_receta.html',context)
    else:
        return redirect('/usuario/login')
    

def vista_perfil(request):
    if request.user.is_authenticated:
        context={'logueado':request.user} 
        return render(request,'subir/perfil_usuarios.html',context)
    else:
        return redirect('/usuario/login')

def subirrecetas_set(request):
    if request.user.is_authenticated:
        u = request.user
        p = get_object_or_404(Profile2, user = u)
        if request.method == 'POST':
            form_class = ContactForm
            form = Prb1Form(request.POST, request.FILES)
            form2 = ContactForm(request.POST or None)
            if form2.is_valid():
                data = form2.cleaned_data
                entrada = form.save(commit=True)
                send_mail(
                    data['Asunto'],#asunto del correo
                    data['Contenido'],#Nombre de quien lo envia
                    [data['Correo']], #Correo de quien lo envia
                    ['tunevera.official@gmail.com'],#para quien va el correo 
                fail_silently=False)
                entrada.save()
                return redirect('/indexex/')
        else:
            form = Prb1Form()
            form2 = ContactForm()


        template = loader.get_template('subir/subirrecetas.html')

        context = {
            'form' : form
            }

        return render(request, 'subir/subirrecetas.html', {'form':form, 'form2':form2,'logueado':request.user,'idlogueado':request.user.id,'avatares':p.imagen})
    else:
        return redirect('/usuario/login')

def fotoprueba(request):
    
    if request.method == 'POST':
        form = pruebafotoform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('../vistafotorecortada/')
    else:
        form = pruebafotoform()
        
    return render(request, 'subir/pruebafoto.html',{'form':form})
    
def buscadoring(request):
    if request.POST['texto_buscar']=="":
        return render(request,'subir/interrogantes.html')
    if request.method == "POST":
        texto_buscar = request.POST['texto_buscar'].split(',')
    else:
        texto_buscar = ''
    
    
    queryset  =IngredientesAdministracion.objects.filter(nombre =texto_buscar) 
    

    ll=RecetasAdministracion.objects.filter(ingredientesadministracion__nombre__in = texto_buscar).distinct()
    
    llcant=len(ll)
    print(llcant)
    
    print(queryset)
    

    
    if llcant == 1:
        xxx = RecetasAdministracion.objects.annotate(num_ingredientes = Count('ingredientesadministracion__nombre',filter=Q(ingredientesadministracion__nombre__in = texto_buscar))).order_by('-num_ingredientes')[:1]
        context = {'xxx': xxx}
        return render(request,'subir/prueba1.html',context)
    
    if llcant == 2:
        xxx = RecetasAdministracion.objects.annotate(num_ingredientes = Count('ingredientesadministracion__nombre',filter=Q(ingredientesadministracion__nombre__in = texto_buscar))).order_by('-num_ingredientes')[:2]
        context = {'xxx': xxx}
        return render(request,'subir/prueba2.html',context)
    
    if llcant >=3:
        xxx = RecetasAdministracion.objects.annotate(num_ingredientes = Count('ingredientesadministracion__nombre',filter=Q(ingredientesadministracion__nombre__in = texto_buscar))).order_by('-num_ingredientes')[:3]
        context = {'xxx': xxx}
        return render(request,'subir/prueba.html',context)
        
        


def vistafotorecortada(request):
    tt=pruebafoto2.objects.all()
    context={'tt':tt} 
    return render(request, 'subir/vistafotorecortada.html',{'tt':tt})