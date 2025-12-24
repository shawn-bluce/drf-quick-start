import sys
import logging
from pathlib import Path
from loguru import logger


# 1. 定义拦截处理器，将标准 logging 转发给 loguru
class InterceptHandler(logging.Handler):
    def emit(self, record):
        # 获取对应的 Loguru 日志级别
        try:
            level = logger.level(record.levelname).name
        except ValueError:
            level = record.levelno

        # 查找调用者
        frame, depth = logging.currentframe(), 2
        while frame.f_code.co_filename == logging.__file__:
            frame = frame.f_back
            depth += 1

        logger.opt(depth=depth, exception=record.exc_info).log(level, record.getMessage())


# def user_module_filter(record):
#     return record["extra"].get("module") == "users"


# 3. 配置 Loguru
def setup_logging():
    # 移除默认的 Handler
    logger.remove()

    # 格式化配置
    log_format = "<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>"

    # --- Sink 1: 终端输出 (INFO 及以上) ---
    logger.add(
        sys.stdout,
        format=log_format,
        level="INFO",
        colorize=True
    )

    # --- Sink 2: 全局日志文件 (DEBUG 及以上，包含轮转) ---
    # rotation: 10 MB 一个文件; retention: 保留 30 天; compression: zip 压缩旧文件
    logger.add(
        Path("logs/app_{time:YYYY-MM-DD}.log"),
        format=log_format,
        level="DEBUG",
        rotation="10 MB",
        retention="30 days",
        compression="zip",
        encoding="utf-8"
    )

    # logger.add(
    #     Path("logs/users_{time:YYYY-MM-DD}.log"),
    #     format=log_format,
    #     level="DEBUG",
    #     filter=user_module_filter,
    #     rotation="10 MB",
    #     retention="30 days",
    #     encoding="utf-8"
    # )

    # 4. 设置标准 logging 的行为
    # 替换 Django 默认的 logging 配置
    logging.basicConfig(handlers=[InterceptHandler()], level=0, force=True)

    # 忽略一些过于嘈杂的第三方库日志
    for logger_name in ["django.db.backends", "uvicorn.access"]:
        logging_logger = logging.getLogger(logger_name)
        logging_logger.handlers = [InterceptHandler()]
        logging_logger.propagate = False
