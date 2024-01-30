from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .form import form_create_loc, form_edit_loc
from .models import library_location
from managementUser.models import admin_library

#region ================================= LOCATION AREA ==========================================================================

@login_required()
def location_create(response):
    #Authorisation
    if response.user.role != 'superadmin':
        return HttpResponseRedirect('/')
    
    if response.method == "POST":
        form = form_create_loc(response.POST)
        if form.is_valid():
            instance = form.save(commit=False)  # Prevent premature saving
            instance.save()
            return redirect('location_read')
    else:
        form = form_create_loc()
    return render(response, "location/location_create.html", {"form":form})

@login_required()
def location_read(response):
    data = library_location.objects.all()
    return render(response, "location/location_read.html", {"data":data})

@login_required()
def location_update(response, id):
    data = get_object_or_404(library_location, id=id)

    #Authorisation (Note: Change more specific)
    author = ['superadmin', 'admin']
    if response.user.role not in author:
        return HttpResponseRedirect('/')
    
    #Only admin from each library that can edit
    admin = admin_library.objects.filter(user = response.user.id).first()
    if response.user.role == 'admin' and data.id != admin.library_location.id:
        return HttpResponseRedirect('/')
    
    form = form_edit_loc(response.POST or None, instance=data)
    if response.method =="POST":
        if form.is_valid():
            instance = form.save(commit=False)  # Prevent premature saving

            # Handle empty values explicitly:
            if not instance.decsription:
                instance.decsription = ''  # Set to None for empty strings

            instance.save()
            return redirect('location_read')
    
    return render(response, "location/location_edit.html", {"form":form, "data":data})

@login_required()
def location_delete(response, id):
    data = get_object_or_404(library_location, id=id)

    #Authorisation
    author = ['superadmin']
    if response.user.role not in author:
        return HttpResponseRedirect('/')
    else:
        data.delete()
        return redirect('location_read') 
    
#endregion ================================= LOCATION AREA ==========================================================================
