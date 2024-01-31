from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import author as auth, genre
from .form import form_create_author, form_edit_author, form_create_genre, form_edit_genre
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
