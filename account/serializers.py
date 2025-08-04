from rest_framework import serializers

from account.models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email','password')
        extra_kwargs = {'password': {'write_only': True}}


    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        return user

    # def validate_username(self, value):
    #     if len(value) <8:
    #         raise serializers.ValidationError('username must be between 30 characters')
    #     return value

