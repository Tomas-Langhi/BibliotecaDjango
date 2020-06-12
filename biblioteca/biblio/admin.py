from django.contrib import admin
from biblio.models import * 

class UsuarioAdmin(admin.ModelAdmin):

    #Para excluir atributos
    #exclude = ['telefono']
    
    #Para armar pestañas separando los datos
    fieldsets = (
        ('Informacion Personal',{
            'fields': ('nombre', 'direccion', 'telefono')
        }),
        ('Detalle de alquileres',{
            'fields': ('ejemplar',)
        }),
    )

    #Para previsualizar datos
    list_display = ['nombre', 'apellido','telefono']

# Register your models here.
admin.site.register(Autor,);
admin.site.register(Libro,);
admin.site.register(Usuario, UsuarioAdmin,);
admin.site.register(Ejemplar,);
