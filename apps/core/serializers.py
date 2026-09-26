from django.contrib.auth.tokens import PasswordResetTokenGenerator
from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer
from djoser.serializers import UserSerializer as BaseUserSerializer
from rest_framework import serializers
from rest_framework.exceptions import AuthenticationFailed

from .models import User

# serializers for create user


class UserCreateSerializer(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        fields = ["id", "username", "password", "email", "first_name", "last_name"]


class UserSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        ref_name = "CustomUser"
        fields = ["id", "username", "email", "first_name", "last_name"]


class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["first_name", "last_name"]


class ChangePasswordSerializer(serializers.Serializer):
    model = User
    """
    Serializer for password change endpoint.
    """
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)


class ResetPasswordEmailRequestSerializer(serializers.Serializer):
    email = serializers.EmailField(min_length=2)

    class Meta:
        fields = ["email"]


class SetNewPasswordSerializer(serializers.Serializer):
    password = serializers.CharField(min_length=6, max_length=68, write_only=True)
    token = serializers.CharField(min_length=1, write_only=True)
    email = serializers.EmailField()

    class Meta:
        fields = ["password", "token", "email"]

    def validate(self, attrs):
        try:
            user = User.objects.get(email=attrs.get("email"))
        except User.DoesNotExist:
            raise AuthenticationFailed("The reset link is invalid", 401) from None
        if not PasswordResetTokenGenerator().check_token(user, attrs.get("token")):
            raise AuthenticationFailed("The reset link is invalid", 401)
        user.set_password(attrs.get("password"))
        user.save()
        return user
