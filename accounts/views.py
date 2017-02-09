from django.shortcuts import render, redirect
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout
)
from .forms import UserLoginForm, UserRegistrationForm, ChangePasswordForm
from django import forms
from django.contrib import messages
# Create your views here.


def login_view(request):
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect("/")
    return render(request, 'blog/login.html', {"form": form})


def register_view(request):
    form = UserRegistrationForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get("password")
        user.set_password(password)
        #make_password(password)
        user.save()
        new_user = authenticate(username=user.username, password=password)
        login(request, new_user)
        return redirect("/")

    context = {
        "form": form,
    }
    return render(request, "blog/register.html", context)


def logout_view(request):
    logout(request)
    return redirect('accounts.views.login_view')


def change_password(request):
    form = ChangePasswordForm(request.POST or None)
    if form.is_valid():
        user = request.user
        username = request.user
        password = form.cleaned_data.get("new_password")
        confirm_password = form.cleaned_data.get("confirm_password")
        if confirm_password != password:
            messages.error(request, 'Passwords didn\'t match' )
            return render(request, "blog/change_password.html", {"form": form})
        user.set_password(password)
        user.save()
        new_user = authenticate(username=username, password=password)
        login(request, new_user)
        messages.success(request, 'Password was successfully changed!')
        return redirect("/")
    return render(request, "blog/change_password.html", {"form": form})

