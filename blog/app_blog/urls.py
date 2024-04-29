from django.urls import path
from .views import *

urlpatterns = [
    path("", home, name="home"),
    path("login/", signin, name="login"),
    path("logout/", logout_view, name="logout"),
    path("search/", search_view, name="search_view"),
]
