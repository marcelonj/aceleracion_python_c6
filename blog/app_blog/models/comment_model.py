from django.db import models
from .post_model import Post


class Comment(models.Model):
    autor = models.CharField(max_length=30)
    contenido = models.TextField()
    creacion = models.DateTimeField(auto_now_add=True)
    actualizacion = models.DateTimeField(auto_created=True)
    articulo = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)
    contador_likes = models.IntegerField(default=0)
