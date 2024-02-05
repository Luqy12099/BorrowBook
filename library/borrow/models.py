from django.db import models
from register.models import User
from book.models import book
# Create your models here.

class borrow(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(book, on_delete=models.CASCADE)
    borrow_request_date = models.DateField(auto_now_add=True)
    return_date = models.DateField(null=True)
    is_approved = models.BooleanField(default= False)
    is_returned = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} borrowed {self.book.tittle}"