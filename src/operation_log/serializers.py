from rest_framework import serializers
from .models import OperationLog


class OperationLogSerializer(serializers.ModelSerializer):
    operator_name = serializers.CharField(
        source='operator.username',
        read_only=True,
        allow_null=True,
    )
    operation_type_display = serializers.CharField(
        source='get_operation_type_display',
        read_only=True,
    )

    class Meta:
        model = OperationLog
        fields = [
            'id',
            'operator',
            'operator_name',
            'operate_time',
            'operation_type',
            'operation_type_display',
            'content_type',
            'object_id',
            'old_values',
            'new_values',
        ]
        read_only_fields = fields
