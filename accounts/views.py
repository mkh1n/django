
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate

def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f'Добро пожаловать, {user.get_full_name() or user.username}!')
            return redirect('products.products_list')
        else:
            messages.error(request, 'Не верное имя пользователя или пароль.')
    return render(request, 'accounts/login.html')

def logout_view(request):
    logout(request)
    messages.info(request, "Вы успешно вышли из системы")
    return redirect("accounts:login")


def profile_view(request):
    return render(request, 'accounts/profile.html')