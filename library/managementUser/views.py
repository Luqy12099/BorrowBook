from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from register.models import User
from .form import form_edit_user
# Create your views here.

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
    form = form_edit_user(response.POST or None, instance=data)

    if response.method =="POST":
        if form.is_valid():
            instance = form.save(commit=False)  # Prevent premature saving
            instance.save()
            return redirect('user_read')

    return render(response, "managementUser/user_update.html", {"form":form, "data":data})

@login_required()
def user_delete(response, id):
    user = get_object_or_404(User, id=id)
    # Check if the user has permission to delete this ToDoList item
    print(response.user.role)
    if response.user.role == 'superadmin':
        user.delete()
        return redirect('user_read')
    else:
        return HttpResponseRedirect('/')

#endregion ================================= USER MANAGEMENT AREA ==========================================================================
