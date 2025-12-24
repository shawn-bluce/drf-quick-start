import os
from celery import Celery

# 设置默认 Django settings 模块
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fs_project.settings')

app = Celery('config')

# 从 Django settings 中读取配置，命名空间为 'CELERY'
app.config_from_object('django.conf:settings', namespace='CELERY')

# 自动发现所有 installed apps 中的 tasks.py
app.autodiscover_tasks()

# 配置定时任务（也可以放在 settings.py 中）
app.conf.beat_schedule = {
    'celery-health-check': {
        'task': 'common_check.tasks.celery_health_check',
        'schedule': 30.0,
    },
}