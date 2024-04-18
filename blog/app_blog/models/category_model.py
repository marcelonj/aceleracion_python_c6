from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    nombre = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=255)
    slug = models.SlugField(max_length=30, unique=True)
    color = models.CharField(max_length=30)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.nombre)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.nombre
