from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm

from .forms import CustomUserCreationForm, CustomAuthenticationForm


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('main')  # Замените 'main' на URL вашей стартовой страницы
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            remember_me = request.POST.get('remember_me')
            user = form.get_user()
            login(request, user)

            if not remember_me:
                request.session.set_expiry(0)
            return redirect('main')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

