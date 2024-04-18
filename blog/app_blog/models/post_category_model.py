from django.db import models
from .category_model import Category
from .post_model import Post


class PostCategory(models.Model):
    articulo = models.ForeignKey(Post, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Category, on_delete=models.CASCADE)
