from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, SignupForm

def LoginView(request):
    params = {
        'title': 'LOGIN',
        'form': LoginForm,
        'message': '',
    }
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/home')
        else:
            params['message'] = 'パスワードもしくはユーザー名が間違えています'
    return render(request, 'accounts/login.html', params)

def SignupView(request):
    params = {
        'title': 'SIGNUP',
        'form': SignupForm,
        'message': '',
    }
    print(request.method)
    if request.method == 'POST':
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        try:
            User.objects.create_user(username, email, password)
        except IntegrityError:
            params['message'] = 'すでに登録されています'
            return render(request, 'accounts/signup.html', params)
    else:
        return render(request, 'accounts/signup.html', params)
    return render(request, 'accounts/signup.html', params)

@login_required(login_url='/accounts/login/')
def LogoutView(request):
    logout(request)
    return redirect('/')