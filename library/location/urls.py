from django.urls import path
from . import  views

urlpatterns = [
    path("", views.location_read, name = "location_read"),
    path("create/", views.location_create, name = "location_create"),
    path("<int:id>", views.location_update, name = "location_update"),
    path("<int:id>/delete/", views.location_delete, name = "location_delete"),
]
