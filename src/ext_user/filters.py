import django_filters

from ext_user.models import ExtUser


class ExtUserFilter(django_filters.FilterSet):
    active = django_filters.BooleanFilter(
        field_name='user__is_active',
    )
    username = django_filters.CharFilter(
        field_name='user__username',
        lookup_expr='icontains',
    )
    name = django_filters.CharFilter(
        field_name='name',
        lookup_expr='icontains',
    )
    gender = django_filters.CharFilter(
        field_name='gender',
        lookup_expr='exact',
    )

    order_by = django_filters.OrderingFilter(
        fields=(
            ('id', 'id'),
        )
    )

    class Meta:
        model = ExtUser
        fields = []
