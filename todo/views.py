from sqlite3 import IntegrityError
from this import d
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
# Create your views here.


def signupuser(req):
    if req.method == 'GET':
        return render(req, 'todo/signupuser.html', {'form': UserCreationForm()})
    if req.method == 'POST':
        if req.POST['password1'] == req.POST['password2']:
            try:
                user = User.objects.create_user(
                    req.POST['username'], password=req.POST['password1'])
                user.save()
                login(req, user)
                return redirect('currenttodos')
            except IntegrityError:
                return render(req, 'todo/signupuser.html', {'form': UserCreationForm(), 'error': 'Username already Exist.'})

        else:
            return render(req, 'todo/signupuser.html', {'form': UserCreationForm(), 'error': 'Passwords did not match'})


def home(req):
    return render(req, 'todo/home.html')


def currenttodos(req):
    return render(req, 'todo/currenttodos.html')


def logoutuser(req):
    if req.method == 'POST':
        logout(req)
        return redirect('home')


def loginuser(req):
    if req.method == 'GET':
        return render(req, 'todo/loginuser.html', {'form': AuthenticationForm()})
    if req.method == 'POST':
        user = authenticate(
            req, username=req.POST['username'], password=req.POST['password'])
        if user is None:
            return render(req, 'todo/loginuser.html', {'form': AuthenticationForm(), 'error': 'Username and Password did not match'})
        else:
            login(req, user)
            return redirect('currenttodos')
