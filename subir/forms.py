from .models import Recetas,pruebafoto2

from django.forms import ModelForm

from django import forms

class Prb1Form(ModelForm):
    class Meta:
        model = Recetas
        fields = '__all__'
        
        
class pruebafotoform(ModelForm):
    class Meta:
        model = pruebafoto2
        fields = '__all__'
        
class ContactForm(forms.Form):
    Asunto = forms.CharField(max_length=100)
    Nombre = forms.CharField(max_length=100, required=False)
    Correo = forms.EmailField()
    Contenido = forms.CharField(widget=forms.Textarea)          
