from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from register.models import User
from .form import form_edit_user, AdminLibraryForm
from .models import admin_library

#region ================================= USER MANAGEMENT AREA ==========================================================================

@login_required()
def user_read(response):
    if response.user.role != 'superadmin':
        return HttpResponseRedirect('/')
    data = User.objects.all()
    return render(response, "managementUser/user_read.html", {"data":data})

@login_required()
def user_update(response, id):
    #Autorisation
    if response.user.role != 'superadmin':
        return HttpResponseRedirect('/')

    data = get_object_or_404(User, id=id)
    data2 = admin_library.objects.filter(user=data).first()
    old_role = data.role
    form = form_edit_user(response.POST or None, instance=data)
    form2 = AdminLibraryForm(response.POST or None, instance=data2)

    if response.method =="POST":
        if form.is_valid():
            instance = form.save(commit=False)  

            # Delete admin_library, when role change from admin to another
            if old_role != instance.role and instance.role != 'admin':
                admin = get_object_or_404(admin_library, user = instance)
                admin.delete()

            # Save form2 (AdminLibraryForm) only if the role is 'admin'
            if instance.role == 'admin' and form2.is_valid():
                admin_library_instance = form2.save(commit=False) # Prevent premature saving
                admin_library_instance.user = instance
                
                if not admin_library_instance.decsription:
                    admin_library_instance.decsription = ''  # Set to None for empty strings
                
                admin_library_instance.save()

            instance.save()
            return redirect('user_read')

    return render(response, "managementUser/user_update.html", {"form":form, 'form2':form2})

@login_required()
def user_delete(response, id):
    user = get_object_or_404(User, id=id)
    
    # Check if the user has permission to delete this ToDoList item
    if response.user.role == 'superadmin':
        user.delete()
        return redirect('user_read')
    else:
        return HttpResponseRedirect('/')

#endregion ================================= USER MANAGEMENT AREA ==========================================================================

#region ================================= LIBRARY ADMIN AREA ==========================================================================



#endregion ================================= LIBRARY ADMIN AREA ==========================================================================