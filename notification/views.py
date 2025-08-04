from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from notification.models import Notification
from notification.serializers import NotificationSerializer, EmptySerializer


# Create your views here.


class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    permission_classes = (IsAuthenticated,)
    def get_serializer_class(self):
        if self.action == 'retrieve':
            return NotificationSerializer
        elif self.action == 'mark_all_as_read':
            return EmptySerializer
        return self.serializer_class

    def get_queryset(self):
        return self.queryset.filter(to_user=self.request.user, is_read=False)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.is_read = True
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    @action(methods=['put'], detail=False)
    def mark_all_as_read(self, request):
        Notification.objects.filter(to_user=self.request.user, is_read=False).update(is_read=True)
        return Response({'message': 'success'})

    @action(methods=['get'], detail=False)
    def unread_count(self, request):
        count = self.get_queryset().count()
        return Response({'unread_count': count})