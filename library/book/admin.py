from django.contrib import admin
from .models import author, genre, publisher, book, stock
# Register your models here.
admin.site.register(author)
admin.site.register(genre)
admin.site.register(publisher)
admin.site.register(book)
admin.site.register(stock)
