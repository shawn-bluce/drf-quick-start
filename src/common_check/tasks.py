from celery import shared_task
from loguru import logger

@shared_task(name='common_check.celery_health_check')
def celery_health_check():
    logger.info("Celery health check task executed successfully.")
    return