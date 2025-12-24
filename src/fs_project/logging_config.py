import sys
import logging
from pathlib import Path
from loguru import logger

from fs_project.log_sender import send_error_notification


class InterceptHandler(logging.Handler):
    def emit(self, record):
        try:
            level = logger.level(record.levelname).name
        except ValueError:
            level = record.levelno

        frame, depth = logging.currentframe(), 2
        while frame.f_code.co_filename == logging.__file__:
            frame = frame.f_back
            depth += 1

        logger.opt(depth=depth, exception=record.exc_info).log(level, record.getMessage())


# def user_module_filter(record):
#     return record["extra"].get("module") == "users"


def setup_logging():
    logger.remove()

    log_format = "<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>"

    logger.add(
        sys.stdout,
        format=log_format,
        level="INFO",
        colorize=True
    )

    logger.add(
        Path("logs/app_{time:YYYY-MM-DD}.log"),
        format=log_format,
        level="DEBUG",
        rotation="10 MB",
        retention="30 days",
        compression="zip",
        encoding="utf-8"
    )

    # --- Sink: ERROR 报警 Hook ---
    logger.add(
        send_error_notification,
        level="ERROR",
        serialize=True,    # using dict data
        enqueue=True,      # async
        backtrace=True,    # track full stack trace
        diagnose=True
    )

    logging.basicConfig(handlers=[InterceptHandler()], level=0, force=True)

    # ignore some useless loggers
    for logger_name in ["django.db.backends", "uvicorn.access"]:
        logging_logger = logging.getLogger(logger_name)
        logging_logger.handlers = [InterceptHandler()]
        logging_logger.propagate = False
