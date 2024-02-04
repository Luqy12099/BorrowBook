from django.db import models
from location.models import library_location

# Create your models here.
class author(models.Model):
    first_name = models.CharField(max_length=200)
    middle_name = models.CharField(max_length=200, null= True)
    last_name = models.CharField(max_length=200, null= True)
    is_active = models.BooleanField(default= True, help_text= "0 not active; 1 active")

    def __str__(self):
        name = self.first_name
        if self.middle_name:
            name += " " + self.middle_name
        if self.last_name:
            name += " " + self.last_name
               
        return name
    
class genre(models.Model):
    name = models.CharField(max_length=200)
    is_active = models.BooleanField(default= True, help_text= "0 not active; 1 active")

    def __str__(self):
        return self.name
    
class publisher(models.Model):
    name = models.CharField(max_length=200)
    is_active = models.BooleanField(default= True, help_text= "0 not active; 1 active")

    def __str__(self):
        return self.name
    
class book(models.Model):
    tittle = models.CharField(max_length=200)
    author = models.ForeignKey(author, on_delete=models.CASCADE)
    genre = models.ForeignKey(genre, on_delete=models.CASCADE)
    publisher = models.ForeignKey(publisher, on_delete=models.CASCADE)
    library_location = models.ForeignKey(library_location, on_delete=models.CASCADE)
    stock = models.IntegerField(default=0)
    total_page = models.IntegerField(null= True)
    isbn = models.CharField(max_length=50, null= True)
    published_date = models.DateField(null= True)
    is_active = models.BooleanField(default= True, help_text= "0 not active; 1 active")

    def __str__(self):
        return self.tittle
