from django.urls import path
from . import  views

urlpatterns = [
    path("author/", views.author_read, name = "author_read"),
    path("author/create/", views.author_create, name = "author_create"),
    path("author/<int:id>/", views.author_update, name = "author_update"),
    path("author/<int:id>/delete/", views.author_delete, name = "author_delete"),

    path("genre/", views.genre_read, name = "genre_read"),
    path("genre/create/", views.genre_create, name = "genre_create"),
    path("genre/<int:id>/", views.genre_update, name = "genre_update"),
    path("genre/<int:id>/delete/", views.genre_delete, name = "genre_delete"),
]

'''

    path("create/", views.location_create, name = "location_create"),
    path("<int:id>", views.location_update, name = "location_update"),
    path("<int:id>/delete/", views.location_delete, name = "location_delete"),
'''
