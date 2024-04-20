from django.contrib import admin
from app_blog.models import *


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ("user", "fecha_nac", "bio", "github")
    exclude = ("fecha_nac", "bio", "github")


# Formulario relacionado por Clave Foránea
class CommentInline(admin.TabularInline):
    model = Comment
    extra = 1  # Cantidad de formularios renderizados por defecto
    fields = ("autor", "contenido", "contador_likes")


# Formulario relacionado por relación ManyToMany
class CategoryInline(admin.TabularInline):
    model = PostCategory
    extra = 1


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        "titulo",
        "autor",
        "contenido",
        "descripcion",
        "creacion",
        "actualizacion",
        "estado",
        "slug",
        "imagen",
        "contador_comentarios",
        "contador_visualizaciones",
        "contador_likes",
    )
    exclude = (
        "slug",
        "creacion",
        "actualizacion",
        "contador_comentarios",
        "contador_visualizaciones",
        "contador_likes",
    )
    inlines = [CommentInline, CategoryInline]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("nombre", "descripcion", "slug", "color")
    exclude = ("slug",)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = (
        "autor",
        "contenido",
        "creacion",
        "actualizacion",
        "articulo",
        "contador_likes",
    )
    exclude = ("creacion", "actualizacion")
