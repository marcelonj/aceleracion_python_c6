from django.urls import path
from .views import *

urlpatterns = [
    path("", home, name="home"),
    path("login/", signin, name="login"),
    path("logout/", logout_view, name="logout"),
    path("search/", search_view, name="search_view"),
    path("create/", create_post, name="create_post"),
    path("post/", post_list, name="post_list"),
    path("post/<slug:post_slug>", view_post, name="view_post"),
    path("like_post/<slug:post_slug>", like_post, name="like_post"),
    path("like_comentario/<int:id><slug:post_slug>", like_comentario, name="like_comentario"),
    path("crear_cuenta/", crer_cuenta, name="crear_cuenta"),
    path("categories/", categories_list, name="lista_categorias"),
    path("category/<slug:category_slug>", ver_categoria, name="ver_categoria"),
    path("new_category", crear_categoria, name="crear_categoria")
]
