from django.shortcuts import render
from .models import Post

def home(request):
    num_articulos = Post.objects.filter(estado="publicado").count()
    articulos_recientes = Post.objects.filter(estado="publicado").order_by("creacion")[:3]
    articulos_mas_vistos = Post.objects.filter(estado="publicado").order_by("contador_visualizaciones")[:3]

    context = {
        "num_articulos": num_articulos,
        "articulos_recientes": articulos_recientes,
        "articulos_mas_vistos": articulos_mas_vistos,
    }

    return render(request, "blog/home.html", context)

# Create your views here.
