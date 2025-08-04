from django.contrib.postgres.search import TrigramSimilarity
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status, filters

from task.models import Project
from task.serializers import BaseProjectSerializer, ProjectCreateSerializer
from account.permissions import IsOwnerOrReadOnly


class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = BaseProjectSerializer
    # permission_classes = [IsAuthenticated]
    # filter_backends = [filters.SearchFilter]
    # search_fields = ['name', 'description']
    filter_backends = [DjangoFilterBackend,]
    filterset_fields = ['name', 'description']



    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destroy']:
            return [IsOwnerOrReadOnly()]
        elif self.action in ['list', 'retrieve']:
            return [IsOwnerOrReadOnly()]
        return [IsAuthenticated()]

    def get_serializer_class(self):
        if self.action == 'create':
            return ProjectCreateSerializer
        return self.serializer_class

    # def get_queryset(self):
    #     search_query = self.request.query_params.get('search')
    #     queryset = Project.objects.all()
    #     if search_query:
    #         queryset = queryset.annotate(
    #             similarity=TrigramSimilarity('name', search_query)
    #         ).filter(similarity__gt=0.3).order_by('-similarity')
    #     return queryset

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def list(self, request, *args, **kwargs):
    #     queryset = self.get_queryset()
    #     serializer = self.get_serializer(queryset, many=True)
    #     return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
