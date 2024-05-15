from rest_framework import serializers
from django.contrib.auth.models import User


class RegisterSerializer(serializers.Serializer):
    username = serializers.EmailField(
        min_length=5,
        max_length=100,
        allow_blank=False,
        allow_null=False,
        required=True
    )
    name = serializers.CharField(
        min_length=2,
        max_length=100,
        allow_blank=False,
        allow_null=False,
        required=True
    )
    password = serializers.CharField(
        min_length=6,
        max_length=100,
        allow_blank=False,
        allow_null=False,
        required=True
    )
    password_repeat = serializers.CharField(
        min_length=6,
        max_length=100,
        allow_blank=False,
        allow_null=False,
        required=True
    )

    def validate(self, data):
        if data['password'] != data['password_repeat']:
            raise serializers.ValidationError({'message': '两次密码不一致'}, code='password_mismatch')

        if User.objects.filter(username=data['username']).exists():
            raise serializers.ValidationError({'message': '用户名已存在'}, code='username_exists')

        return data


class PasswordResetSerializer(serializers.Serializer):
    ext_user_id = serializers.IntegerField(
        allow_null=False,
        required=True,
    )
    new_password = serializers.CharField(
        min_length=6,
        max_length=100,
        allow_blank=False,
        allow_null=False,
        required=True
    )
    new_password_repeat = serializers.CharField(
        min_length=6,
        max_length=100,
        allow_blank=False,
        allow_null=False,
        required=True
    )

    def validate(self, data):
        if not self.context['request'].user.is_superuser:
            raise serializers.ValidationError({'message': '您无权执行次操作'})

        if data['new_password'] != data['new_password_repeat']:
            raise serializers.ValidationError({'message': '两次密码不一致'}, code='password_mismatch')

        return data


class LockSerializer(serializers.Serializer):
    ext_user_id = serializers.IntegerField(
        required=True,
    )
    status = serializers.BooleanField(
        required=True,
    )

    def validate(self, data):
        if not self.context['request'].user.is_superuser:
            raise serializers.ValidationError({'message': '您无权执行次操作'})
        return data
