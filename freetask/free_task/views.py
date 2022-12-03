from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def HomePage(request):
    return render(request, 'free_task/index.html',{})

def Register(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        user_name = request.POST.get('uname')
        email = request.POST.get('email')
        password = request.POST.get('pword')

        new_user = User.objects.create_user(user_name, email, password)
        new_user.first_name = fname
        new_user.last_name = lname
        new_user.save()
        return redirect('login-page')

    return render(request, 'free_task/register.html',{})

def LogIn(request):
    if request.method == 'POST':
        user_name = request.POST.get('uname')
        password = request.POST.get('pword')

        user = authenticate(request, username=user_name, password=password)
        if user is not None:
            login(request, user)
            return redirect('home-page')
        else: 
            return HttpResponse('Error, user does not exist')

    return render(request, 'free_task/login.html',{})

def LogOut(request):
    logout(request)
    return redirect('login-page')
