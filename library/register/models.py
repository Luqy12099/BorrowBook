from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ROLE_CHOICES = [
        ('user', 'User'),
        ('admin', 'Admin'),
        ('superadmin', 'Super Admin'),
    ]

    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='user')

    class Meta(AbstractUser.Meta):
       swappable = 'AUTH_USER_MODEL'
    