from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import Register_user, UserUpdateForm

def profile(request):
    if request.method == 'POST':
        update_profle = UserUpdateForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f"Account Updated successfully!")
            return redirect('profile')
        else:
            form = UserUpdateForm()
    return render(request, "users/profile.html", {"form":form})

def register(request):
    if request.method == 'POST':
        form = Register_user(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"Account created for {username}!")
            return redirect('login')
    
    else:
        form = Register_user()
    return render(request, 'users/login.html',{"form": form})
    