from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from datetime import timedelta

from .models import borrow as br
from book.models import book
from managementUser.models import admin_library


#region ================================= BORROW REQUEST AREA ==========================================================================

@login_required()
def borrow_create(response, id):
    data_book = get_object_or_404(book, id=id)

    if response.method == "POST":
        if data_book.stock < 1:
            return redirect('book_read')
        
        data_book.stock = int(data_book.stock) - 1
        data_book.save()
        borrowed_book = br.objects.create(user=response.user, book=data_book)

        return redirect('book_read')
    
    return render(response, "borrow/borrow_create.html", {"book":data_book})


@login_required()
def borrow_request_read(response):
    header = "Borrow Request"

    #Authorisation (Note: Change more specific)
    if response.user.role == 'user':
        data = br.objects.filter(user = response.user, is_approved = False)

    elif response.user.role == 'admin':
        # Find admin library location
        admin_libraries = admin_library.objects.filter(user=response.user).first()
        library_locations = admin_libraries.library_location
        # Find book from library location
        data_book = book.objects.filter(library_location = library_locations)
        # Find borrowed book from book in each library location
        data = br.objects.filter(book__in=data_book, is_approved = False)

    elif response.user.role == 'superadmin':
        data = br.objects.filter(is_approved = False)

        
    return render(response, "borrow/borrow_request_read.html", {"data":data, "header_content":header})
    
@login_required()
def borrow_request_delete(response, id):
    data = get_object_or_404(br, id=id)

    #Authorisation
    if response.user.role == 'admin':
        admin_lib = admin_library.objects.filter(user=response.user).first()
        if admin_lib.library_location != data.book.library_location:
            return redirect('borrow_request_read')
        
    elif response.user.role == 'user':
        if response.user != data.user:
            return redirect('borrow_request_read')
    
    elif response.user.role == 'superadmin':
        pass
    else :
        return redirect('borrow_request_read')
    
    # Delete data
    if response.method == "POST":
        data_book = book.objects.filter(id = data.book.id).first()
        data_book.stock = int(data_book.stock) + 1
        data_book.save()
        data.delete()
        return redirect('borrow_request_read')
    
#endregion ================================= BORROW REQUEST AREA ==========================================================================

#region ================================= BORROW APPROVAL AREA ==========================================================================
@login_required()
def borrow_approval(response, id):
    data = get_object_or_404(br, id=id)

    #Authorisation (Note: Change more specific)
    author = ['superadmin', 'admin']
    if response.user.role not in author:
        return HttpResponseRedirect('/')
    
    if response.user.role == 'admin':
        admin_lib = admin_library.objects.filter(user=response.user).first()
        if admin_lib.library_location != data.book.library_location:
            return redirect('borrow_request_read')

    if response.method == "POST":
        return_date = timezone.now().date() + timedelta(days=14)
        data.is_approved = True
        data.return_date = return_date
        data.save()
    
    return redirect('borrow_request_read')

@login_required()
def borrow_approval_read(response):
    header = "Borrowed Book"

    #Authorisation (Note: Change more specific)
    if response.user.role == 'user':
        data = br.objects.filter(user = response.user, is_approved = True, is_returned = False)

    elif response.user.role == 'admin':
        # Find admin library location
        admin_libraries = admin_library.objects.filter(user=response.user).first()
        library_locations = admin_libraries.library_location
        # Find book from library location
        data_book = book.objects.filter(library_location = library_locations)
        # Find borrowed book from book in each library location
        data = br.objects.filter(book__in=data_book, is_approved = True, is_returned = False)

    elif response.user.role == 'superadmin':
        data = br.objects.filter(is_approved = True, is_returned = False)
    
    return render(response, "borrow/borrowed_book_read.html", {"data":data, "header_content":header})

#endregion ================================= BORROW APPROVAL AREA ==========================================================================


#region ================================= RETURN AREA ==========================================================================
@login_required()
def borrow_return_read(response):
    header = "Return Book"

    #Authorisation (Note: Change more specific)
    if response.user.role == 'user':
        data = br.objects.filter(user = response.user, is_approved = True, is_returned = True)

    elif response.user.role == 'admin':
        # Find admin library location
        admin_libraries = admin_library.objects.filter(user=response.user).first()
        library_locations = admin_libraries.library_location
        # Find book from library location
        data_book = book.objects.filter(library_location = library_locations)
        # Find borrowed book from book in each library location
        data = br.objects.filter(book__in=data_book, is_approved = True, is_returned = True)

    elif response.user.role == 'superadmin':
        data = br.objects.filter(is_approved = True, is_returned = True)
    
    return render(response, "borrow/return_book_read.html", {"data":data, "header_content":header})

@login_required()
def borrow_return(response, id):
    data = get_object_or_404(br, id=id)

    #Authorisation (Note: Change more specific)
    author = ['superadmin', 'admin']
    if response.user.role not in author:
        return HttpResponseRedirect('/')
    
    if response.user.role == 'admin':
        admin_lib = admin_library.objects.filter(user=response.user).first()
        if admin_lib.library_location != data.book.library_location:
            return redirect('borrow_approval_read')

    if response.method == "POST":
        data.is_returned = True
        data.save()
        
        #Add stock
        data_book = book.objects.filter(id = data.book.id).first()
        data_book.stock = int(data_book.stock) + 1
        data_book.save()

    return redirect('borrow_approval_read')

#endregion ================================= RETURN AREA ==========================================================================
