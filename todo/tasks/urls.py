from django.urls import path, include
from .views import home, task_status, TaskViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'tasks', TaskViewSet)

urlpatterns = [
    path('', home, name='home'),
    path('<int:pk>/', task_status, name='task_status'),
    path('api_home/',include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]