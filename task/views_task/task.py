from rest_framework import viewsets, permissions, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from account.permissions import IsOwnerProjectOrAssign, TaskMemberPermission
from task.models import Task
from task.pagination import CustomPagination
from task.serializers import TaskSerializer, TaskCreateSerializer, TaskProjectSerializer
from task.task import add


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskProjectSerializer
    pagination_class = CustomPagination
    # serializer_class = TaskSerializer
    # permission_classes = [IsAuthenticated,]

    # def get_queryset(self):
    #     queryset = Task.objects.all()
    #     # add(6,9)
    #     return queryset


    # def get_permissions(self):
    #     # print(self.request.user),print(self.action)
    #     if self.action in ['update', 'partial_update', 'destroy']:
    #         return [IsOwnerProjectOrAssign()]
    #     elif self.action in ['list', 'retrieve']:
    #         # print(self.request.user)
    #         return [TaskMemberPermission(),]
    #     return [IsAuthenticated(),]

    # def create(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response(serializer.data, status=status.HTTP_201_CREATED)
    #
    # def list(self, request, *args, **kwargs):
    #     queryset = self.get_queryset()
    #     serializer = self.get_serializer(queryset, many=True)
    #     return Response(serializer.data)
    #
    # def retrieve(self, request, *args, **kwargs):
    #     queryset = self.get_object()
    #     serializer = self.get_serializer(queryset)
    #     return Response(serializer.data)
    #
    # def put(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response(serializer.data)
    #
    # def patch(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response(serializer.data)
    #
    # def destroy(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)
    #

    # def get_serializer_class(self):
    #     if self.action in ['create','update', 'partial_update', 'destroy']:
    #         return TaskCreateSerializer
    #     return self.get_serializer()












