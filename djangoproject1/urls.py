from django.contrib import admin
from django.urls import path, include

from django.contrib.auth import views as auth_views

from .views import home
urlpatterns = [
    path("", home, name="home"),

    path("admin/", admin.site.urls),

    path("movies/", include("movies.urls")),

    path("account/", include("accounts.urls")),

    path(
        "account/login/",
        auth_views.LoginView.as_view(
            template_name="registration/login.html"
        ),
        name="login",
    ),

    path(
        "account/logout/",
        auth_views.LogoutView.as_view(),
        name="logout",
    ),
]