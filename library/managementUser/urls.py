from django.urls import path
from . import  views

urlpatterns = [
    path("", views.user_read, name = "user_read"),
    path("<int:id>/", views.user_update, name = "user_update"),
    path("delete/<int:id>/", views.user_delete, name = "user_delete"),
]
