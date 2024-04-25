from django.contrib import admin
from app_blog.models import *

from .admin_forms import CustomUserAdminForm


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    form = CustomUserAdminForm

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        # Reordenar los campos para colocar los campos del usuario al principio
        form.base_fields = dict(
            [
                ("username", form.base_fields["username"]),
                ("email", form.base_fields["email"]),
                ("first_name", form.base_fields["first_name"]),
                ("last_name", form.base_fields["last_name"]),
                ("password", form.base_fields["password"]),
                ("avatar", form.base_fields["avatar"]),
                ("dob", form.base_fields["dob"]),
                ("bio", form.base_fields["bio"]),
                ("github", form.base_fields["github"]),
            ]
            + list(form.base_fields.items())
        )
        return form

    list_display = ("get_username", "get_email", "dob", "github", "get_bio")

    def get_username(self, obj):
        return obj.user.username if obj.user else None

    get_username.short_description = "Usuario"

    def get_email(self, obj):
        return obj.user.email if obj.user else None

    get_email.short_description = "Email"

    def get_bio(self, obj):
        return obj.bio if obj.bio else "Sin biografía"

    get_bio.short_description = "Biografía"


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
