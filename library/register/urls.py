from django.urls import path
from . import  views

urlpatterns = [
    path("register/", views.register, name = "register"),
    path("logout_view/", views.logout_view, name = "logout_view"),
    path("", views.base, name = "base"),
]