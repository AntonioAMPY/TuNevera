from django.contrib import admin

# Register your models here.
from .models import Profile,Follow,Profile2,Receta
admin.site.register(Profile)
admin.site.register(Follow)
admin.site.register(Profile2)
admin.site.register(Receta)