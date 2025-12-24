from django.urls import path

from common_check.views import HealthCheckView


urlpatterns = [
    path(r'health', HealthCheckView.as_view(), name='health'),
]
