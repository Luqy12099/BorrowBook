from django.db import models
# Create your models here.

class library_location(models.Model):
    name = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    decsription = models.CharField(max_length=200, null = True)
    is_active = models.BooleanField(default= True)

    def __str__(self):
        return self.name
