from django.shortcuts import render, redirect
from .models import Task
from django.views.generic import CreateView
from .forms import Create_task
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    if request.method == 'POST':
        form = Create_task(request.POST)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            messages.success(request, f"Task added")
            return redirect('home')
    else:
        form = Create_task()
    context = {
        "tasks": Task.objects.all(),
        'form': form
    }
    return render(request, "tasks/home.html", context)
