from django.shortcuts import render, redirect
from .models import Post, CustomUser, Comment
from django.contrib.auth.decorators import login_required
from .forms import NuevoPostForm, CommentForm

# Dependencias para iniciar y cerrar sesión
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout

# Dependencias para consultas complejas
from django.db.models import Q
from .models import Post


def home(request):
    num_articulos = Post.objects.filter(estado="publicado").count()
    articulos_recientes = Post.objects.filter(estado="publicado").order_by("creacion")[
        :3
    ]
    articulos_mas_vistos = Post.objects.filter(estado="publicado").order_by(
        "contador_visualizaciones"
    )[:3]

    context = {
        "num_articulos": num_articulos,
        "articulos_recientes": articulos_recientes,
        "articulos_mas_vistos": articulos_mas_vistos,
    }

    return render(request, "blog/home.html", context)


def signin(request):
    if request.user.is_authenticated:
        # Alternativa de la función redirect
        return HttpResponseRedirect(reverse("home"))

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            return render(
                request,
                "blog/signin.html",
                {"error": "Usuario o contraseña incorrectos"},
            )
    else:  # método GET
        return render(request, "blog/signin.html")


@login_required
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("login"))

def search_view(request):
    query = request.GET.get("query", "")
    if query:
        posts = Post.objects.filter(
            Q(titulo__icontains=query)
            | Q(contenido__icontains=query)
            | Q(descripcion__icontains=query),
            estado="publicado",  # Asegura que solo se busquen posts publicados
        )
    else:
        posts = Post.objects.none()  # No hay resultados si no hay consulta

    return render(
        request,
        "blog/search_results.html",
        {"articulos_filtrados": posts, "query": query},
    )

@login_required
def create_post(request):
    if request.method == "POST":
        form = NuevoPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.autor = CustomUser.objects.get(user=request.user)
            post.save()
            return redirect("home")
    else:  # Método GET
        form = NuevoPostForm()

    context = {"titulo": "Nuevo Post", "form": form, "submit": "Crear Post"}
    return render(request, "blog/create_form.html", context)

def view_post(request, post_slug):
    post = Post.objects.get(slug=post_slug)
    if request.method == "POST":
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.autor = CustomUser.objects.get(user=request.user)
            comment.articulo = post
            comment.save()
            return redirect("home")
    else:  # Método GET
        form = CommentForm()
    comentarios = Comment.objects.filter(articulo=post)

    context = {
        "post": post,
        "form": form,
        "comentarios": comentarios,
        "submit": "Publicar comentario",
    }
    return render(request, "blog/view_post.html", context=context)