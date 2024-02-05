from django.urls import path
from . import  views

urlpatterns = [
    path("<int:id>/", views.borrow_create, name = "borrow_create"),

    path("request/", views.borrow_request_read, name = "borrow_request_read"),
    path("request/<int:id>/delete/", views.borrow_request_delete, name = "borrow_request_delete"),

    path("request/<int:id>/", views.borrow_approval, name = "borrow_approval"),
    path("approved/", views.borrow_approval_read, name = "borrow_approval_read"),

    path("return/", views.borrow_return_read, name = "borrow_return_read"),
    path("return/<int:id>/", views.borrow_return, name = "borrow_return"),
]

