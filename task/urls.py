from django.urls import path, include
from rest_framework.routers import DefaultRouter

from task.views import TaskQueryViewSet, ProjectQueryViewSet
from task.views_task.project import ProjectViewSet
from task.views_task.task import TaskViewSet

router = DefaultRouter()
router.register('projects', ProjectViewSet, basename='project')
router.register('task', TaskViewSet, basename='task')
router.register('taskquery', TaskQueryViewSet, basename='taskquery')
router.register('projectquery', ProjectQueryViewSet, basename='projectquery')

urlpatterns = [
    path('',include(router.urls)),

]