import inspect
import logging

from loguru import logger


class InterceptHandler(logging.Handler):
    """
    日志拦截处理器，用于将日志重定向到 loguru
    """

    def emit(self, record: logging.LogRecord) -> None:
        # 获取loguru的级别
        try:
            level = logger.level(record.levelname).name
        except ValueError:
            level = record.levelno

        # 查找记录日志消息的调用者
        frame, depth = inspect.currentframe(), 0
        while frame and (depth == 0 or frame.f_code.co_filename == logging.__file__):
            frame = frame.f_back
            depth += 1

        logger.opt(depth=depth, exception=record.exc_info).log(level, record.getMessage())