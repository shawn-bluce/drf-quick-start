import requests

from loguru import logger
from django.conf import settings


def send_error_notification(message):
    """

    """

    if not settings.IS_PROD:
        logger.warning("Skipping error notification in non-production environment.")
        return

    record = message['record']

    # get information from record
    payload = {
        "level": record['level'].name,
        "logger": record['name'],
        "function": record['function'],
        "line": record['line'],
        "message": record['message'],
        "timestamp": str(record['time']),
        "extra": record['extra']
    }

    # get exception stack trace if exists
    if record['exception'] is not None:
        payload["exception"] = record['exception']

    webhook_url = "https://your-monitoring-service.com/api/alerts"

    try:
        requests.post(webhook_url, json=payload, timeout=3)
    except Exception as e:
        # DON'T use logger here to avoid infinite loop
        print(f"Failed to send error notification: {e}")