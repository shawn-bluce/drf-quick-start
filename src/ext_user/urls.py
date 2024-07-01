from django.urls import include, path
from rest_framework import routers

from ext_user.views import ExtUserViewSet


router = routers.DefaultRouter()
router.register(r'ext_user', ExtUserViewSet, basename='ext_user')

urlpatterns = [
    path('', include(router.urls)),
]