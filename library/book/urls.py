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

    path("publisher/", views.publisher_read, name = "publisher_read"),
    path("publisher/create/", views.publisher_create, name = "publisher_create"),
    path("publisher/<int:id>/", views.publisher_update, name = "publisher_update"),
    path("publisher/<int:id>/delete/", views.publisher_delete, name = "publisher_delete"),

    path("book/", views.book_read, name = "book_read"),
    path("book/create/", views.book_create, name = "book_create"),
    path("book/<int:id>/", views.book_update, name = "book_update"),
    path("book/<int:id>/delete/", views.book_delete, name = "book_delete"),
]

'''

    path("create/", views.location_create, name = "location_create"),
    path("<int:id>", views.location_update, name = "location_update"),
    path("<int:id>/delete/", views.location_delete, name = "location_delete"),
'''
