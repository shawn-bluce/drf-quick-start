from django.contrib.auth.models import User
from django.db import transaction
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from account.serializers import RegisterSerializer, PasswordResetSerializer, LockSerializer
from ext_user.models import ExtUser


class RegisterView(APIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = RegisterSerializer(data=request.data)

        if serializer.is_valid():
            username = serializer.validated_data['username']
            name = serializer.validated_data['name']
            password = serializer.validated_data['password']
            with transaction.atomic():
                user = User.objects.create_user(username=username, password=password, is_active=True)
                ExtUser.objects.create(user=user, name=name)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PasswordResetView(APIView):
    serializer_class = PasswordResetSerializer

    def post(self, request, *args, **kwargs):
        serializer = PasswordResetSerializer(data=request.data, context={'request': request})

        if serializer.is_valid():
            student_id = serializer.validated_data['student_id']
            password = serializer.validated_data['new_password']
            with transaction.atomic():
                user = ExtUser.objects.get(id=student_id).user
                user.set_password(password)
                user.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LockViewSet(APIView):
    serializer_class = LockSerializer

    def post(self, request, *args, **kwargs):
        serializer = LockSerializer(data=request.data, context={'request': request})

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        student_id = serializer.validated_data['student_id']
        lock_status = serializer.validated_data['status']

        if student_id is None:
            print(f'no student_id: {student_id}')
            return Response(status=status.HTTP_400_BAD_REQUEST)

        student = ExtUser.objects.filter(id=student_id).first()
        if student is None:
            print(f'no student: {student_id}')
            return Response(status=status.HTTP_400_BAD_REQUEST)

        user = student.user
        user.is_active = lock_status
        user.save()

        return Response(status=status.HTTP_200_OK)
