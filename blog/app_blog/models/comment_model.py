from django.db import models
from .post_model import Post
from .custom_user_model import CustomUser


class Comment(models.Model):
    autor = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    contenido = models.TextField()
    creacion = models.DateTimeField(auto_now_add=True)
    actualizacion = models.DateTimeField(auto_created=True)
    articulo = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)
    contador_likes = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.articulo}({self.autor})"