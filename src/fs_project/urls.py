from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)


urlpatterns = [
    path('admin/', admin.site.urls),

    path('account/', include('account.urls')),
    path('ext_user/', include('ext_user.urls')),

    # user about
    path(r'token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path(r'token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path(r'token/verify/', TokenVerifyView.as_view(), name='token_verify'),

]
