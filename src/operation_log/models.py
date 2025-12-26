from django.db import models
from django.contrib.auth.models import User


class OperationType(models.TextChoices):
    CREATE = 'CREATE', '创建'
    UPDATE = 'UPDATE', '更新'
    DELETE = 'DELETE', '删除'


class OperationLog(models.Model):
    operator = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        db_index=True,
        verbose_name='操作人',
        help_text='执行此操作的用户',
    )
    operate_time = models.DateTimeField(
        auto_now_add=True,
        db_index=True,
        verbose_name='操作时间',
        help_text='操作执行的时间',
    )
    operation_type = models.CharField(
        max_length=20,
        choices=OperationType.choices,
        db_index=True,
        verbose_name='操作类型',
        help_text='操作的类型：CREATE/UPDATE/DELETE',
    )
    content_type = models.CharField(
        max_length=255,
        db_index=True,
        verbose_name='模型标识',
        help_text='被操作对象的模型，格式：app_label.ModelName',
    )
    object_id = models.CharField(
        max_length=255,
        db_index=True,
        verbose_name='对象ID',
        help_text='被操作对象的主键ID',
    )
    old_values = models.JSONField(
        null=True,
        blank=True,
        verbose_name='修改前的值',
        help_text='对象修改前的数据，JSON格式',
    )
    new_values = models.JSONField(
        null=True,
        blank=True,
        verbose_name='修改后的值',
        help_text='对象修改后的数据，JSON格式',
    )

    class Meta:
        db_table = 'operation_log'
        verbose_name = '操作日志'
        verbose_name_plural = '操作日志'
        ordering = ['-operate_time']
        indexes = [
            models.Index(fields=['content_type', 'object_id']),
            models.Index(fields=['operator', 'operate_time']),
        ]

    def __str__(self):
        return f'{self.operator} - {self.operation_type} - {self.content_type}:{self.object_id}'
