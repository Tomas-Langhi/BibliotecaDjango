from django.contrib import admin
from biblio.models import * 

class UsuarioAdmin(admin.ModelAdmin):

    #Para excluir atributos
    #exclude = ['telefono']
    
    #Para armar pestañas separando los datos
    fieldsets = (
        ('Informacion Personal',{
            'fields': ('nombre','apellido','edad', 'direccion', 'telefono')
        }),
        ('Detalle de alquileres',{
            'fields': ('ejemplar',)
        }),
    )

    #Para diferenciar entre adultos y menores
    """
    def mayor(self):
        if edad > 18:
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
    #Para previsualizar datos
    list_display = ['nombre', 'apellido','telefono']

class AutorAdmin(admin.ModelAdmin):
    list_display = ('get_age', 'title')
    list_display_links = ('title',)
    filter_vertical = True

# Register your models here.
admin.site.register(Autor,);
admin.site.register(Libro,);
admin.site.register(Usuario, UsuarioAdmin,);
admin.site.register(Ejemplar,);
