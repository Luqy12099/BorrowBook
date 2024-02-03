from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import author as auth, genre, publisher, book, stock
from location.models import library_location
from managementUser.models import admin_library as admin_library_model
from .form import form_create_author, form_edit_author, form_create_genre, form_edit_genre
from .form import form_create_publisher, form_edit_publisher, form_create_book, form_edit_book
from .form import form_create_stock
# Create your views here.

#region ================================= AUTHOR AREA ==========================================================================

@login_required()
def author_read(response):
    data = auth.objects.all()
    return render(response, "book/author_read.html", {"data":data})

@login_required()
def author_create(response):
    #Authorisation
    author = ['superadmin', 'admin']
    if response.user.role not in author:
        return HttpResponseRedirect('/')
    
    if response.method == "POST":
        form = form_create_author(response.POST)
        if form.is_valid():
            instance = form.save(commit=False)  # Prevent premature saving
            instance.save()
            return redirect('author_read')
    else:
        form = form_create_author()
    return render(response, "book/author_create.html", {"form":form})

@login_required()
def author_update(response, id):
    data = get_object_or_404(auth, id=id)

    #Authorisation (Note: Change more specific)
    author = ['superadmin', 'admin']
    if response.user.role not in author:
        return HttpResponseRedirect('/')
    
    form = form_edit_author(response.POST or None, instance=data)
    if response.method =="POST":
        if form.is_valid():
            instance = form.save(commit=False)  # Prevent premature saving

            # Handle empty values explicitly:
            if not instance.middle_name:
                instance.middle_name = ''  # Set to None for empty strings
            if not instance.last_name:
                instance.last_name = '' 
            instance.save()
            return redirect('author_read')
    
    return render(response, "book/author_edit.html", {"form":form, "data":data})

@login_required()
def author_delete(response, id):
    data = get_object_or_404(auth, id=id)

    #Authorisation
    author = ['superadmin']
    if response.user.role not in author:
        return HttpResponseRedirect('/')
    else:
        data.delete()
        return redirect('author_read') 
#endregion ================================= AUTHOR AREA ==========================================================================

#region ================================= GENRE AREA ==========================================================================

@login_required()
def genre_read(response):
    data = genre.objects.all()
    return render(response, "book/genre_read.html", {"data":data})

@login_required()
def genre_create(response):
    #Authorisation
    author = ['superadmin', 'admin']
    if response.user.role not in author:
        return HttpResponseRedirect('/')
    
    if response.method == "POST":
        form = form_create_genre(response.POST)
        if form.is_valid():
            instance = form.save(commit=False)  # Prevent premature saving
            instance.save()
            return redirect('genre_read')
    else:
        form = form_create_genre()
    return render(response, "book/genre_create.html", {"form":form})

@login_required()
def genre_update(response, id):
    data = get_object_or_404(genre, id=id)

    #Authorisation (Note: Change more specific)
    author = ['superadmin', 'admin']
    if response.user.role not in author:
        return HttpResponseRedirect('/')
    
    form = form_edit_genre(response.POST or None, instance=data)
    if response.method =="POST":
        if form.is_valid():
            instance = form.save(commit=False)  # Prevent premature saving

            instance.save()
            return redirect('genre_read')
    
    return render(response, "book/genre_edit.html", {"form":form, "data":data})

@login_required()
def genre_delete(response, id):
    data = get_object_or_404(genre, id=id)

    #Authorisation
    author = ['superadmin']
    if response.user.role not in author:
        return HttpResponseRedirect('/')
    else:
        data.delete()
        return redirect('genre_read') 
#endregion ================================= GENRE AREA ==========================================================================

#region ================================= PUBLISHER AREA ==========================================================================

@login_required()
def publisher_read(response):
    data = publisher.objects.all()
    return render(response, "book/publisher_read.html", {"data":data})

@login_required()
def publisher_create(response):
    #Authorisation
    author = ['superadmin', 'admin']
    if response.user.role not in author:
        return HttpResponseRedirect('/')
    
    if response.method == "POST":
        form = form_create_publisher(response.POST)
        if form.is_valid():
            instance = form.save(commit=False)  # Prevent premature saving
            instance.save()
            return redirect('publisher_read')
    else:
        form = form_create_publisher()
    return render(response, "book/publisher_create.html", {"form":form})

@login_required()
def publisher_update(response, id):
    data = get_object_or_404(publisher, id=id)

    #Authorisation (Note: Change more specific)
    author = ['superadmin', 'admin']
    if response.user.role not in author:
        return HttpResponseRedirect('/')
    
    form = form_edit_publisher(response.POST or None, instance=data)
    if response.method =="POST":
        if form.is_valid():
            instance = form.save(commit=False)  # Prevent premature saving

            instance.save()
            return redirect('publisher_read')
    
    return render(response, "book/publisher_edit.html", {"form":form, "data":data})

@login_required()
def publisher_delete(response, id):
    data = get_object_or_404(publisher, id=id)

    #Authorisation
    author = ['superadmin']
    if response.user.role not in author:
        return HttpResponseRedirect('/')
    else:
        data.delete()
        return redirect('publisher_read') 

#endregion ================================= PUBLISHER AREA ==========================================================================

#region ================================= BOOK AREA ==========================================================================

@login_required()
def book_read(response):
    data = book.objects.all()
    return render(response, "book/book_read.html", {"data":data})

@login_required()
def book_create(response):
    #Authorisation
    author = ['superadmin', 'admin']
    if response.user.role not in author:
        return HttpResponseRedirect('/')
    
    if response.method == "POST":
        form = form_create_book(response.POST)
        form2 = form_create_stock(user=response.user, data=response.POST)

        if form.is_valid():
            instance = form.save(commit=False)  # Prevent premature saving
            instance.save()

            if form2.is_valid():
                stock_instance = form2.save(commit=False) # Prevent premature saving
                stock_instance.book = instance
                
                if not stock_instance.decsription:
                    stock_instance.decsription = ''  # Set to None for empty strings

                stock_instance.save()

            else:
                return redirect('book_read')
            
            return redirect('book_read')
        
    else:
        form = form_create_book()
        form2 = form_create_stock(user=response.user)
    return render(response, "book/book_create.html", {"form":form, "form2":form2})

@login_required()
def book_update(response, id):
    data = get_object_or_404(book, id=id)

    #Authorisation (Note: Change more specific)
    author = ['superadmin', 'admin']
    if response.user.role not in author:
        return HttpResponseRedirect('/')
    
    form = form_edit_book(response.POST or None, instance=data)
    if response.method =="POST":
        if form.is_valid():
            instance = form.save(commit=False)  # Prevent premature saving

            instance.save()
            return redirect('book_read')
    
    return render(response, "book/book_edit.html", {"form":form, "data":data})

@login_required()
def book_delete(response, id):
    data = get_object_or_404(book, id=id)

    #Authorisation
    author = ['superadmin']
    if response.user.role not in author:
        return HttpResponseRedirect('/')
    else:
        data.delete()
        return redirect('book_read')
#endregion ================================= BOOK AREA ==========================================================================

