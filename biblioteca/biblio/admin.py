from django.contrib import admin
from biblio.models import * 

class UsuarioAdmin(admin.ModelAdmin):

    #Para excluir atributos
    #exclude = ['telefono']

    #Para previsualizar datos
    list_display = ['nombre', 'apellido','telefono', 'get_age',]
    
    #Para armar pestañas separando los datos
    fieldsets = (
        ('Informacion Personal',{
            'fields': ('nombre','apellido','edad')
        }),
        ('Contacto',{
            'fields': ('direccion', 'telefono')
        }),
        ('Detalle de alquileres',{
            'fields': ('ejemplar',)
        }),
    )
"""
    #Para diferenciar entre adultos y menores
    def mayor(self):
        if self.edad > 18:
            return True
        else:
            False
    mayor.boolean = True
    mayor.short_description = 'Es adulto'

    #cambia de color
    def color(self):
        if edad > 18:
            return "<b style = 'color: green;'>Aprobado</b>"
        else:
            return "<b style = color: red;'>Desaprobado</b>"
    #color.allow_tag = True
"""



class AutorAdmin(admin.ModelAdmin):
    #Para previsualizar datos
    list_display = ['nombre', 'apellido', 'get_age',]

class LibroAdmin(admin.ModelAdmin):
    #Para previsualizar datos
    list_display = ['titulo', 'editorial']

class EjemplarAdmin(admin.ModelAdmin):
    #Para previsualizar datos
    list_display = ['libro', 'localizacion']

# Register your models here.
admin.site.register(Autor, AutorAdmin,);
admin.site.register(Libro, LibroAdmin),;
admin.site.register(Usuario, UsuarioAdmin,);
admin.site.register(Ejemplar, EjemplarAdmin,);
