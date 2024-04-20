from django.db import models
from tinymce.models import HTMLField
from django.utils.text import slugify
from .category_model import Category
from .custom_user_model import CustomUser


class Post(models.Model):
    titulo = models.CharField(max_length=50)
    autor = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    contenido = HTMLField()
    descripcion = models.CharField(max_length=255)
    creacion = models.DateTimeField(auto_now_add=True)
    actualizacion = models.DateTimeField(auto_now_add=True)
    categorias = models.ManyToManyField(Category, through="PostCategory")
    estado = models.CharField(
        max_length=20,
        choices=[
            ("borrador", "Borrador"),
            ("publicado", "Publicado"),
            ("eliminado", "Eliminado"),
        ],
        default="Publicado",
        blank=True,
    )
    slug = models.SlugField(max_length=50, unique=True)
    imagen = models.ImageField(
        upload_to="app_blog", default="app_blog/default.png", blank=True
    )
    contador_comentarios = models.IntegerField(default=0)
    contador_visualizaciones = models.IntegerField
    contador_likes = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.titulo)
        super(Post, self).save(*args, **kwargs)
