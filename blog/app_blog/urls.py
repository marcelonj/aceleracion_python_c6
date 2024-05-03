from django.urls import path
from .views import *

urlpatterns = [
    path("", home, name="home"),
    path("login/", signin, name="login"),
    path("logout/", logout_view, name="logout"),
    path("search/", search_view, name="search_view"),
    path("create/", create_post, name="create_post"),
    path("post/<slug:post_slug>", view_post, name="view_post"),
]
