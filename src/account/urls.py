from django.urls import include, path
from rest_framework import routers


from account.views import RegisterView, PasswordResetView, LockViewSet


urlpatterns = [
    path(r'register', RegisterView.as_view(), name='register'),
    path(r'password_reset', PasswordResetView.as_view(), name='password_reset'),
    path(r'lock', LockViewSet.as_view(), name='lock'),
]
