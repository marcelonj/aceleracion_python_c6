from django.contrib import admin
from .models import *

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'contenido', 'descripcion', 'creacion', 'actualizacion', 'estado', 'slug', 'imagen', 'contador_comentarios', 'contador_visualizaciones', 'contador_likes')
    exclude = ('slug', 'creacion', 'actualizacion', 'contador_comentarios', 'contador_visualizaciones', 'contador_likes')
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'slug', 'color')
    exclude = ('slug',)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('autor', 'contenido', 'creacion', 'actualizacion', 'articulo', 'contador_likes')
    exclude = ('creacion', 'actualizacion')