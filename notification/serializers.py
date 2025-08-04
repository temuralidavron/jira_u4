from rest_framework import serializers

from notification.models import Notification


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = [
            'id',
            'title',
            'descriptions',
            'to_user',
            'is_read',
            'created_at',
        ]


class EmptySerializer(serializers.Serializer):
    pass