# Create your views here.
from myauth import forms,models
from django.shortcuts import render,redirect,HttpResponseRedirect
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User  
from django.contrib.auth import authenticate , login as auth_login,logout as auth_logout
from django.contrib.auth.decorators import login_required


def index(request):
    d={}
    return render(request,"myauth/index.html",d)


def login(request):
    if request.user.is_authenticated:
        return redirect("/main/home")
    else:
        form = forms.LoginForm()
        if(request.method == "POST"):
            form  = forms.LoginForm(request.POST)
            if(form.is_valid()):
                username = form.cleaned_data["username"]
                password = form.cleaned_data["password"]
                user = authenticate(username=username,password=password)
                if(user):
                    auth_login(request,user)
                    messages.info(request,"You are logged in succesfully")
                    return redirect("/main/home")
                else:
                    messages.error(request,"Invalid username or password")
            else:
                messages.error(request,"Invalid username or password")
        d = {
            "form" : form 
        }
        return render(request,"myauth/login.html",d)

@login_required(login_url='login')
def logout(request):
    auth_logout(request)
    messages.success(request,"Logged out successfully")
    return redirect("/main/home")


def signUp(request):
    if request.user.is_authenticated:
        return redirect("/main/home")
    else:
        form = forms.SignUpForm()
        if(request.method == "POST"):
            form  = forms.SignUpForm(request.POST)
            if(form.is_valid() and form.cleaned_data["password"] == form.cleaned_data["password_confirm"]):
                password = form.cleaned_data["password"]
                first_name = form.cleaned_data["first_name"]
                last_name = form.cleaned_data["last_name"]
                username = form.cleaned_data["username"]
                email = form.cleaned_data["email"]
                
                user = User.objects.create_user(username,email,password)
                user.first_name = first_name
                user.last_name = last_name
                user.save()
                messages.success(request,"Welcome to our site")
                messages.success(request,"Thanks for signing up")
                return redirect("/main/home")
            elif(form.cleaned_data["password"] != form.cleaned_data["password_confirm"]):
                form.add_error("password_confirm","Password do not match")
        d = {
            "form" : form 
        }
        return render(request,"myauth/signup.html",d)