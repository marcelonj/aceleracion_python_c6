from django.db import models
from django.utils.text import slugify
from tinymce.models import HTMLField

class Category(models.Model):
    nombre = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=255)
    slug =models.SlugField(max_length=30, unique=True)
    color = models.CharField(max_length=30)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.nombre)
        super(Category, self).save(*args, **kwargs)

class Post(models.Model):
    titulo = models.CharField(max_length=50)
    autor = models.CharField(max_length=30)
    contenido = HTMLField()
    descripcion = models.CharField(max_length=255)
    creacion = models.DateTimeField(auto_now_add=True)
    actualizacion = models.DateTimeField(auto_now_add=True)
    categorias = models.ManyToManyField(Category, through='PostCategory')
    estado = models.CharField(
        max_length=20,
        choices= [
            ('borrador', 'Borrador'),
            ('publicado', 'Publicado'),
            ('eliminado', 'Eliminado'),
        ],
        default='Publicado',
        blank=True,
    )
    slug = models.SlugField(max_length=50, unique=True)
    imagen = models.ImageField(upload_to='app_blog', default='app_blog/default.png', blank=True)
    contador_comentarios = models.IntegerField(default=0)
    contador_visualizaciones = models.IntegerField
    contador_likes = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.titulo)
        super(Post, self).save(*args, **kwargs)
    
class PostCategory(models.Model):
    articulo = models.ForeignKey(Post, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Category, on_delete=models.CASCADE)

class Comment(models.Model):
    autor = models.CharField(max_length=30)
    contenido = models.TextField()
    creacion = models.DateTimeField(auto_now_add=True)
    actualizacion = models.DateTimeField(auto_created=True)
    articulo = models.OneToOneField(Post, on_delete=models.SET_NULL, null=True)
    contador_likes = models.IntegerField(default=0)