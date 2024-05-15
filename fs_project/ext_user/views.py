import django_filters
from rest_framework import permissions, viewsets, status, mixins

from ext_user.models import ExtUser
from ext_user.serializers import ExtUserSerializer
from ext_user.filters import ExtUserFilter


class ExtUserViewSet(viewsets.ModelViewSet):

    queryset = ExtUser.objects.all().order_by('-id')
    serializer_class = ExtUserSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
    filterset_class = ExtUserFilter

    def get_queryset(self):
        if self.request.user.is_superuser:
            return self.queryset

        return self.queryset.filter(id=self.request.user.extuser.id)
