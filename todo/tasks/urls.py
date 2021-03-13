from django.urls import path, include
from .views import home, task_status


urlpatterns = [
    path('', home, name='home'),
    path('<int:pk>/', task_status, name='task_status'),
]