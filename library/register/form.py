from django.contrib.auth.forms import UserCreationForm
from .models import User
from django.db import models

class form(UserCreationForm):
    email = models.EmailField()

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]