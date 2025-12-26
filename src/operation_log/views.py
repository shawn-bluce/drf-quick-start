from rest_framework import viewsets, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from .models import OperationLog
from .serializers import OperationLogSerializer


class OperationLogViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = OperationLog.objects.all()
    serializer_class = OperationLogSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = {
        'operator': ['exact'],
        'operation_type': ['exact'],
        'content_type': ['exact'],
        'object_id': ['exact'],
        'operate_time': ['gte', 'lte', 'exact'],
    }
    ordering_fields = ['operate_time', 'id']
    ordering = ['-operate_time']

    def get_queryset(self):
        queryset = super().get_queryset()
        username = self.request.query_params.get('operator__username', None)
        if username:
            queryset = queryset.filter(operator__username=username)
        return queryset

    @action(detail=False, methods=['get'])
    def by_object(self, request):
        content_type = request.query_params.get('content_type')
        object_id = request.query_params.get('object_id')

        if not content_type or not object_id:
            return Response(
                {'error': '必须提供 content_type 和 object_id 参数'},
                status=400
            )

        logs = self.queryset.filter(
            content_type=content_type,
            object_id=str(object_id)
        )
        serializer = self.get_serializer(logs, many=True)
        return Response(serializer.data)
