from django.contrib.postgres.aggregates import ArrayAgg
from django.db.models import F
from django.shortcuts import render
from rest_framework import viewsets, permissions
from rest_framework.authentication import TokenAuthentication

from task.models import Task, Project
from task.serializers import TaskQuerySerializer, ProjectQuerySerializer
# from task.task_models.project import Project


# Create your views here.


class TaskQueryViewSet(viewsets.ModelViewSet):
    # queryset = Task.objects.select_related('project').annotate(
    #     project_n=F('project__name')
    # )
    queryset = Task.objects.select_related("project").all()
    serializer_class = TaskQuerySerializer
    # permission_classes = [permissions.IsAuthenticated,]
    # authentication_classes = [TokenAuthentication,]
    #
    # def get_queryset(self):
    #     queryset = Task.objects.select_related("project").all()
    #     return queryset

class ProjectQueryViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.annotate(
        task_titles=ArrayAgg('task_project__title')
    ).all()
    # queryset = Project.objects.prefetch_related("task_project").all()
    # queryset = Project.objects.all()
    serializer_class = ProjectQuerySerializer
    # Project.objects.row("select ")
