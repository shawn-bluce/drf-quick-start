from django.contrib import admin
from .models import OperationLog


@admin.register(OperationLog)
class OperationLogAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'operator',
        'operation_type',
        'content_type',
        'object_id',
        'operate_time',
    ]
    list_filter = ['operation_type', 'content_type', 'operate_time']
    search_fields = ['operator__username', 'object_id', 'content_type']
    readonly_fields = [
        'operator',
        'operate_time',
        'operation_type',
        'content_type',
        'object_id',
        'old_values',
        'new_values',
    ]
    ordering = ['-operate_time']

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser
