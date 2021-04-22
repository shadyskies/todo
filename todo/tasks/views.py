from django.shortcuts import render, redirect
from .models import Task
from django.views.generic import CreateView
from .forms import Create_task
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .serializers import  TaskSerializer
from .models import Task
from rest_framework import viewsets, permissions


@login_required(login_url='login/')
def home(request):
    if request.method == 'POST':
        form = Create_task(request.POST)
        # select_task = Select_task(request.POST)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            # select_task.save()
            messages.success(request, f"Task added")
            return redirect('home')
    else:
        form = Create_task()
        # select_task = Select_task()
    context = {
        "tasks": Task.objects.all(),
        "form": form,
        "user": request.user,
        # "select_task_form": select_task
    }
    return render(request, "tasks/home.html", context)


def task_status(request, pk):
    task = Task.objects.get(id=pk)
    if task.check_done == False:
        task.check_done = True
    task.save()
    return redirect('/')


def update_task_status(request):
    print(request.POST.getlist('check_done'))


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permissions_classes = [permissions.IsAuthenticatedOrReadOnly]