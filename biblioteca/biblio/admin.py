from django.contrib import admin
from biblio.models import * 

#Para excluir atributos
#exclude = ['telefono']

class UsuarioAdmin(admin.ModelAdmin):
    #Para previsualizar datos
    list_display = ['nombre', 'apellido','telefono', 'get_age', 'mayor',]
    
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

class LibroInline(admin.TabularInline):
    model = Libro

class AutorAdmin(admin.ModelAdmin):
    #Para previsualizar datos
    list_display = ['nombre', 'apellido', 'get_age', 'mayor',]
    search_fields = ['nombre', 'apellido',]

    #Para poder editar los datos del libro desde el autor
    inlines = [ LibroInline,]

class LibroAdmin(admin.ModelAdmin):

    #Para previsualizar datos
    list_display = ['titulo', 'editorial']

class EjemplarAdmin(admin.ModelAdmin):
    #Para previsualizar datos
    list_display = ['libro', 'localizacion']

    #Para utilizarlo se necesita deshabilitar el django-jet
    #filter_horizontal = ('libro',)

# Register your models here.
admin.site.register(Autor, AutorAdmin,);
admin.site.register(Libro, LibroAdmin),;
admin.site.register(Usuario, UsuarioAdmin,);
admin.site.register(Ejemplar, EjemplarAdmin,);
