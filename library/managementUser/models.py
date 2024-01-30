from django.db import models
from register.models import User
from location.models import library_location
# Create your models here.

class admin_library(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    library_location = models.ForeignKey(library_location, on_delete=models.CASCADE)
    decsription = models.CharField(max_length=200, null = True)
    is_active = models.BooleanField(default= True)

    def __str__(self):
        return "Admin # " + str(self.library_location.name)
