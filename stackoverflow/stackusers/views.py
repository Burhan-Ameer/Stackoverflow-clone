from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth import authenticate, logout, login as auth_login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Profile
def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"Account successfully created for {username}")
            return redirect("home")  # Ensure 'login' is a valid URL name in your urls.py
    else:
        form = UserRegisterForm()
    return render(request, "register.html", {"form": form})

def login_page(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                messages.success(request, f"Welcome back, {username}!")
                return redirect("home")  # Ensure 'home' is a valid URL name in your urls.py
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    return render(request, "login.html", {"form": form})
def logout_page(request):
    logout(request)
    return redirect("home")
@login_required
def profile(request):
    return render(request,"Profile.html")
@login_required
def update_profile(request):
    profile = Profile.objects.get(user=request.user)
    if request.method == 'POST':
        # Update profile fields
        if 'profile_image' in request.FILES:
            profile.profile_image = request.FILES['profile_image']
        profile.bio = request.POST.get('bio', '')
        profile.phone = request.POST.get('phone', '')
        email = request.POST.get("email")
        if email:
            request.user.email = email
            request.user.save()
        profile.save()
        messages.success(request, 'Profile updated successfully!')
        return redirect('profile')
    
    return render(request, "update_profile.html", {'profile': profile})