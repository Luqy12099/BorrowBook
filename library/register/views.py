from django.shortcuts import render, redirect
from .form import form as fm
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

#another
from crispy_forms.helper import FormHelper 

# Create your views here.
@login_required
def base(response):
    return render(response, "register/base.html")

def register(response):
    if response.method =="POST":
        form = fm(response.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/login') 
    else:
        form = fm()
    return render(response, "register/register.html", {"form":form})

def logout_view(response):
    logout(response)
    return HttpResponseRedirect('/login')
