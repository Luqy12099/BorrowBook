from django.db import models

# Create your models here.
class author(models.Model):
    first_name = models.CharField(max_length=200)
    middle_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200, null= True)
    is_active = models.BooleanField(default= True, help_text= "0 not active; 1 active")

    def __str__(self):
        return self.first_name
    
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
    total_page = models.IntegerField(null= True)
    isbn = models.CharField(max_length=50, null= True)
    published_date = models.DateField(null= True)
    is_active = models.BooleanField(default= True, help_text= "0 not active; 1 active")

    def __str__(self):
        return self.tittle
