from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import RegisterForm, UpdateProfileForm, UserUpdateForm


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully! Please log in.")
            return redirect('login')
    else:
        form = RegisterForm()

    return render(request, 'users/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, "Invalid username or password")

    return render(request, 'users/login.html')


def logout_view(request):
    logout(request)
    messages.success(request, "Log out successful!")
    return redirect('login')


@login_required
def profile_view(request):
    user = request.user
    profile = user.profile

    if request.method == "POST":
        user_form = UserUpdateForm(request.POST, instance=user)
        profile_form = UpdateProfileForm(request.POST, request.FILES, instance=profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, "Profile Update successful!")
            return redirect('profile')
    else:
        user_form = UserUpdateForm(instance=user)
        profile_form = UpdateProfileForm(instance=profile)

    return render(request, "users/profile.html", {
        "user_form": user_form,
        "profile_form": profile_form,
        "profile": profile,
    })


@login_required
def dashboard_view(request):
    
    return render(request, 'users/dashboard.html')
