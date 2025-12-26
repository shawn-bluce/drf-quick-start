from .models import OperationLog, OperationType


def create_operation_log(
    operator,
    operation_type,
    instance,
    old_values=None,
    new_values=None,
):
    content_type = f'{instance._meta.app_label}.{instance._meta.model_name}'
    object_id = str(instance.pk)

    log = OperationLog.objects.create(
        operator=operator,
        operation_type=operation_type,
        content_type=content_type,
        object_id=object_id,
        old_values=old_values,
        new_values=new_values,
    )

    return log


def model_to_dict(instance):
    from django.forms.models import model_to_dict as django_model_to_dict

    return django_model_to_dict(instance)
