from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.success(request, ("Błędna nazwa użytkownika lub hasło"))
            return redirect('login')
    else:
        return render(request, 'login_app/html/index.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, ("Wylogowano"))
    return redirect('login')